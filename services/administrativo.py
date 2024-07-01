from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.administrativo import Administrativo
from schemas.administrativo_schema import administrativo_schema, administrativos_schema

administrativo_routes = Blueprint("administrativo_routes", __name__)

@administrativo_routes.route('/create_administrativo', methods=['POST'])
def create_administrativo():
    id_persona = request.json('id_persona')
    id_cargo = request.json('id_cargo')

    new_administrativo = Administrativo(id_persona, id_cargo)

    db.session.add(new_administrativo)
    db.session.commit()

    result = administrativo_schema.dump(new_administrativo)

    data = {
        "message": "Administrativo creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@administrativo_routes.route('/get_administrativos', methods=['GET'])
def get_administrativos():
    all_administrativos = Administrativo.query.all()

    if not all_administrativos:
        data = {
            "message": "No se encontraron administrativos",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = administrativos_schema.dump(all_administrativos)

    data = {
        "message": "Todos los registros de administrativos han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@administrativo_routes.route('/get_administrativo/<int:id_administrativo>', methods=['GET'])
def get_administrativo(id_administrativo):
    administrativo = Administrativo.query.get(id_administrativo)

    if not administrativo:
        data = {
            "message": "No se encontró el administrativo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = administrativo_schema.dump(administrativo)

    data = {
        "message": "Administrativo encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@administrativo_routes.route('/update_administrativo/<int:id_administrativo>', methods=['PUT'])
def update_administrativo(id_administrativo):
    administrativo = Administrativo.query.get(id_administrativo)

    if not administrativo:
        data = {
            "message": "No se encontró el administrativo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    id_persona = request.json('id_persona')
    id_cargo = request.json('id_cargo')

    administrativo.id_persona = id_persona
    administrativo.id_cargo = id_cargo
    administrativo.activo = request.json('activo')

    db.session.commit()

    result = administrativo_schema.dump(administrativo)

    data = {
        "message": "Administrativo actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@administrativo_routes.route('/delete_administrativo/<int:id_administrativo>', methods=['DELETE'])
def delete_administrativo(id_administrativo):
    administrativo = Administrativo.query.get(id_administrativo)

    if not administrativo:
        data = {
            "message": "No se encontró el administrativo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(administrativo)
    db.session.commit()

    data = {
        "message": "Administrativo eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)