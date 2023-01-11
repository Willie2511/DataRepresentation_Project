from flask import Flask, jsonify, abort

app = Flask(__name__, static_url_path='', static_folder='static')

bands = [
    {'name': 'band1'},
    {'name': 'band2'}
]


@app.route('/band', methods=['GET'])
def getAllBands():
    return jsonify(bands)


if __name__ == "__main__":
    app.run(debug=True)
