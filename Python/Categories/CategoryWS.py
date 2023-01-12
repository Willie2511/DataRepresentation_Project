from flask import Flask, jsonify, abort
from CategoriesDAO import categoryDAO

app = Flask(__name__, static_url_path='', static_folder='DataRepresentation_Project/FrontEnd')

@app.route('/Categories', methods=['GET'])
def getAllCategories():
    allCategories = categoryDAO.getAllCategories()
    return jsonify(allCategories)

@app.route('/Categories/search/<id>', methods=['GET'])
def getCategoryById(id):
    category = categoryDAO.getCategoryById(id)
    return jsonify(category)