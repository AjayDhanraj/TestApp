from flask import Flask,request,jsonify,render_template
from App import app

@app.route('/')
def home():
    if request.method == "GET":
        return render_template("home.html")

    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            msg = {"Username": username}
            return jsonify(msg)
        else:
            msg = {"Login": "Failed"}
            return jsonify(msg)