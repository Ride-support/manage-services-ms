from flask import Flask, jsonify, request
from Servicesdb import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
#Services routes

@app.route('/')
def index():
    return jsonify({"Message":"to see registers go to /services"})

@app.route('/services', methods=['GET'])
def readServices():
    return getServices()

@app.route('/services/<int:id_company>')
def getService (id_company):
    return(getServiceById(id_company))



@app.route('/services', methods=['POST'])
def createService():
    postService(request.json)
    return jsonify({"Mensaje": "Servicio agregado"})


@app.route('/services', methods=['PUT'])
def updateService():
    editService(request.json)
    return jsonify({"Mensaje":"Servicio modificado"})
    

@app.route('/services/<int:id_company>',methods=['DELETE'])
def deleteService(id_company):
    return deleteServ(id_company)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)