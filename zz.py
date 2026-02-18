from flask import Flask, request, jsonify
import os
import subprocess
import psutil

app = Flask(__name__)

# Faqat ruxsat berilgan buyruqlar
ALLOWED_COMMANDS = ["ls", "whoami", "uptime", "df -h", "free -m"]

@app.route("/run", methods=["POST"])
def run_command():
    """Ruxsat berilgan buyruqni bajarish"""
    data = request.json
    command = data.get("command")

    if command not in ALLOWED_COMMANDS:
        return jsonify({"error": "Ushbu buyruq ruxsat etilmagan!"}), 403

    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return jsonify({"command": command, "output": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/system", methods=["GET"])
def system_info():
    """Tizim ma'lumotlarini olish"""
    info = {
        "cpu_usage": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
