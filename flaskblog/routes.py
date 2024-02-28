from flask import Flask, render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user,logout_user, current_user, login_required
 


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
    # redirecting an already logged in user to the homepage
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # ## create an instance of the Registration form
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
    # redirecting an already logged in user to the homepage
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    ## create an instance of the login form
    form = LoginForm()
    if form.validate_on_submit():
        # logic for logging a user in 
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # this will return true if user exists and password in database
            login_user(user, remember=form.remember.data) # log user in 
            next_page = request.args.get('next') ## don't really  understand
            # redirect to homepage after login 
            return redirect(next_page) if next_page else redirect(url_for('home')) 
        else:
            flash('Login Failed. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home')) 


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form =  UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', 
                         filename='Default Pictures/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

    
    