#!/usr/bin/python
from flask import Flask, jsonify, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/price")
def price():
    data = request.args
    widgets = data.get('widgets', "")
    if not widgets:
        widgets = 0
    widgets = int(widgets)
    birthdate = data.get('birthdate')

    cost = widgets * 5000 # Cents

    if birthdate:
        birthdate = date(*map(int, birthdate.split("-")))
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age <= 5:
            cost *= 0.5

    return jsonify(cost)

@app.route("/register", methods=["POST"])
def register():
    return app.send_static_file("registered.html")

if __name__ == "__main__":
    app.run(debug=True)