from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or empty JSON body"}), 400
    message = data.get('message')
    if not isinstance(message, str):
        return jsonify({"error": "The 'message' field is required and must be a string"}), 400
    return jsonify({"length": len(message.encode('utf-8'))})

@app.route('/codepoint_length', methods=['POST'])
def codepoint_length():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or empty JSON body"}), 400
    message = data.get('message')
    if not isinstance(message, str):
        return jsonify({"error": "The 'message' field is required and must be a string"}), 400
    return jsonify({"codepoint_length": len(message)})

if __name__ == "__main__":
    app.run(debug=True)

