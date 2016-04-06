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


if __name__ == "__main__":
    app.run()
    