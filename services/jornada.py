from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Jornada import Jornada
from schemas.jornada_schema import jornada_schema, jornadas_schema

jornada_routes = Blueprint("jornada_routes", __name__)

@jornada_routes.route('/create_jornada', methods=['POST'])
def create_jornada():
    
    data = request.get_json()
    
    id_administrativo = data.get('id_administrativo')
    id_dia = data.get('id_dia')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')

    new_jornada = Jornada(id_administrativo, id_dia, hora_inicio, hora_fin)

    db.session.add(new_jornada)
    db.session.commit()

    result = jornada_schema.dump(new_jornada)

    data = {
        "message": "Jornada creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@jornada_routes.route('/get_jornadas', methods=['GET'])
def get_jornadas():
    all_jornadas = Jornada.query.all()

    if not all_jornadas:
        data = {
            "message": "No se encontraron jornadas",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = jornadas_schema.dump(all_jornadas)

    data = {
        "message": "Todos los registros de jornadas han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@jornada_routes.route('/get_jornada/<int:id_jornada>', methods=['GET'])
def get_jornada(id_jornada):
    jornada = Jornada.query.get(id_jornada)

    if not jornada:
        data = {
            "message": "No se encontró la jornada",
            "status": 404
        }
        return make_response(jsonify(data), 404)
        
    result = jornada_schema.dump(jornada)

    data = {
        "message": "Jornada encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@jornada_routes.route('/update_jornada/<int:id_jornada>', methods=['PUT'])
def update_jornada(id_jornada):
    jornada = Jornada.query.get(id_jornada)

    if not jornada:
        data = {
            "message": "No se encontró la jornada",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    
    data = request.get_json()
        
    jornada.id_administrativo = data.get('id_administrativo')
    jornada.id_dia = data.get('id_dia')
    jornada.hora_inicio = data.get('hora_inicio')
    jornada.hora_fin = data.get('hora_fin')

    db.session.commit()

    result = jornada_schema.dump(jornada)

    data = {
        "message": "Jornada actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@jornada_routes.route('/delete_jornada/<int:id_jornada>', methods=['DELETE'])
def delete_jornada(id_jornada):
    jornada = Jornada.query.get(id_jornada)

    if not jornada:
        data = {
            "message": "No se encontró la jornada",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(jornada)
    db.session.commit()

    data = {
        "message": "Jornada eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)