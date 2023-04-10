# Flask Introduction, Application, Open Link Flask, App Routing Flask Url Building Flask

from flask import Flask  # import Flask 
from flask import request   # it is used input take form user

app = Flask(__name__)      # it is a object of Flask

@app.route("/")                        # it is for decorator
def hello_world():                     # it is my very basic function
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")             # define router to access this function
def hello_world1():                     # it is my very basic function
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world2")             # define router to access this function
def hello_world2():                     # it is my very basic function
    return "<h1>Hello, World!2</h1>"

@app.route("/test")    # define router to access this function
def test():            # this function is decorate by "/test" path
    a = 5 + 6
    return "this is my functhion to run app {}".format(a)

@app.route("/test2")     
def test2() :                          # this function is decorate by "/test2" path
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")    # to run this in local host

# 200 means successfully access
# 404 means page not found