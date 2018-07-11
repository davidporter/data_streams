from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<int:ntimes>')
