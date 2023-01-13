from flask import Flask, jsonify, abort
from customerDAO import customerDAO

app = Flask(__name__, static_url_path='', static_folder='DataRepresentation_Project/FrontEnd')

@app.route('/Customers', methods=['GET'])
def getAllCustomers():
    allCustomers = customerDAO.getAllCustomers()
    return jsonify(allCustomers)

@app.route('/Customers/<id>', methods=['GET'])
def getCustomerById(id):
    customer = customerDAO.getCustomerById(id)
    return jsonify(customer)

@app.route('/Customers/search/<email>', methods=['GET'])
def getCustomerByEmail(email):
    customerByEmail = customerDAO.getCustomerByEmailAddress(email)
    return jsonify(customerByEmail)

@app.route('/Customers', methods=['POST'])
def addNewCustomer(customer):
    customerDAO.addNewCustomer(customer)


if __name__ == "__main__":
    app.run(debug=True)