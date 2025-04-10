from flask import Flask , render_template,redirect,request
from flask import current_app as app
from .models import *

@app.route('/userlogin', methods = ['GET','POST'])
def user_login():
    if request.method == 'POST':
        u_name = request.form.get("u_name")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username = u_name).first()
        if this_user : 
            if this_user.password == pwd :
                return render_template('user_dashboard_mybooks.html')
            else :
                return "Incorrect Password!!"
        else :
            return "User doesn't exist!!"
    return render_template('user_login.html')

@app.route('/userregister', methods = ['GET','POST'])
def user_register():
    if request.method == 'POST':
        u_name = request.form.get("u_name")
        pwd = request.form.get("pwd")
        this_user = User.query.filter_by(username = u_name).first()
        if this_user :
            return "User already exists!!"
        else :
            new_user = User(username = u_name, password = pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/userlogin')
    return render_template('user_registration.html')

@app.route('/librarian', methods = ['GET','POST'])
def librarian_login():
    librarian = User.query.filter_by(type = "librarian").first()
    return render_template("librarian_dashboard_home.html")