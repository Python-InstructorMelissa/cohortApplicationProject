from flask import Flask, render_template
from classes.park import Park

parkApp = Flask(__name__)



@parkApp.route('/')
def index():
    return render_template('index.html')

@parkApp.route('/about')
def about():
    return render_template('about.html')











if __name__=="__main__":
    parkApp.run(debug=True)