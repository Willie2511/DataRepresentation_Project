from flask import Flask, jsonify, abort
from staffDAO import staffDAO

app = Flask(__name__, static_url_path='', static_folder='DataRepresentation_Project/FrontEnd')

@app.route('/Staff', methods=['GET'])
def getAllStaff():
    allStaff = staffDAO.getAllStaff()
    return jsonify(allStaff)

@app.route('/Staff/search/<id>', methods=['GET'])
def getStaffById(id):
    staffById = staffDAO.getStaffById(id)
    return jsonify(staffById)
