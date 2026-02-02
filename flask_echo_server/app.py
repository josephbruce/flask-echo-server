from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text = data['text']
    if not isinstance(text, str):
        return jsonify({"error": "'text' must be a string"}), 400

    return jsonify({"length": len(text)})

if __name__ == "__main__":
    app.run(debug=True)

