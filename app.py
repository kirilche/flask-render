import os
from flask import Flask
app = Flask(__name__)

default_name = os.environ.get('DEFAULT_USERNAME')

if not default_name:
    default_name = "Світ!"

@app.route('/')
def hello_world():
    return f'Привіт, {default_name}'
