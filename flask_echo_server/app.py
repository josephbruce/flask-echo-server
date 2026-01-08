from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/madlibs', methods=['GET'])
def madlibs():
    place = request.args.get('place')
    verb = request.args.get('verb')
    if not place or not verb:
        return jsonify({"error": "Both 'place' and 'verb' query parameters are required."}), 400
    sentence = f"I went to the {place} so I could {verb}"
    return jsonify({"sentence": sentence})

if __name__ == "__main__":
    app.run(debug=True)

