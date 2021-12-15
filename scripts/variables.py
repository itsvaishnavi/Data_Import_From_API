"""
Data class contains all the essential constant data variables.
"""
class Data():
	# API endpoint URL
	baseURL = 'https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/'

	# ---------Database connection Details-----------------
	driver_name = '{ODBC Driver 17 for SQL Server}'
	server_name = 'DESKTOP-7E5IPP2'
	database_name = 'SparkNetwork'
	trusted_connection = 'Yes'
	# -----------------------------------------------------

	# ---------SQL Queries---------------------------------
	open_encryption_query = """OPEN SYMMETRIC KEY SparkEncryptionKey
        DECRYPTION BY CERTIFICATE Spark_Encryption_Certificate;"""

	insert_query_message = """INSERT INTO message_table(id,receiver_id,sender_id,createdAt) VALUES (?,?,?,?)"""

	insert_query_users = """INSERT INTO users(id,first_name,last_name,user_address,zipcode,birthdate,income,city,country,email_domain,isSmoking,profession,gender,createdAt,updatedAt)
	VALUES(?,EncryptByKey(Key_GUID('SparkEncryptionKey'),?),EncryptByKey(Key_GUID('SparkEncryptionKey'),?),EncryptByKey(Key_GUID('SparkEncryptionKey'),?),EncryptByKey(Key_GUID('SparkEncryptionKey'),?),
	EncryptByKey(Key_GUID('SparkEncryptionKey'),?),EncryptByKey(Key_GUID('SparkEncryptionKey'),?),?,?,?,?,?,?,?,?)"""
	
	insert_query_subscription = """
	INSERT INTO subscriptions(id,createdAt,startDate,endDate,subscription_status,amount)
	VALUES(?,?,?,?,?,?)
	"""
	# -----------------------------------------------------

	# -----------Dictionary for the keys which can have null values------------------------

	k_data = {
    'users': ['firstName','lastName','address','zipCode','birthDate','city','country','email'],
    'users_profile' : ['income','isSmoking','profession','gender']
    }
    # -------------------------------------------------------------------------------------