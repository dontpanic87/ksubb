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
        title='Блог',
        year=datetime.now().year,
        message='Блог'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Контакты',
        year=datetime.now().year,
        message='Если Вы заинтересованы, обращайтесь:'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Резюме',
        year=datetime.now().year,
        message='Обо мне'
    )

if (__name__ =="__main__"):
    app.run(debug = True)