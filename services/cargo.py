from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.cargo import Cargo
from schemas.cargo_schema import cargo_schema, cargos_schema

cargo_routes = Blueprint("cargo_routes", __name__)

@cargo_routes.route('/create_cargo', methods=['POST'])
def create_cargo():
    nombre = request.json('nombre')

    new_cargo = Cargo(nombre)

    db.session.add(new_cargo)
    db.session.commit()

    result = cargo_schema.dump(new_cargo)

    data = {
        "message": "Cargo creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@cargo_routes.route('/get_cargos', methods=['GET'])
def get_cargos():
    all_cargos = Cargo.query.all()

    if not all_cargos:
        data = {
            "message": "No se encontraron cargos",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = cargos_schema.dump(all_cargos)

    data = {
        "message": "Todos los registros de cargos han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@cargo_routes.route('/get_cargo/<int:id_cargo>', methods=['GET'])
def get_cargo(id_cargo):
    cargo = Cargo.query.get(id_cargo)

    if not cargo:
        data = {
            "message": "No se encontró el cargo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = cargo_schema.dump(cargo)

    data = {
        "message": "Cargo encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@cargo_routes.route('/update_cargo/<int:id_cargo>', methods=['PUT'])
def update_cargo(id_cargo):
    cargo = Cargo.query.get(id_cargo)

    if not cargo:
        data = {
            "message": "No se encontró el cargo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json('nombre')

    cargo.nombre = nombre

    db.session.commit()

    result = cargo_schema.dump(cargo)

    data = {
        "message": "Cargo actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@cargo_routes.route('/delete_cargo/<int:id_cargo>', methods=['DELETE'])
def delete_cargo(id_cargo):
    cargo = Cargo.query.get(id_cargo)

    if not cargo:
        data = {
            "message": "No se encontró el cargo",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(cargo)
    db.session.commit()


    data = {
        "message": "Cargo eliminado correctamente",
        "status": 200,
    }

    return make_response(jsonify(data), 200)