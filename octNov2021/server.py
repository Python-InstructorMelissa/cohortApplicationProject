from flask import Flask, render_template, session, redirect, request
from classes.park import *
from env import KEY

parkApp = Flask(__name__)

parkApp.secret_key = KEY

@parkApp.route('/')
def index():
    return render_template('index.html', park=park)

@parkApp.route('/about')
def about():
    return render_template('about.html')

@parkApp.route('/addAbout', methods=['POST'])
def createAbout():
    session['name'] = request.form['name']
    session['description'] = request.form['description']
    return redirect('/about')











if __name__=="__main__":
    parkApp.run(debug=True)