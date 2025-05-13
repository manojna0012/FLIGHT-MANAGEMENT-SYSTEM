import mysql.connector
'''mydb=mysql.connector.connect(host='localhost',user='root',passwd='Manojna@123')
mycursor=mydb.cursor()
mycursor.execute('create database if not exists MnM')
mycursor.execute('show databases')
for x in mycursor:
    print(x)'''
    

''''def createtable_Fldetails():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Manojna@123',database='MnM')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('create table fldetails (Flno int(20) primary key,Fltype varchar(200) ,Airlinename varchar(100), Seats int(5),Classes int(5),Flweek int(5))')
    mycursor.execute('Desc fldetails')
    for x in mycursor:
        print(x)    
createtable_Fldetails()'''
        
'''def flint():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='lucky@143',database='MnM')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('create table flint (Flno int(20) primary key,airlinename varchar(200) ,arrivalcity varchar(100), departurecity varchar(100),boardingdate varchar(100),arrivaldate varchar(100),triptype varchar(50),noofstops int(4),price float(15,2))')
    mycursor.execute('Desc flint')
    for x in mycursor:
        print(x)
flint()'''

'''def flbookings():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='lucky@143',database='MnM')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('create table flbooking (Flid varchar(100) ,custid varchar(100) ,flname varchar(100), noflyers int(5), Departurecity varchar(100),Boardingdate varchar(100),Arrivalcity varchar(100),Arrivingdate varchar(100),triptype varchar(100),noofstops int(4),layoverloc varchar(100),meal varchar(100))')
    mycursor.execute('Desc flbooking')
    for x in mycursor:
        print(x)
flbookings()'''
        
'''def createtable_hotelbookings():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Manojna@123',database='MnM')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('create table hotelbookings (CustID int(20) primary key,CustName varchar(200) , HotelID int(20),HotelName varchar(200),Guestsno int(5),Roomno int(5),Datechkin varchar(200),Datechkout varchar(200),View char(6),Amenities char(6),Roomtype varchar(200),Breakfast char(6))')
    mycursor.execute('Desc hotelbookings')
    for x in mycursor:
        print(x)

#createtable_hotelbookings()'''

def createtable_Customer():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='lucky@143',database='MnM')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('create table customer (custid int(20),Name varchar(200) ,Age varchar(100), Contact char(15))')
    mycursor.execute('Desc customer')
    for x in mycursor:
        print(x)    
createtable_Customer()


