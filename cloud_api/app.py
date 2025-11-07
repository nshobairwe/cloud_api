from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
ping_results = {}  # stores incoming results from clients

@app.route("/")
def dashboard_web():
    return render_template("dashboard.html", results=ping_results)

@app.route("/api/ping", methods=["POST"])
def receive_ping():
    global ping_results
    ping_results = request.get_json()   # update stored results
    return jsonify({"message": "received"}), 200

@app.route("/dashboard", methods=["GET"])
def dashboard_json():
    return jsonify(ping_results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
