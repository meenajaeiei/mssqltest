from django.shortcuts import render
from webtest.models import sqlserverconn
import pyodbc
import random
import os
import random
import string


db_ip = os.getenv('dbip') #haproxy ip SELECT  CONNECTIONPROPERTY('local_net_address')
#INSERT INTO table2 (column1, column2, column3, ...) SELECT column1, column2, column3, ... FROM table1
db_name = os.getenv('dbname')
db_username = os.getenv('dbuser')
db_password = os.getenv('dbpass')


def get_instance_ip():
    result = ""
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor=conn.cursor()
    cursor.execute("SELECT local_net_address FROM sys.dm_exec_connections")
    result=cursor.fetchone()
    return result

#for insert data

def connsql(request):
    return render(request , 'index.html' , {'sqlserverconn':query()})

def insert(request):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(5))
    address =  ''.join(random.choice(letters) for i in range(10))
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor=conn.cursor()
    print(get_instance_ip())
    #cursor.execute("INSERT INTO SampleTable  VALUES ('"+".".join(str(get_instance_ip()).split('.'))+"','"+db_ip+"') ")
    cursor.execute(" INSERT INTO [dbo].[SampleTable] ([name] ,[address]) VALUES('"+name+"', '"+address+"') ")
    cursor.commit()
    return render(request , 'index.html' , {'sqlserverconn':query()})

def createdb(request):
    print(db_ip)
    print(db_username)
    print(db_password)
    zxc = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db_ip+'; UID='+db_username+'; PWD='+db_password)
    zxc.autocommit = True
    asd = zxc.cursor()
    asd.execute('create database '+db_name+';')
    asd.commit()
    return render(request , 'index.html' , {})

def createtable(request):
    connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor_connect = connect.cursor()
    cursor_connect.execute('''

                   CREATE TABLE SampleTable
                   (

                   proxyip nvarchar(50),
                   instanceip nvarchar(50),
                   test nvarchar(50),

                   )

                   ''')

    connect.commit()
    return render(request , 'index.html' , {})

def query():
    global username
    global password
    username = 'sa'
    password = '1qazXSW@'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor=conn.cursor()
    cursor.execute("select * from SampleTable")
    result=cursor.fetchall()
    return result

