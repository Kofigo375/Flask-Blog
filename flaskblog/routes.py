from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

 


posts = [
    {
       'author': 'Ephraim Osei',
       'title': 'Blog post one',
       'content': 'First post content in my blog',
       'date_posted': 'Aprill 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog post Two',
        'content': 'second post content in my blog',
        'date_posted': 'Aprill 22, 2024'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    ## create an instance of the Registration form
    form = RegistrationForm()
    ## checking if form validated after submission
    if  form.validate_on_submit():
        # create  account
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data ,password=hashed_password)
        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash(f'Account created!', 'success')
        return redirect(url_for('login'))  ## user will be returned to login page 
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    ## create an instance of the login form
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)
