from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
CORS(app)
