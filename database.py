import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#Database Bağlantısı Açma
def getDbConnection():
    try:
        connection=mysql.connector.connect(
            host='localhost',
            database='softwaredb',
            user='root',
            password='')
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to database {} ".format(error))

#Database Bağlantısı Kapatma
def closeDbConnection(connection):
    try:
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to close database connection {}".format(error))

#Dijital Verileri İkili Biçime Dönüştürme
def convertToBinaryData(filename):
    with open(filename,'rb') as file:
        binaryData=file.read()
    return binaryData

#ikili verileri uygun biçime dönüştürür
def write_img(data,filename):
    with open(filename,'wb') as file:
        file.write(data)

#Müşteri Ekle
def insertCustomer(admin_ıd,name,surname,photo,mother_name,father_name,gender,birth_city,birth_date,address):
    try:
        connection=getDbConnection()
        cursor=connection.cursor()
        query="INSERT INTO customers(admin_ıd,name,surname,photo,mother_name,father_name,gender,birth_city,birth_date,address) VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        picture=convertToBinaryData(photo)
        insert_customer=(admin_ıd,name,surname,photo,mother_name,father_name,gender,birth_city,birth_date,address)
        result=cursor.execute(query,insert_customer)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to insert Doctor table {}".format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#Müşteri Bilgilerini Almak
def readCustomerDetails(customer_ıd):
    try:
        connection=getDbConnection()
        cursor=connection.cursor()
        query="SELECT *FROM customers WHERE ıd=%s "
        cursor.execute(query,(customer_ıd,))
        records=cursor.fetchall()
        print("Printing Customer Record")
        for row in records:
            print("Customer ID:= ",row[0])
            print("Admin ID:= ", row[1])
            print("Customer Name:= ", row[2])
            print("Customer Surname:= ", row[3])
            image=row[4]
            print("Customer Mother:= ", row[5])
            print("Customer Father:= ", row[6])
            print("Customer Gender:= ", row[7])
            print("Customer Birtyh City:= ", row[8])
            print("Customer Birth Date:= ", row[9])
            print("Customer Address:= ",row[10],"\n")
        closeDbConnection(connection)
    except mysql.connector.Error as error:
        print("Failed to read Doctor table {}".format(error))
readCustomerDetails(1)


