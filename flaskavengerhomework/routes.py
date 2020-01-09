from flaskavengerhomework import app, db 
from flask import render_template, redirect, request, url_for
from flaskavengerhomework.forms import SignupForm,LoginForm

from werkzeug.security import check_password_hash

from flask_login import login_user, current_user

from flaskavengerhomework.models import User

#home route
@app.route("/")
def home():
    return render_template("home.html")


 # Sing up Route
@app.route("/signup",methods=["GET","POST"])
def signup():
    signupForm = SignupForm()
    if request.method == 'POST':
    
        avengername = signupForm.avengername.data
        address = signupForm.address.data
        phonenumber = signupForm.phonenumber.data
        print(avengername,phonenumber,address)

        user = User(username,email,password)
        db.session.add(user) # Start Communication with database
        db.session.commit() # Save Data to database and close session
    
    return render_template("signup.html", signupform = signupForm)

@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        # find out who the logged in user currently is
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
        else:
            print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)