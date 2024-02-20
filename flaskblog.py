from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

## setting a secret key
app.config['SECRET_KEY'] = 'def1b1d4d5bf91e42aa3f6a0cf1bf20b'

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
        flash(f'Accounted created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    ## create an instance of the login form
    form = LoginForm()
    return render_template('login.html', title='login', form=form)

## if we want to run this script with python directly
if __name__ == '__main__':
    app.run(debug=True)

## two ways of runing flask apps 
## 1. set environment variables
## 2. including app.run in main app script
