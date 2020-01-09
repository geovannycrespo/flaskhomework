from flaskavengerhomework import app, db 
from flask import render_template, redirect, request, url_for
from flaskavengerhomework.forms import SignupForm,LoginForm,PostForm

from werkzeug.security import check_password_hash

from flask_login import login_user, current_user, login_required

from flaskavengerhomework.models import User,Post

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

        user = User(avengername,address,phonenumber)
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

@app.route("/post", methods = ["GET", "POST"])
@login_required
def post():
    postForm = PostForm()
    title = postForm.title.data
    content = postForm.content.data
    user_id = current_user.id 
    print(title,content,user_id)

    # saving post data to database
    post = Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()

    return render_template('create_post.html', postform = postForm)