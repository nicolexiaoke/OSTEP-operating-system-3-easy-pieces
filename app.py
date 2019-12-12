from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')  #render_template代表转到哪个页面

@app.route('/userlogin')
def getlogin():
    return("login")

if __name__ == '__main__':
    app.run()
