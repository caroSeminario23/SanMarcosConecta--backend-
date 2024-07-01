from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tipo_aula import TipoAula
from schemas.tipo_aula_schema import tipo_aula_schema, tipos_aula_schema

tipo_aula_routes = Blueprint("tipo_aula_routes", __name__)

@tipo_aula_routes.route('/create_tipo_aula', methods=['POST'])
def create_tipo_aula():
    nombre = request.json('nombre')

    new_tipo_aula = TipoAula(nombre)

    db.session.add(new_tipo_aula)
    db.session.commit()

    result = tipo_aula_schema.dump(new_tipo_aula)

    data = {
        "message": "Tipo de aula creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@tipo_aula_routes.route('/get_tipos_aula', methods=['GET'])
def get_tipos_aula():
    all_tipos_aula = TipoAula.query.all()

    if not all_tipos_aula:
        data = {
            "message": "No se encontraron tipos de aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = tipos_aula_schema.dump(all_tipos_aula)

    data = {
        "message": "Todos los registros de tipos de aula han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_aula_routes.route('/get_tipo_aula/<int:id_tipo_aula>', methods=['GET'])
def get_tipo_aula(id_tipo_aula):
    tipo_aula = TipoAula.query.get(id_tipo_aula)

    if not tipo_aula:
        data = {
            "message": "No se encontró el tipo de aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = tipo_aula_schema.dump(tipo_aula)

    data = {
        "message": "Registro de tipo de aula encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_aula_routes.route('/update_tipo_aula/<int:id_tipo_aula>', methods=['PUT'])
def update_tipo_aula(id_tipo_aula):
    tipo_aula = TipoAula.query.get(id_tipo_aula)

    if not tipo_aula:
        data = {
            "message": "No se encontró el tipo de aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    tipo_aula.nombre = request.json('nombre')

    db.session.commit()

    result = tipo_aula_schema.dump(tipo_aula)

    data = {
        "message": "Tipo de aula actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_aula_routes.route('/delete_tipo_aula/<int:id_tipo_aula>', methods=['DELETE'])
def delete_tipo_aula(id_tipo_aula):
    tipo_aula = TipoAula.query.get(id_tipo_aula)

    if not tipo_aula:
        data = {
            "message": "No se encontró el tipo de aula",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_aula)
    db.session.commit()

    result = tipo_aula_schema.dump(tipo_aula)

    data = {
        "message": "Tipo de aula eliminado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)