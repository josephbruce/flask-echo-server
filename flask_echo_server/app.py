from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json(silent=True)
    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    text = data.get('text')
    if text is None:
        return jsonify({"error": "Missing 'text' key"}), 400

    if not isinstance(text, str):
        return jsonify({"error": "'text' must be a string"}), 400

    return jsonify({"length": len(text)})

if __name__ == "__main__":
    app.run(debug=True)

