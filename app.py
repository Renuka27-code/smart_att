from flask import Flask, request, jsonify, render_template
import checkin_checkout
import report_generator
import visualize
from db import collection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    emp_id = data.get("emp_id")
    name = data.get("name")
    status, message = checkin_checkout.login(emp_id, name)
    return jsonify({"message": message, "success": status})

@app.route("/logout", methods=["POST"])
def logout():
    data = request.get_json()
    emp_id = data.get("emp_id")
    status, message = checkin_checkout.logout(emp_id)
    return jsonify({"message": message, "success": status})

@app.route("/status/<emp_id>", methods=["GET"])
def status(emp_id):
    active = checkin_checkout.get_status(emp_id)
    return jsonify({"emp_id": emp_id, "active": active})

@app.route("/attendance", methods=["GET"])
def get_attendance():
    records = list(collection.find({}, {"_id": 0}))
    return jsonify(records)

@app.route("/report", methods=["GET"])
def report():
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "Missing 'date' parameter"}), 400
    report_path = report_generator.generate_daily_report(date_str)
    if not report_path:
        return jsonify({"error": f"No records for {date_str}"}), 404
    return jsonify({"report_path": report_path})

@app.route("/visualize", methods=["GET"])
def visualize_attendance():
    date_str = request.args.get("date")
    if not date_str:
        return jsonify({"error": "Missing 'date' parameter"}), 400
    chart_path = visualize.visualize_productivity(date_str)
    if not chart_path:
        return jsonify({"error": f"No data for {date_str}"}), 404
    return jsonify({"chart_path": chart_path})

if __name__ == "__main__":
    app.run(debug=True)