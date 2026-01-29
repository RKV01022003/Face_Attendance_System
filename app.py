# app.py
from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

ATTENDANCE_FILE = "attendance.csv"

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    # Here you can integrate with train_model.py / dataset logic
    # For now, just log in CSV
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, "Registered"])
    return jsonify({"message": f"{name} registered successfully"})

@app.route("/attendance", methods=["POST"])
def attendance():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    # Here you can integrate with recognize_face.py
    # For now, just log in CSV
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, "Present"])
    return jsonify({"message": f"Attendance marked for {name}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
