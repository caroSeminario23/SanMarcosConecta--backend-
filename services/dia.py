from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.dia import Dia
from schemas.dia_schema import dia_schema, dias_schema

dia_routes = Blueprint("dia_routes", __name__)

@dia_routes.route('/create_dia', methods=['POST'])
def create_dia():
    nombre = request.json('nombre')

    new_dia = Dia(nombre)

    db.session.add(new_dia)
    db.session.commit()

    result = dia_schema.dump(new_dia)

    data = {
        "message": "Dia creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@dia_routes.route('/get_dias', methods=['GET'])
def get_dias():
    all_dias = Dia.query.all()

    if not all_dias:
        data = {
            "message": "No se encontraron dias",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = dias_schema.dump(all_dias)

    data = {
        "message": "Todos los registros de dias han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@dia_routes.route('/get_dia/<int:id_dia>', methods=['GET'])
def get_dia(id_dia):
    dia = Dia.query.get(id_dia)

    if not dia:
        data = {
            "message": "No se encontró el dia",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = dia_schema.dump(dia)
    
    data = {
        "message": "Dia encontrado",
        "status": 200,
        "data": result
    }
    
    return make_response(jsonify(data), 200)

@dia_routes.route('/update_dia/<int:id_dia>', methods=['PUT'])
def update_dia(id_dia):
    dia = Dia.query.get(id_dia)

    if not dia:
        data = {
            "message": "No se encontró el dia",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json('nombre')

    dia.nombre = nombre

    db.session.commit()

    result = dia_schema.dump(dia)

    data = {
        "message": "Dia actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@dia_routes.route('/delete_dia/<int:id_dia>', methods=['DELETE'])
def delete_dia(id_dia):
    dia = Dia.query.get(id_dia)

    if not dia:
        data = {
            "message": "No se encontró el dia",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(dia)
    db.session.commit()

    data = {
        "message": "Dia eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)