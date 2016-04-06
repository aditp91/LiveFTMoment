# Python app using Flask for Web Development

from flask import Flask, render_template
#static_folder = '/static/images'
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signUpPage')
def signUpPage():
    return render_template('signup.html')
    
#@app.route('/aboutUs')
#def aboutUsPage():
#    return render_template('AboutUs.html')

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 5000), processes=2)
    