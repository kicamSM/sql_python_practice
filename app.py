import warnings
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# connecting to database the name of the database goes after ///

# Initialize db variable
app.app_context().push()
# note this line above stopped the error 
db = SQLAlchemy()
db.app = app
db.init_app(app)

app.config['SECRET_KEY'] = "iloverollerderby12"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

try:
    from flask_debugtoolbar import DebugToolbarExtension
    debug = DebugToolbarExtension(app)
except ImportError:
    warnings.warn('Debugging disabled. Install flask_debugtoolbar to enable')
    pass

@app.route('/')
def home_page():
    """display home page"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run()