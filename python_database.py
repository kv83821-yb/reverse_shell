# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:20:56 2020

@author: DELL
"""
import mysql.connector
class Add_User:
    def adduser(username,password):
        my_db = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "@123Bandima")
        # Above line returns a connection object
        #if(my_db):
         #   print("Connection Successful")
        
        cursor = my_db.cursor()
        cursor.execute("use kv83821_db")
        cursor.execute("select * from Users")
        for db in cursor:
            if db[0] == username and db[1] == password:
                return False
        cursor.execute("insert into Users(Name,Password) values(%s,%s)",params = (username,password))
        my_db.commit()
        return True
        
class Login_Check:
    
    def check(username,password):
        my_db = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "@123Bandima")
        # Above line returns a connection object
        #if(my_db):
         #   print("Connection Successful")
        
        cursor = my_db.cursor()
        cursor.execute("use kv83821_db")
        cursor.execute("select * from Users")
        for db in cursor:
            if db[0] == username and db[1] == password:
                return True
        
        return False
        
        # A cursor is used to execute sql commands
        #cursor.execute("Create database kv83821_db")
        
        #cursor.execute("show Databases")
        
        #for db in cursor:
         #   print(db)
            
        
        #cursor.execute("Create table Users(Name varchar(20),Password varchar(20))")
        
        #sql_form = "Insert into Users(Name,Password) values(%s,%s)"
        
        #Users = [("Vivek","xyz"),("Yash","pqr"),]
        #cursor.executemany(sql_form,Users)
        
        #my_db.commit()
        
        #cursor.execute("Select * from Users")
        #"""for db in cursor:
         #   print(db)"""
        #This was one way
        
        #my_result = cursor.fetchall()
        
        #for row in my_result:
         #   print(row)
        
        #This is the other way


        






 