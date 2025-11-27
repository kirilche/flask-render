import os
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

default_name = os.environ.get('DEFAULT_USERNAME')

if not default_name:
    default_name = "Світ!"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Привіт {name}\n Вітання {default_name}' 

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
