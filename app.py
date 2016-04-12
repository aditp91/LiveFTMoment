# Python app using Flask for Web Development

from flask import Flask, render_template
from os import environ
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signInPage', methods=['GET', 'POST'])
def signInPage():
    #render_template('signin.html')
    return "reached signInPage method"
    
#@app.route('/aboutUs')
#def aboutUsPage():
#    return render_template('AboutUs.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
