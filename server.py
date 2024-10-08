from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/')
def homeRoute():
    return "welcome to medical shop"

@app.route('/medical_shop_home')
def home():
    return "welcome to medical shop"

if __name__=='__main__':
    app.run(host='localhost',port=5000)