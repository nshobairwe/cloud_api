from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
ping_results = {}

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/api/ping", methods=["POST"])
def receive_ping():
    data = request.get_json()
    print(data)
    return jsonify({"message": "received"}), 200


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify(ping_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
