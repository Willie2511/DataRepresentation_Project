from flask import Flask, jsonify, abort
from staffDAO import staffDAO

app = Flask(__name__, static_url_path='', static_folder='DataRepresentation_Project/FrontEnd')

@app.route('/Staff', methods=['GET'])
def getAllStaff():
    allStaff = staffDAO.getAllStaff()
    return jsonify(allStaff)

@app.route('/Staff/Id', methods=['GET'])
def getStaffById(Id):
    staffById = staffDAO.getStaffById(Id)
    return jsonify(staffById)

@app.route('/Staff/search/<email>', methods=['GET'])
def getStaffByEmail(email):
    staffByEmail = staffDAO.getStaffByEmailAddress(email)
    return jsonify(staffByEmail)
