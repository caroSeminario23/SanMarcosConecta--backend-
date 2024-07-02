from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.aula import Aula
from schemas.aula_schema import aula_schema, aulas_schema

aula_routes = Blueprint("aula_routes", __name__)

@aula_routes.route('/create_aula', methods=['POST'])
def create_aula():
    nombre = request.json('nombre')
    id_pabellon = request.json('id_pabellon')
    n_piso = request.json('n_piso')
    id_tipo_aula = request.json('id_tipo_aula')
    coordenadas = request.json('coordenadas')
    capacidad = request.json('capacidad')

    new_aula = Aula(nombre, id_pabellon, n_piso, id_tipo_aula, coordenadas, capacidad)

    db.session.add(new_aula)
    db.session.commit()

    result = aula_schema.dump(new_aula)

    data = {
        "message": "Aula creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@aula_routes.route('/get_aulas', methods=['GET'])
def get_aulas():
    all_aulas = Aula.query.all()

    if not all_aulas:
        data = {
            "message": "No se encontraron aulas",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = aulas_schema.dump(all_aulas)

    data = {
        "message": "Todos los registros de aulas han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@aula_routes.route('/get_aula/<int:id_aula>', methods=['GET'])
def get_aula(id_aula):
    aula = Aula.query.get(id_aula)

    if not aula:
        data = {
            "message": "No se encontró el aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = aula_schema.dump(aula)

    data = {
        "message": "Aula encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@aula_routes.route('/update_aula/<int:id_aula>', methods=['PUT'])
def update_aula(id_aula):
    aula = Aula.query.get(id_aula)

    if not aula:
        data = {
            "message": "No se encontró el aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json('nombre')
    id_pabellon = request.json('id_pabellon')
    n_piso = request.json('n_piso')
    id_tipo_aula = request.json('id_tipo_aula')
    coordenadas = request.json('coordenadas')
    capacidad = request.json('capacidad')
    aforo_actual = request.json('aforo_actual')

    aula.nombre = nombre
    aula.id_pabellon = id_pabellon
    aula.n_piso = n_piso
    aula.id_tipo_aula = id_tipo_aula
    aula.coordenadas = coordenadas
    aula.capacidad = capacidad
    aula.aforo_actual = aforo_actual

    db.session.commit()

    result = aula_schema.dump(aula)

    data = {
        "message": "Aula actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@aula_routes.route('/delete_aula/<int:id_aula>', methods=['DELETE'])
def delete_aula(id_aula):
    aula = Aula.query.get(id_aula)

    if not aula:
        data = {
            "message": "No se encontró el aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(aula)
    db.session.commit()

    data = {
        "message": "Aula eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)