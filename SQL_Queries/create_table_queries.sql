-- Create Database
Create database SparkNetwork;

use SparkNetwork;

-- Using AES256 Encryption Algorithm

-- Step1:
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'SparkNetwork';

-- Step2:
CREATE CERTIFICATE Spark_Encryption_Certificate WITH SUBJECT = 'Data Encryption';

-- Step3:
CREATE SYMMETRIC KEY SparkEncryptionKey WITH ALGORITHM = AES_256 ENCRYPTION BY CERTIFICATE Spark_Encryption_Certificate;

-- Check the keys:
SELECT name KeyName, 
    symmetric_key_id KeyID, 
    key_length KeyLength, 
    algorithm_desc KeyAlgorithm
FROM sys.symmetric_keys;

-- use command:
USE SparkNetwork;

-- create tables
CREATE TABLE users(
id varchar(1000) PRIMARY KEY,
first_name varbinary(MAX),
last_name varbinary(MAX),
user_address varbinary(MAX),
zipcode varbinary(MAX),
birthdate varbinary(MAX),
income varbinary(MAX),
city varchar(20),
country varchar(20),
email_domain varchar(20),
isSmoking bit,
profession varchar(100),
gender varchar(10),
createdAt datetime,
updatedAt datetime
);

CREATE TABLE subscriptions(
bill_id int NOT NULL IDENTITY (1,1) PRIMARY KEY,
id varchar(1000) NOT NULL,
createdAt datetime NOT NULL,
startDate datetime NOT NULL,
endDate datetime NOT NULL,
subscription_status varchar(10) NOT NULL,
amount float NOT NULL,
FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE message_table(
id varchar(1000) PRIMARY KEY,
createdAt datetime NOT NULL,
sender_id varchar(1000) NOT NULL,
receiver_id varchar(1000) NOT NULL
);