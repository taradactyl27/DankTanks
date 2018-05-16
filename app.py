from flask import Flask, render_template,  request, session, redirect, url_for
from utils import DBbuild
import os, sqlite3, csv, hashlib

myapp = Flask(__name__)
myapp.secret_key="SuperSecretKeyThatIsTooLongToJustRandomlyHackInto"
DBbuild.createTABLE() #creates initial tables if they dont exist already

@myapp.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:     #logs user back in if their session is valid
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title = "Login") # directs to login page


@myapp.route('/home/', methods = ['GET','POST'])
def home():
    if bool(session) != False:       #logs user back in if their session is valid
        return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
    user = request.form['username']
    password = hashlib.md5(request.form['inputPassword3'].encode()).hexdigest() #hashes password with MD5 encryption
    if request.form['submit'] == "Sign up":              #checks if sign up button was pressed
        for entry in DBbuild.listUsers("users", False, ""):
            if (user == entry[0]):           #checks if username isn't already taken, if it is then redirects to error page
                return redirect(url_for('error'))
        DBbuild.insertIntoUserTABLE('users', user, password)        # adds new user to the table of Users
        session['user'] = user    #creates session for the user
        return render_template('listUsers.html', USER = session['user'])
    if request.form['submit'] == "Sign in":          #checks if sign in button was pressed
        for entry in DBbuild.listUsers("users", False, ""):
            if user == entry[0]:     #checks if the user is in the table of Users
                print DBbuild.listUsers("users", True, user)[0][0]
                if password == DBbuild.listUsers("users", True, user)[0][0]:      #checks for password match with attempted user login
                    session['user'] = user #starts session
                    return render_template('listUsers.html', USER = session['user'], listUser=DBbuild.listAllUsers())
        return redirect(url_for('error'))

    
if __name__ == '__main__':
    myapp.debug = True
    myapp.run()        #runs the app
