from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid or empty JSON body"}), 400
    message = data.get('message')
    if not isinstance(message, str):
        return jsonify({"error": "'message' must be a string"}), 400
    return jsonify({"length": len(message)})

if __name__ == "__main__":
    app.run(debug=True)

