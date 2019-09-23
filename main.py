from flask import Flask, request, render_template, redirect
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def usersignup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verpassword = request.form["verpassword"]
        email = request.form["email"]

        username_error = ""
        password_error = ""
        verpassword_error = ""
        email_error = ""

        if username == "":
            username_error = "Invalid Input. Please provide a username."
        elif len(username) <= 3 or len(username) > 20:
            username_error = "Invalid Input. Please provide a username between 3-20 characters."
            username = ""
        elif " " in username:
            username_error = "Invalid Input. Please don't add a space to your username."
        
        if password == "":
            password_error = "Invalid Input. Please provide a password to login."
        elif len(password) <=3 or len(password) > 20:
            password_error = "Invalid Input. Please enter your password between 3-20 characters." 
        elif " " in password:
            password_error = "Invalid Input. Please don't add a space to your password."
    
        if verpassword == "" or verpassword != password:
            verpassword_error = "Password Don't match!"
            verpassword = ""

        if email != "":
            user_error = "Invalid Input. Please enter an email if you have one."
            if "@" not in email and "." not in email:
                email_error = "Invalid Input. Please provide the domain and domain name."
            elif " " in email:
                email_error = "Invalid Input. Please don't add a space."
            elif len(email) <= 3 or len(email) > 20:
                email_error = "Invalid Input. Please enter your email address between 3-20 characters."
                
        if not username_error and not password_error and not verpassword_error and not email_error:
            return redirect("/welcome?username={0}".format(username))
        else:
            return render_template("index.html", username = username, username_error = username_error, password_error = password_error, verpassword_error = verpassword_error, email = email, email_error = email_error)

@app.route("/welcome")
def welcome_signup():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)

app.run()