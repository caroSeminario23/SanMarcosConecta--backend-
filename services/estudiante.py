from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Estudiante import Estudiante
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema

estudiante_routes = Blueprint("estudiante_routes", __name__)

@estudiante_routes.route('/create_estudiante', methods=['POST'])
def create_estudiante():
    
    data = request.get_json()
    
    id_persona = data.get('id_persona')
    n_ciclo = data.get('n_ciclo')
    egresado = data.get('egresado')

    new_estudiante = Estudiante(id_persona, n_ciclo, egresado)

    db.session.add(new_estudiante)
    db.session.commit()

    result = estudiante_schema.dump(new_estudiante)

    data = {
        "message": "Estudiante creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@estudiante_routes.route('/get_estudiantes', methods=['GET'])
def get_estudiantes():
    all_estudiantes = Estudiante.query.all()

    if not all_estudiantes:
        data = {
            "message": "No se encontraron estudiantes",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = estudiantes_schema.dump(all_estudiantes)

    data = {
        "message": "Todos los registros de estudiantes han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@estudiante_routes.route('/get_estudiante/<int:id_estudiante>', methods=['GET'])
def get_estudiante(id_estudiante):
    estudiante = Estudiante.query.get(id_estudiante)

    if not estudiante:
        data = {
            "message": "No se encontró el estudiante",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = estudiante_schema.dump(estudiante)

    data = {
        "message": "El registro de estudiante ha sido encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@estudiante_routes.route('/update_estudiante/<int:id_estudiante>', methods=['PUT'])
def update_estudiante(id_estudiante):
    estudiante = Estudiante.query.get(id_estudiante)

    if not estudiante:
        data = {
            "message": "No se encontró el estudiante",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    
    data = request.get_json()

    estudiante.id_persona = data.get('id_persona')
    estudiante.n_ciclo = data.get('n_ciclo')
    estudiante.egresado = data.get('egresado')

    db.session.commit()

    result = estudiante_schema.dump(estudiante)

    data = {
        "message": "Estudiante actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@estudiante_routes.route('/delete_estudiante/<int:id_estudiante>', methods=['DELETE'])
def delete_estudiante(id_estudiante):
    estudiante = Estudiante.query.get(id_estudiante)

    if not estudiante:
        data = {
            "message": "No se encontró el estudiante",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(estudiante)
    db.session.commit()

    data = {
        "message": "Estudiante eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)