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
        print("Failed to close database connection {}".format((error)))
#Dijital Verileri İkili Sisteme Dönüştürme
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def writeImg(data,filename):
    with open(filename,'wb') as file:
        file.write(data)

#Customer Eklemek
def ınsertCustomer(AdminId,Name,Surname,TCNo,DateOfBirth,Mail,Gender,ProfilePhoto,Username,Password):
    try:
        connection=getDbConnection()
        cursor=connection.cursor()
        query="INSERT INTO customer(AdminId ,Name,Surname, TCNo, DateOfBirth, Mail, Gender, ProfilePhoto, Username, Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        picture=convertToBinaryData(ProfilePhoto)
        insertCustomer=(AdminId,Name,Surname,TCNo,DateOfBirth,Mail,Gender,picture,Username,Password)
        result=cursor.execute(query,insertCustomer)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert Customer table {}".format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Mysql connection is closed")

#Customer Almak
def readCustomerDetails(customerID):
    try:
        connection = getDbConnection()
        cursor = connection.cursor()
        query = "SELECT *FROM customer WHERE ID=%d"
        cursor.execute(query,customerID)
        records=cursor.fetchall()
        print("Printing Customer Record")
        for row in records:
            print("Customer ID=",row[0])
            print("Admin Id=",row[1])
            print("Name=",row[2])
            print("Surname=",row[3])
            print("TC=",row[4])
            print("Date=",row[5])
            print("Mail=",row[6])
            print("Gender=",row[7])
            print("Profile=",row[8])
            print("Username=",row[9])
            print("Password=",row[10],"\n")
        closeDbConnection(connection)
    except mysql.connector.Error as error:
        print("Failed to read Table {}".format(error))
#Customer Giriş
def CustomerLogin(username,password):
    try:
        connection = getDbConnection()
        cursor = connection.cursor()
        CustomerLogin=(username,password)
        query="SELECT *FROM customer WHERE Username=%s AND Password=%s"
        cursor.execute(query,CustomerLogin)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to Login Customer table {}".format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Mysql connection is closed")

