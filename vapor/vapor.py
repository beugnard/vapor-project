#!/usr/bin/python
# coding: utf-8
from flask import Flask
from flask import request

app = Flask(__name__)


def sumit(a, b):
    """
    sumit : Read "sum-it", add a and b, return result.

    @input a : integer
    @input b : integer
    @output : integer
    """
    return a + b


@app.route("/sumit")
def sumreq():
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        print(a, b, type(a), type(b))
        return str(sumit(a, b))


@app.route("/")
def nothing():
        return "There is nothing here"
