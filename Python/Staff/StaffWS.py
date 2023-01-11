from flask import Flask, jsonify, abort
from staffDAO import staffDAO

app = Flask(__name__, static_url_path='', static_folder='FrontEnd')

@app.route('/Staff', methods=['GET'])
def getAllStaff():
    allStaff = staffDAO.getAllStaff()
    return jsonify(allStaff)

