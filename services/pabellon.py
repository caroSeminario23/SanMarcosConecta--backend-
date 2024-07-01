from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.pabellon import Pabellon
from schemas.pabellon_schema import pabellon_schema, pabellones_schema

pabellon_routes = Blueprint("pabellon_routes", __name__)

@pabellon_routes.route('/create_pabellon', methods=['POST'])
def create_pabellon():
    nombre = request.json('nombre')

    new_pabellon = Pabellon(nombre)

    db.session.add(new_pabellon)
    db.session.commit()

    result = pabellon_schema.dump(new_pabellon)

    data = {
        "message": "Pabellon creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@pabellon_routes.route('/get_pabellones', methods=['GET'])
def get_pabellones():
    all_pabellones = Pabellon.query.all()

    if not all_pabellones:
        data = {
            "message": "No se encontraron pabellones",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = pabellones_schema.dump(all_pabellones)

    data = {
        "message": "Todos los registros de pabellones han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@pabellon_routes.route('/get_pabellon/<int:id_pabellon>', methods=['GET'])
def get_pabellon(id_pabellon):
    pabellon = Pabellon.query.get(id_pabellon)

    if not pabellon:
        data = {
            "message": "No se encontró el pabellon",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = pabellon_schema.dump(pabellon)

    data = {
        "message": "El registro de pabellon ha sido encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@pabellon_routes.route('/update_pabellon/<int:id_pabellon>', methods=['PUT'])
def update_pabellon(id_pabellon):
    pabellon = Pabellon.query.get(id_pabellon)

    if not pabellon:
        data = {
            "message": "No se encontró el pabellon",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    pabellon.nombre = request.json('nombre')

    db.session.commit()

    result = pabellon_schema.dump(pabellon)

    data = {
        "message": "Pabellon actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@pabellon_routes.route('/delete_pabellon/<int:id_pabellon>', methods=['DELETE'])
def delete_pabellon(id_pabellon):
    pabellon = Pabellon.query.get(id_pabellon)

    if not pabellon:
        data = {
            "message": "No se encontró el pabellon",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(pabellon)
    db.session.commit()

    data = {
        "message": "Pabellon eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)