from flaskblog import app # app has to exist in __init__ method in flaskblog

if __name__ == '__main__':
    app.run(debug=True)

"""
Execution of this script calls flaskblog package which in turn calls the __init__.py into action. 
#run this script by nav to this folder layer in terminal. python run.py will start server

# to rebuild sql remain in this directory and call
>> from flaskblog import db
>> from flaskblog.models import User, Post
>> db.create_all()
>> User.query.all() # checks the db functionality should give empty list
"""

