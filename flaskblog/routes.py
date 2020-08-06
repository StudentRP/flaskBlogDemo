""" Main routing script """


from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Rory',
        'title': 'blog',
        'content': 'blahhh',
        'date_posted': '04/12/14'
     },
    {
        'author': 'holly',
        'title': 'commander',
        'content': 'Chief',
        'date_posted': '30/01/20'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) # passes left posts to html


@app.route("/about")
def about():
    return render_template('about.html', title="About")# title passed explicitly to html layout


@app.route("/register", methods=["GET", "POST"])
def register():
    """Checks if user is authenticated if true redirects to home.
    Calls Regform from forms.py and assigns it to var form, 2nd rend_temp register.html and passes form var to it.
    Checks posted form.html is valid, hashes pword, creates/adds/commits to db, flash msg and sends to login     """
    if current_user.is_authenticated: # starts false, A proxy for the current user. If no user is logged in,
        # this will be an anonymous user. (user_id) current user is created when
        return redirect(url_for("home")) # if true will route to this place
    form = RegistrationForm() # passes RegistrationForm from import to html vai render_temp(form=form)
    if form.validate_on_submit(): # method associated to wtforms, returns true if submitted.
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # pword hashing
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # associating fields to db
        db.session.add(user) # adding fields to db
        db.session.commit() # committing fields to db
        flash(f"Account created for {form.username.data}! You can now login", "success") # flashes 1 time msg and uses name from form,
        # 2nd arg category and is bootstrap (success)
        return redirect(url_for("login")) # uses funt name not decorator, routes to login if form returns True to all fields
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """flask_login at work login_user"""
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # queries db to find user by email ref and sets to user var
        if user and bcrypt.check_password_hash(user.password, form.password.data): # (db_pword, submitted_pword) user can now do personalised search
            login_user(user, remember=form.remember.data) # ! Flask-Login’s login_user() function is invoked to record the user as logged in for the user session.
            next_page = request.args.get('next') # args is dict. get method does not return error
            flash('You are logged in', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home')) # ternary conditional!!
            # if next_page in this case means None/False redirect to such in such
        else:
            flash('Login failed. Please check email and password', 'danger') # danger give red warning
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user() #
    return redirect(url_for('home'))


@app.route("/account") # function will be registered with Flask as a route.
@login_required # protected by flask-login if this route is accessed by a user who is not authenticated,
# Flask-Login will intercept the request and send the user to the login page instead (login_view).
def account():
    return render_template('account.html', title="Account")





"""This is a test for Git"""



"""

The current_user variable used in the conditional is defined by Flask-Login and is
automatically available to view functions and templates. This variable contains the
currently logged-in user, or a proxy anonymous user object if the user is not logged
in. 

Anonymous user objects have the is_authenticated property set to False, so the
User Authentication expression current_user.is_authenticated is a convenient way to 
know whether the current user is logged in.

"""



