"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/home')

def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact me',
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year
    )

if (__name__ =="__main__"):
    app.run(debug = True)