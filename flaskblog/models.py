from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader # convention. Binds
def load_user(user_id):
    """The application’s user_loader handler reads the user from the database and returns it.
    Flask-Login assigns it to the current_user context variable for the current request. if no id then returns
    AnonymousUser see pg 113"""
    # since the user_id is just the primary key of our User table, use it in the query for the user
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False) # not unique as ppl want same passwords
    posts = db.relationship('Post', backref='author', lazy=True)  # 1 to many relationship binding author many posts.
    # relationship to 'Post' class, backref similar to adding another column to post model:when post can use author
    # attirb to get user that created post. lazy means  sqlalchemy will load the data in 1 go: when true it will load
    # data as necessary. Can use post attrib to get all post created by that user. note not column just query running
    # in background (Basically says have a relationship with Post, where if author is called give them the user object)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # must use utcnow removes ambiguous
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)# creates relationship with user.id
    # binds to relationship above, user is
    # lowercase as ref table name (user) and column name (id) NOT class ref like above

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



""" 
We start by adding something called the UserMixin to our User model. The UserMixin will add Flask-Login attributes to 
our model so Flask-Login will be able to work with it.

Then, we need to specify our user_loader. A user_loader tells Flask-Login how to find a specific user from the ID that 
is stored in their session cookie. 
We can add this in our create_app function along with basic init code for Flask-Login.


Usermixin (get_id) -> @login_manager.user_loader 

UserMixin class that has default implementationsthat are appropriate for most cases.
Usermixin has 4 methods (get_id is 1)
get_id: returns the id.
By specifying user_loader, we can query who the current login user is within database.

"""