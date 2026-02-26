from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

def get_text_from_request():
    data = request.get_json()
    if not isinstance(data, dict):
        return None, (jsonify({"error": "Invalid JSON payload, expected an object"}), 400)

    text = data.get('text', '')
    if not isinstance(text, str):
        return None, (jsonify({"error": "'text' field must be a string"}), 400)

    return text, None

@app.route('/strlen', methods=['POST'])
def strlen():
    text, error_response = get_text_from_request()
    if error_response:
        return error_response
    return jsonify({"length": len(text)})

@app.route('/codepoints', methods=['POST'])
def codepoints():
    text, error_response = get_text_from_request()
    if error_response:
        return error_response
    return jsonify({"codepoints": len(text)})

@app.route('/bytes', methods=['POST'])
def bytes_count():
    text, error_response = get_text_from_request()
    if error_response:
        return error_response
    return jsonify({"bytes": len(text.encode('utf-8'))})

if __name__ == "__main__":
    app.run(debug=True)

