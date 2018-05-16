import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


def createTABLE():
    f="data/users.db"            
    db=sqlite3.connect(f)              #connects to Datebase to allow editing
    c=db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT);"   #creates users table if it doesnt exist
    c.execute(command)
    db.commit()
    db.close()       #closes and commits changes



def insertIntoUserTABLE(tablename, field1, field2):
    f="data/users.db"
    db=sqlite3.connect(f)         #connects to Datebase to allow editing
    c=db.cursor()
    command = "INSERT INTO %s VALUES('%s', '%s');"%(tablename, field1, field2)       #adds user to User Table
    c.execute(command)
    db.commit()
    db.close()       #closes and commits changes


def listUsers(tablename, withPassword, user):
    f="data/users.db"
    db=sqlite3.connect(f)           #connects to Datebase to allow editing
    c=db.cursor()
    if (withPassword):
        command = "SELECT pass FROM %s WHERE name = '%s';"%(tablename, user)    #used for password checking
    else:
        command = "SELECT name FROM %s;"%(tablename)       #returns all users from the table
    c.execute(command)
    listNames = c.fetchall()    #gets all data extracted and puts it in a list
    db.commit()
    db.close()        #closes and commits changes
    return listNames


def listAllUsers():
	f="data/users.db"
	db=sqlite3.connect(f)
	c=db.cursor()
	userList=[]
	for row in c.execute('SELECT name from users'):
		userList.append(row[0])
        db.commit()
        db.close()          #closes and commits changes
	return userList

