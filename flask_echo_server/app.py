from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json(silent=True)
    if data is None or 'message' not in data:
        return jsonify({"error": "Invalid JSON or missing 'message' key"}), 400
    message = data['message']
    return jsonify({"length": len(message.encode('utf-8'))})

if __name__ == "__main__":
    app.run(debug=True)

