"""
This script is for unit testing purpose.
Usage: python -m unittest
"""

# Importing essential libraries
import requests
import unittest
from populate_data_script import MainClass #Importing class 'MainClass' from the python file with name 'populate_data_script.py'
import variables #python file with name 'variables.py'

# Create object of Data class
d = variables.Data()

# class Test inherited from unittest.TestCase
class Test(unittest.TestCase):
	# Test 1: to check the Api response status code
	def test_api_status(self):
		self.resp=requests.get(d.baseURL+'users')
		self.assertTrue(self.resp.status_code == 200, 'API not working. Check the url.')
		self.resp=requests.get(d.baseURL+'messages')
		self.assertTrue(self.resp.status_code == 200, 'API not working. Check the url.')

	# Test 2: to check the Api response content
	def test_api_content(self):
		self.resp=requests.get(d.baseURL+'users')
		self.assertTrue(self.resp.headers['Content-Type'] == 'application/json', 'API response is not json')
		self.resp=requests.get(d.baseURL+'messages')
		self.assertTrue(self.resp.headers['Content-Type'] == 'application/json', 'API response is not json')

	# Test 3: to check the functions written in MainClass of populate_data_script.py
	def test_functions_in_Main_Class(self):
		m = MainClass()

		# Get the response for 'users' endpoint
		response = m.get_response('users')
		assert (response != [-1])

		# Get the response for 'users' endpoint
		response = m.get_response('messages')
		assert (response != [-1])

		# Insert the test response to the database
		message_data = [{"createdAt":"2021-12-24T02:30:13.552Z","message":"Sample message data","receiverId":"92","id":"99","senderId":"99"}]

		m.process_response('messages',message_data)

		# Insert the test response to the database
		user_data = [{"createdAt":"2021-11-29T16:10:33.614Z","updatedAt":"2021-11-29T13:34:15.404Z","firstName":"Michael","lastName":"Smith","address":"Erne Street","zipCode":"95734","email":"user_sample@hotmail.com","birthDate":"2020-12-16T02:41:21.036Z","profile":{"gender":"male","isSmoking":True,"profession":"Central Configuration Planner","income":"3709.61"},
			"subscription":[{"createdAt":"2021-11-24T16:58:46.581Z","startDate":"2022-04-24T05:12:49.301Z","endDate":"2022-09-18T06:05:59.630Z","status":"Active","amount":"43.18"}],'id':'1201'}]

		m.process_response('users',user_data)

if __name__ == '__main__':
	unittest.main()