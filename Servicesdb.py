from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps, RELAXED_JSON_OPTIONS

MONGO_URI = 'mongodb://l_services'

client = MongoClient(MONGO_URI)

db_services = client['services']

collection = db_services ['service']


def getServices():
    
    return dumps(collection.find(), json_options=RELAXED_JSON_OPTIONS)

def getServiceById(idvalue):
    return dumps(collection.find_one({"Idcompany":idvalue}),json_options=RELAXED_JSON_OPTIONS)

def postService(newService):

    collection.insert_one({
        "Idcompany": newService["company_id"],
        "Service": newService["type_service"],
        "Name": newService["company_name"],
        "Location": newService["company_location"],
        "Prices": newService["prices_service"],
        "Shedule": newService["shedule_service"]

    })


def editService(upService):

        _a=upService["company_id"]
        _b=upService["type_service"]
        _c=upService["company_name"]
        _d=upService["company_location"]
        _e=upService["prices_service"]
        _f=upService["shedule_service"]

        collection.update_one({"Idcompany": _a}, {"$set":{"Service": _b, "Name":_c, "Location":_d, "Prices":_e, "Shedule":_f}})

  

def deleteServ(id_to_delete):
    collection.delete_one({"Idcompany":id_to_delete})
    return "Servicio eliminado satisfactoriamente"
