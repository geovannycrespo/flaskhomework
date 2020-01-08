from flaskavengerhomework import app 
from flask import render_template
from flaskavengerhomework.forms import SignupForm

#home route
@app.route("/")
def home():
    return render_template("home.html")


 # Sing up Route
@app.route("/signup",methods=["GET","POST"])
def signup():
    signupForm = SignupForm()
    
    avengername = signupForm.avengername.data
    address = signupForm.address.data
    phonenumber = signupForm.phonenumber.data
    print(avengername,phonenumber,address)

    return render_template("signup.html", signupform = signupForm)