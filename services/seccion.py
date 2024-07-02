from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Seccion import Seccion
from schemas.seccion_schema import seccion_schema, secciones_schema

seccion_routes = Blueprint("seccion_routes", __name__)

@seccion_routes.route('/create_seccion', methods=['POST'])
def create_seccion():
    id_curso = request.json('id_curso')
    id_aula = request.json('id_aula')
    id_docente = request.json('id_docente')
    id_dia = request.json('id_dia')
    hora_inicio = request.json('hora_inicio')
    hora_fin = request.json('hora_fin')

    new_seccion = Seccion(id_curso, id_aula, id_docente, id_dia, hora_inicio, hora_fin)

    db.session.add(new_seccion)
    db.session.commit()

    result = seccion_schema.dump(new_seccion)

    data = {
        "message": "Sección creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@seccion_routes.route('/get_secciones', methods=['GET'])
def get_secciones():
    all_secciones = Seccion.query.all()

    if not all_secciones:
        data = {
            "message": "No se encontraron secciones",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = secciones_schema.dump(all_secciones)

    data = {
        "message": "Todos los registros de secciones han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@seccion_routes.route('/get_seccion/<int:id_seccion>', methods=['GET'])
def get_seccion(id_seccion):
    seccion = Seccion.query.get(id_seccion)

    if not seccion:
        data = {
            "message": "No se encontró la sección",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = seccion_schema.dump(seccion)

    data = {
        "message": "Sección encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@seccion_routes.route('/update_seccion/<int:id_seccion>', methods=['PUT'])
def update_seccion(id_seccion):
    seccion = Seccion.query.get(id_seccion)

    if not seccion:
        data = {
            "message": "No se encontró la sección",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    seccion.id_curso = request.json('id_curso')
    seccion.id_aula = request.json('id_aula')
    seccion.id_docente = request.json('id_docente')
    seccion.id_dia = request.json('id_dia')
    seccion.hora_inicio = request.json('hora_inicio')
    seccion.hora_fin = request.json('hora_fin')

    db.session.commit()

    result = seccion_schema.dump(seccion)

    data = {
        "message": "Sección actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@seccion_routes.route('/delete_seccion/<int:id_seccion>', methods=['DELETE'])
def delete_seccion(id_seccion):
    seccion = Seccion.query.get(id_seccion)

    if not seccion:
        data = {
            "message": "No se encontró la sección",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(seccion)
    db.session.commit()

    data = {
        "message": "Sección eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)