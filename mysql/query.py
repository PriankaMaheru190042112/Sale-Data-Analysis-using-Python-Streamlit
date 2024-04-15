import mysql.connector

conn= mysql.connector.connect(
host = "localhost",
port = "3306",
db = "mysql",
user = "root",
password = ""
)

c= conn.cursor()

def view_data():
    c.execute('select Invoice_ID,Branch,City from supermarkt_sales')
    data= c.fetchall()
    return data

view_data()
# "Customer_type","Gender","Product line","Unit price","Quantity","Tax 5%","Total","Date","Time","Payment","cogs","gross margin percentage","gross income","Rating"