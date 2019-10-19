import sqlite3
con=sqlite3.connect("software.db")
cursor=con.cursor()

def tablOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS new_employee(İd PRIMARY KEY,Name TEXT, photo BLOB,resume BLOB)")
    con.commit()

def convertToBinaryData(filename):
    with open(filename,'rb') as file:
        blobData=file.read()
        return blobData
def insertBLOB(empId,name,photo,resumeFile):
    try:
        softwareConnection=sqlite3.connect('software.db')
        cursor=softwareConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query="""INSERT INTO new_empoyee('id','name','photo','resume')
VALUES(?,?,?,?)"""
        empPhoto=convertToBinaryData(photo)
        resume=convertToBinaryData(resumeFile)
        data_tuple=(empId,name,empPhoto,resume)
        cursor.execute(sqlite_insert_blob_query,data_tuple)
        softwareConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
    except software.Error as error:
        print("Failed to insert blob data into sqlite table",error)
    finally:
        if(softwareConnection):
            softwareConnection.close()
            print("the sqlite connect,on is closed")

            
insertBLOB(1,'Joker','C:\\Users\\Lawliet\\Desktop\\db2\\joker.jpg','C:\\Users\\Lawliet\\Desktop\\db2\\joker_life.txt')
insertBLOB(2,'Wonder','C:\\Users\\Lawliet\\Desktop\\db2\\wonder.jpg','C:\\Users\\Lawliet\\Desktop\\db2\\wonder_life.txt')

