# -- coding:utf-8 --
# @Time:2019/10/2 19:08
# @User:wuhaifeng
# @DESCIPTION:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'