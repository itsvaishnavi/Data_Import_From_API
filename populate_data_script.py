import requests
import pyodbc
import pandas as pd
from variables import Data

class MainClass():
	def __init__(self):
		self.__d = Data()
		self.__conn = pyodbc.connect(Trusted_Connection=self.__d.trusted_connection,Driver=self.__d.driver_name,Server=self.__d.server_name,Database=self.__d.database_name)
		self.__cur= self.__conn.cursor()

	def get_response(self,api_endpoint):
		response = requests.get(self.__d.baseURL+api_endpoint)
		return response.json()

	def process_response(self,api_endpoint,response):
		if api_endpoint == 'messages':
			for res in response:
				try:
					self.__cur.execute(self.__d.insert_query_message, (res['id'],res['receiverId'],res['senderId'],res['createdAt']))
					self.__conn.commit()
				except Exception as er:
					print("Data with message id",res['id'],'maybe already present!Please check once.')	
					pass

		if api_endpoint == 'users':

			self.__cur.execute(self.__d.open_encryption_query)
			for res in response:
				if res['profile']['isSmoking']==True:
					res['profile']['isSmoking']=1

				if res['profile']['isSmoking']==False:
					res['profile']['isSmoking']=0

				if res['email']!=None:
					res['email'] = res['email'].split('@')[-1]

				if res['profile']['gender']!=None:
					res['profile']['gender'] = res['profile']['gender'].upper()

				try:
					self.__cur.execute(self.__d.insert_query_users,(res['id'],res['firstName'],res['lastName'],res['address'],res['zipCode'],res['birthDate'],res['profile']['income'],res['city'],res['country'],res['email'],res['profile']['isSmoking'],res['profile']['profession'],res['profile']['gender'],res['createdAt'],res['updatedAt']))

					id = res['id']
					if len(res['subscription'])!=0:
						for r in res['subscription']:
							self.__cur.execute(self.__d.insert_query_subscription,(id,r['createdAt'],r['startDate'],r['endDate'],r['status'],r['amount']))
					self.__conn.commit()

				except Exception as e:
					print("Exception occured:",e)

def main():
	mainClass = MainClass()
	response = mainClass.get_response('users')
	mainClass.process_response('users',response)
	response = mainClass.get_response('messages')
	mainClass.process_response('messages',response)

if __name__ == '__main__':
	main()