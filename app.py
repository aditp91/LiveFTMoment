# Python app using Flask for Web Development

from flask import Flask, render_template
from os import environ
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signInPage')
def signInPage():
    return render_template('signin.html')

@app.route('/signUpButton', methods=['GET', 'POST'])
def signUpButton():
    _email = request.form['email']
    _password = request.form['password']
    return "this is data"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    app.run(host='localhost', port=port)
