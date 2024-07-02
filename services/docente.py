from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Docente import Docente
from schemas.docente_schema import docente_schema, docentes_schema

docente_routes = Blueprint("docente_routes", __name__)

@docente_routes.route('/create_docente', methods=['POST'])
def create_docente():
    id_persona = request.json('id_persona')

    new_docente = Docente(id_persona)

    db.session.add(new_docente)
    db.session.commit()

    result = docente_schema.dump(new_docente)

    data = {
        "message": "Docente creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@docente_routes.route('/get_docentes', methods=['GET'])
def get_docentes():
    all_docentes = Docente.query.all()

    if not all_docentes:
        data = {
            "message": "No se encontraron docentes",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = docentes_schema.dump(all_docentes)

    data = {
        "message": "Todos los registros de docentes han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@docente_routes.route('/get_docente/<int:id_docente>', methods=['GET'])
def get_docente(id_docente):
    docente = Docente.query.get(id_docente)

    if not docente:
        data = {
            "message": "No se encontró el docente",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = docente_schema.dump(docente)

    data = {
        "message": "Docente encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@docente_routes.route('/update_docente/<int:id_docente>', methods=['PUT'])
def update_docente(id_docente):
    docente = Docente.query.get(id_docente)

    if not docente:
        data = {
            "message": "No se encontró el docente",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    id_persona = request.json('id_persona')
    activo = request.json('activo')

    docente.id_persona = id_persona
    docente.activo = activo

    db.session.commit()

    result = docente_schema.dump(docente)

    data = {
        "message": "Docente actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@docente_routes.route('/delete_docente/<int:id_docente>', methods=['DELETE'])
def delete_docente(id_docente):
    docente = Docente.query.get(id_docente)

    if not docente:
        data = {
            "message": "No se encontró el docente",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(docente)
    db.session.commit()

    data = {
        "message": "Docente eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)



