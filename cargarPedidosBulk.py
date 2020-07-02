import pymongo
#from pymongo import MongoClient
import datetime

client = pymongo.MongoClient("mongodb+srv://acozzi:aw96b6@farmersmarket-tu1em.gcp.mongodb.net/farmersMarket?retryWrites=true&w=majority")
db = client['sg'] # <class 'pymongo.database.Database'>
pedidos = db.pedidos # <class 'pymongo.collection.Collection'>



pedidoSimple = {
    "cliente":"Vicky y Nico",
    "idPedido":1,
    "pedidos":[
        {"tipo":7,"cantidad":0.97},
        {"tipo":8,"cantidad":1.05}
    ]
    }



post_id = pedidos.insert(
    [
        {"cliente":"Daniel","idPedido":2,"pedidos":[{"tipo":6,"cantidad":0.93},{"tipo":13,"cantidad":0.42}]},
        {"cliente":"Claudia","idPedido":3,"pedidos":[{"tipo":6,"cantidad":0.94}]},
        {"cliente":"Horacio","idPedido":4,"pedidos":[{"tipo":8,"cantidad":1.03}]},
        {"cliente":"Tamy","idPedido":5,"pedidos":[{"tipo":5,"cantidad":1.057},{"tipo":8,"cantidad":1.042}]},
        {"cliente":"Majo","idPedido":6,"pedidos":[{"tipo":8,"cantidad":1.107},{"tipo":13,"cantidad":0.5},{"tipo":15,"cantidad":0.67}]},
        {"cliente":"Vicky","idPedido":7,"pedidos":[{"tipo":6,"cantidad":0.952}]},
        {"cliente":"Victor","idPedido":8,"pedidos":[{"tipo":7,"cantidad":0.937}]},
        {"cliente":"Silvina 14a","idPedido":9,"pedidos":[{"tipo":8,"cantidad":1.027}]},
        {"cliente":"Pupi","idPedido":10,"pedidos":[{"tipo":7,"cantidad":0.976}]},
        {"cliente":"Dario Balan","idPedido":11,"pedidos":[{"tipo":7,"cantidad":0.93},{"tipo":13,"cantidad":0.51},{"tipo":15,"cantidad":0.299}]},
        {"cliente":"Lau","idPedido":12,"pedidos":[{"tipo":6,"cantidad":0.954},{"tipo":15,"cantidad":0.687}]},
        {"cliente":"Romi y Ale","idPedido":13,"pedidos":[{"tipo":8,"cantidad":1},{"tipo":14,"cantidad":1.856}]},
        {"cliente":"Tota","idPedido":14,"pedidos":[{"tipo":13,"cantidad":0.594},{"tipo":15,"cantidad":0.617}]},
        {"cliente":"Fer","idPedido":15,"pedidos":[{"tipo":8,"cantidad":1.013}]},
        {"cliente":"Lorena","idPedido":16,"pedidos":[{"tipo":7,"cantidad":0.947}]},
        {"cliente":"Ric y Luli","idPedido":17,"pedidos":[{"tipo":13,"cantidad":0.522},{"tipo":15,"cantidad":0.633}]},
        {"cliente":"MARIAN","idPedido":18,"pedidos":[{"tipo":7,"cantidad":1}]},
        {"cliente":"Miriam Dujovne","idPedido":19,"pedidos":[{"tipo":7,"cantidad":0.943},{"tipo":8,"cantidad":1.098},{"tipo":13,"cantidad":0.485}]},
        {"cliente":"Monica Rabinovich","idPedido":20,"pedidos":[{"tipo":8,"cantidad":1.05},{"tipo":15,"cantidad":1.016}]},
        {"cliente":"Shei","idPedido":21,"pedidos":[{"tipo":11,"cantidad":0.375}]},
        {"cliente":"Alan karpovsky","idPedido":22,"pedidos":[{"tipo":5,"cantidad":1.055}]},
        {"cliente":"Claudia","idPedido":23,"pedidos":[{"tipo":6,"cantidad":0.941},{"tipo":7,"cantidad":0.956},{"tipo":8,"cantidad":1.076},{"tipo":13,"cantidad":0.85},{"tipo":14,"cantidad":0.58}]},
        {"cliente":"Felipe","idPedido":24,"pedidos":[{"tipo":12,"cantidad":0.55},{"tipo":13,"cantidad":0.56},{"tipo":14,"cantidad":0.655}]},
        {"cliente":"Alex","idPedido":25,"pedidos":[]},
        {"cliente":"Martin Villanova","idPedido":26,"pedidos":[{"tipo":5,"cantidad":1.003},{"tipo":11,"cantidad":0.57},{"tipo":12,"cantidad":0.46},{"tipo":13,"cantidad":0.487}]},
        {"cliente":"Daniel","idPedido":27,"pedidos":[{"tipo":11,"cantidad":0.34}]},
        {"cliente":"Telma","idPedido":28,"pedidos":[{"tipo":11,"cantidad":0.361}]},
        {"cliente":"Carolina 10A","idPedido":29,"pedidos":[{"tipo":8,"cantidad":1.054}]},
        {"cliente":"Sofi","idPedido":30,"pedidos":[{"tipo":7,"cantidad":0.93}]},
        {"cliente":"dany","idPedido":31,"pedidos":[{"tipo":7,"cantidad":0.948},{"tipo":8,"cantidad":1.02}]},
        {"cliente":"Meli y Manu","idPedido":32,"pedidos":[{"tipo":6,"cantidad":2.928},{"tipo":13,"cantidad":0.394}]},
        {"cliente":"Martin","idPedido":33,"pedidos":[{"tipo":5,"cantidad":6.107}]},
        {"cliente":"Monica","idPedido":34,"pedidos":[{"tipo":11,"cantidad":0.342},{"tipo":12,"cantidad":0.958},{"tipo":14,"cantidad":1.092}]},
        {"cliente":"Shei","idPedido":35,"pedidos":[{"tipo":6,"cantidad":0.952},{"tipo":15,"cantidad":0.329}]},
        {"cliente":"Ruchi","idPedido":36,"pedidos":[{"tipo":6,"cantidad":0.986}]},
        {"cliente":"Alan","idPedido":37,"pedidos":[{"tipo":6,"cantidad":1.972}]},
        {"cliente":"Daniel","idPedido":38,"pedidos":[{"tipo":9,"cantidad":0.747}]},
        {"cliente":"Mauro","idPedido":39,"pedidos":[{"tipo":5,"cantidad":1.034}]},
        {"cliente":"Nico y Vicky","idPedido":40,"pedidos":[{"tipo":8,"cantidad":1.048},{"tipo":9,"cantidad":0.409}]},
        {"cliente":"Caro shek","idPedido":41,"pedidos":[{"tipo":13,"cantidad":0.494}]},
        {"cliente":"Ar","idPedido":42,"pedidos":[{"tipo":5,"cantidad":1.006},{"tipo":11,"cantidad":0.272}]},
        {"cliente":"Mariano","idPedido":43,"pedidos":[{"tipo":8,"cantidad":1.035}]},
        {"cliente":"Amit","idPedido":44,"pedidos":[{"tipo":7,"cantidad":0.928},{"tipo":13,"cantidad":0.685},{"tipo":15,"cantidad":0.532}]},
        {"cliente":"Meli DG","idPedido":45,"pedidos":[{"tipo":12,"cantidad":0.525},{"tipo":14,"cantidad":0.564}]},
        {"cliente":"Ric y Luli","idPedido":46,"pedidos":[{"tipo":9,"cantidad":0.6},{"tipo":15,"cantidad":0.373}]},
        {"cliente":"Dany","idPedido":47,"pedidos":[{"tipo":7,"cantidad":0.948},{"tipo":8,"cantidad":1.02}]},
        {"cliente":"Monica","idPedido":48,"pedidos":[{"tipo":5,"cantidad":1},{"tipo":8,"cantidad":1.078},{"tipo":15,"cantidad":0.366}]},
        {"cliente":"Martin","idPedido":49,"pedidos":[{"tipo":5,"cantidad":0.973},{"tipo":9,"cantidad":0.519},{"tipo":12,"cantidad":0.89},{"tipo":15,"cantidad":0.358}]},
        {"cliente":"Mati y Flor","idPedido":50,"pedidos":[{"tipo":6,"cantidad":1.869},{"tipo":13,"cantidad":0.647}]},
        {"cliente":"Marcelo","idPedido":51,"pedidos":[{"tipo":13,"cantidad":0.611},{"tipo":15,"cantidad":0.31},{"tipo":16,"cantidad":1},{"tipo":17,"cantidad":1}]},
        {"cliente":"Luli Hambo","idPedido":52,"pedidos":[{"tipo":6,"cantidad":0.891},{"tipo":7,"cantidad":1.045}]},
        {"cliente":"Telma","idPedido":53,"pedidos":[{"tipo":15,"cantidad":0.34},{"tipo":17,"cantidad":1},{"tipo":18,"cantidad":1}]},
        {"cliente":"Daniel","idPedido":54,"pedidos":[{"tipo":5,"cantidad":1.044},{"tipo":10,"cantidad":0.67},{"tipo":17,"cantidad":1}]},
        {"cliente":"Miriam","idPedido":55,"pedidos":[{"tipo":7,"cantidad":0.89},{"tipo":8,"cantidad":0.983},{"tipo":13,"cantidad":0.58},{"tipo":17,"cantidad":1}]},
        {"cliente":"Vic Romano","idPedido":56,"pedidos":[{"tipo":7,"cantidad":0.921},{"tipo":18,"cantidad":1},{"tipo":20,"cantidad":1}]},
        {"cliente":"Cami Villa","idPedido":57,"pedidos":[{"tipo":5,"cantidad":1.109},{"tipo":16,"cantidad":1},{"tipo":18,"cantidad":1}]},
        {"cliente":"Danilo","idPedido":58,"pedidos":[{"tipo":5,"cantidad":1.052},{"tipo":6,"cantidad":0.963}]},
        {"cliente":"Ric y Luli","idPedido":59,"pedidos":[{"tipo":5,"cantidad":1.068},{"tipo":9,"cantidad":0.537},{"tipo":10,"cantidad":0.482},{"tipo":14,"cantidad":0.248},{"tipo":15,"cantidad":0.338},{"tipo":17,"cantidad":1},{"tipo":18,"cantidad":1}]},
        {"cliente":"Martin Villanova","idPedido":60,"pedidos":[{"tipo":12,"cantidad":0.5}]},
        {"cliente":"Monica Rabinovich","idPedido":61,"pedidos":[{"tipo":5,"cantidad":1},{"tipo":8,"cantidad":1},{"tipo":12,"cantidad":1},{"tipo":13,"cantidad":1},{"tipo":15,"cantidad":0.355}]},
        {"cliente":"Sebastia Linares","idPedido":62,"pedidos":[{"tipo":5,"cantidad":1.061},{"tipo":13,"cantidad":0.462}]},
        {"cliente":"Moni","idPedido":63,"pedidos":[{"tipo":5,"cantidad":1.053},{"tipo":8,"cantidad":0.99},{"tipo":12,"cantidad":0.958},{"tipo":13,"cantidad":1.139},{"tipo":15,"cantidad":0.343}]},
        {"cliente":"mati y flor","idPedido":64,"pedidos":[{"tipo":10,"cantidad":0.475},{"tipo":13,"cantidad":0.546},{"tipo":16,"cantidad":1}]},
        {"cliente":"pupi","idPedido":65,"pedidos":[{"tipo":7,"cantidad":0.971},{"tipo":8,"cantidad":1.109},{"tipo":15,"cantidad":0.348}]},
        {"cliente":"victor","idPedido":66,"pedidos":[{"tipo":8,"cantidad":1.018},{"tipo":9,"cantidad":0.605},{"tipo":10,"cantidad":0.47}]},
        {"cliente":"Jenny Lis","idPedido":67,"pedidos":[{"tipo":6,"cantidad":2.008},{"tipo":7,"cantidad":1.031},{"tipo":12,"cantidad":0.461},{"tipo":15,"cantidad":0.331}]},
        {"cliente":"Yae","idPedido":68,"pedidos":[{"tipo":7,"cantidad":0.974},{"tipo":10,"cantidad":0.548}]},
        {"cliente":"Meli y Manu","idPedido":69,"pedidos":[{"tipo":6,"cantidad":0.984},{"tipo":10,"cantidad":0.606},{"tipo":20,"cantidad":1}]},
        {"cliente":"David","idPedido":70,"pedidos":[{"tipo":9,"cantidad":0.63},{"tipo":12,"cantidad":0.487},{"tipo":13,"cantidad":0.5}]},
        {"cliente":"An","idPedido":71,"pedidos":[{"tipo":5,"cantidad":1.033},{"tipo":6,"cantidad":0.936}]},
        {"cliente":"Jesus","idPedido":72,"pedidos":[{"tipo":5,"cantidad":2.094},{"tipo":16,"cantidad":250}]},
        {"cliente":"Shei","idPedido":73,"pedidos":[{"tipo":15,"cantidad":0.71},{"tipo":17,"cantidad":250}]},
        {"cliente":"Tincho","idPedido":74,"pedidos":[{"tipo":10,"cantidad":0.6},{"tipo":14,"cantidad":0.563},{"tipo":18,"cantidad":350}]},
        {"cliente":"Feli","idPedido":75,"pedidos":[{"tipo":12,"cantidad":0.8},{"tipo":13,"cantidad":0.461},{"tipo":14,"cantidad":0.565},{"tipo":15,"cantidad":0.302}]},
        {"cliente":"Laura","idPedido":76,"pedidos":[{"tipo":7,"cantidad":0.942},{"tipo":13,"cantidad":0.525}]},
        {"cliente":"Vic Y Nico","idPedido":77,"pedidos":[]},
        {"cliente":"Monica","idPedido":78,"pedidos":[{"tipo":12,"cantidad":0.586},{"tipo":13,"cantidad":0.44},{"tipo":14,"cantidad":0.417}]},
        {"cliente":"Ruggieri 2944 23 torres señoria/ Agustin","idPedido":79,"pedidos":[{"tipo":13,"cantidad":0.457}]},
        {"cliente":"Sergio","idPedido":80,"pedidos":[]},
        {"cliente":"Cori","idPedido":81,"pedidos":[{"tipo":13,"cantidad":0.5}]},
        {"cliente":"lorena","idPedido":82,"pedidos":[{"tipo":14,"cantidad":0.464}]},
        {"cliente":"lau","idPedido":83,"pedidos":[{"tipo":14,"cantidad":0.375}]},
    ]

)

#pedidos.insert_one(pedidoSimple).inserted_id
print(post_id)
