from flask import Flask, render_template, request, session, redirect
from data.data import movies
from env import KEY
import os
app = Flask(__name__)
# app.secret_key = os.environ['KEY']
app.secret_key = KEY

@app.route('/')
def index():
    return render_template('index.html', theMovies=movies)





if __name__=="__main__":
    app.run(debug=True)