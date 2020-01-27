# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:36:10 2020

@author: GL63
"""


import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/greet/<name>")
def greet(name):
    return "Hello, {}!".format(name)

if __name__ == '__main__':
    app.run()
    

