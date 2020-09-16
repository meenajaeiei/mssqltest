from django.shortcuts import render
from webtest.models import sqlserverconn
import pyodbc
import random



def connsql(request):
    return render(request , 'index.html' , {'sqlserverconn':query()})

def insert(request):
    cursor.execute("INSERT INTO  sale VALUES (1234,'CREATED_BY_DJANGO') ")
    cursor.commit()
    return render(request , 'index.html' , {'sqlserverconn':query()})

def query():
    server = "10.33.0.199"
    database = 'mheedb_node2'
    username = 'sa'
    password = '1qazXSW@'
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    global cursor
    cursor=conn.cursor()
    cursor.execute("select * from sale")
    result=cursor.fetchall()
    return result