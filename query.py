import mysql.connector
import streamlit as st

conn= mysql.connector.connect(
host = "localhost",
port = 3306,
database = "mysql",
username = "root",
password = ""
)

c= conn.cursor()

def view_data():
    c.execute('select * from supermarkt_sales')
    data= c.fetchall()
    return data
