from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/string_length', methods=['POST'])
def string_length():
    data = request.get_data()
    return jsonify({"length": len(data)})

if __name__ == "__main__":
    app.run(debug=True)

