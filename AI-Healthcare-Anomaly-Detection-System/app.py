from flask import Flask, render_template, request, redirect, url_for, session
import random
import datetime
from anomaly_detector import detect_anomaly

app = Flask(__name__)
app.secret_key = "healthcare_secret"

history = []

USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/", methods=["GET"])
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    vitals = None
    result = None
    score = None

    if request.method == "POST":

        heart_rate = float(request.form["heart_rate"])
        spo2 = float(request.form["spo2"])
        temperature = float(request.form["temperature"])
        systolic = float(request.form["systolic"])
        diastolic = float(request.form["diastolic"])
        resp_rate = float(request.form["resp_rate"])

        vitals = [heart_rate, spo2, temperature, systolic, diastolic, resp_rate]

        result, score = detect_anomaly(vitals)

        record = {
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "heart_rate": heart_rate,
            "spo2": spo2,
            "temperature": temperature,
            "bp": f"{systolic}/{diastolic}",
            "resp_rate": resp_rate,
            "status": result
        }

        history.insert(0, record)

    return render_template(
        "dashboard.html",
        vitals=vitals,
        result=result,
        score=score,
        history=history[:10]
    )


app.run(host="0.0.0.0", port=5000)