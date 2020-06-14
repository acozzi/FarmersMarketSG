import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://acozzi:aw96b6@farmersmarket-tu1em.gcp.mongodb.net/farmersMarket?retryWrites=true&w=majority')






cliente = {
    "timestamp": datetime.datetime.utcnow(),
    "nombre": "Ale Cozzi",
    "direccion": {
        "calle": "Cullen",
        "altura": 4941,
        "pisoDepto": "12 B",
        "cp": 1431,
        "localidad": "CABA",
        "zona": 0
    },
    "telefono":"247815448449",
    "mail":"acozzzi@gmail.com",
    "facebook":"acozzzi",
    "instagram":"acozzzi"
}
print(cliente["timestamp"])
db = client['sg'] # <class 'pymongo.database.Database'>
clientes = db.clientes # <class 'pymongo.collection.Collection'>

post_id = clientes.insert_one()

"""
cliente = {
    "nombre": "",
    "direccion": {
        "calle": "",
        "altura": 0,
        "pisoDepto": "",
        "cp": 0,
        "localidad": "",
        "zona": 0
    },
    "telefono":"",
    "mail":"",
    "facebook":"",
    "instagram":""
}
"""


"""
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://acozzi:<password>@farmersmarket-tu1em.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });



client.connect(err => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});
"""