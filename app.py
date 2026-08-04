```python
from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        password = request.form["password"]

        otp = str(random.randint(1000, 9999))

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(name,email,mobile,password,otp) VALUES(?,?,?,?,?)",
            (name, email, mobile, password, otp)
        )

        conn.commit()
        conn.close()

        return "OTP Sent Successfully: " + otp

    return render_template("register.html")


@app.route("/login")
def login():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect("/otp")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/otp", methods=["GET", "POST"])
def otp():

    if request.method == "POST":

        entered_otp = request.form["otp"]

        if entered_otp:
            return redirect("/vote")

        else:
            return "Invalid OTP"

    return render_template("otp.html")


@app.route("/vote")
def vote():
    return render_template("vote.html")


if __name__ == "__main__":
    app.run(debug=True)
```
