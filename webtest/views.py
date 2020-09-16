from django.shortcuts import render
from webtest.models import sqlserverconn
import pyodbc
import random
import os

db_ip = os.getenv('dbip')
db_name = os.getenv('dbname')
db_username = os.getenv('dbuser')
db_password = os.getenv('dbpass')

def connsql(request):
    return render(request , 'index.html' , {'sqlserverconn':query()})

def insert(request):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO  test123 VALUES (1234,'CREATED_BY_DJANGO') ")
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

                   CREATE TABLE test123
                   (
                   number int,
                   firstname nvarchar(50),

                   )

                   ''')

    connect.commit()
    return render(request , 'index.html' , {})

def query():
    server = "10.33.0.199"
    database = 'mheedb_node2'
    global username
    global password
    username = 'sa'
    password = '1qazXSW@'
    print('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+db_ip+'; DATABASE='+db_name+'; UID='+db_username+'; PWD='+db_password)
    cursor=conn.cursor()
    cursor.execute("select * from test123")
    result=cursor.fetchall()
    return result