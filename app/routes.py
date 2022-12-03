from app import app
from flask import render_template

@app.route('/')
def home():
    students = ['jules', 'fifi', 'ruby', 'brownie']
    return render_template('index.html', names=students)


