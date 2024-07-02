from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Tipo_usuario import Tipo_usuario
from schemas.tipo_usuario_schema import tipo_usuario_schema, tipos_usuarios_schema

tipo_usuario_routes = Blueprint("tipo_usuario_routes", __name__)

@tipo_usuario_routes.route('/create_tipo_usuario', methods=['POST'])
def create_tipo_usuario():
    
    data = request.get_json()
    
    nombre = data.get("nombre")

    new_tipo_usuario = Tipo_usuario(nombre)

    db.session.add(new_tipo_usuario)
    db.session.commit()

    result = tipo_usuario_schema.dump(new_tipo_usuario)

    data = {
        "message": "Tipo de usuario creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@tipo_usuario_routes.route('/get_tipos_usuario', methods=['GET'])
def get_tipos_usuario():
    all_tipos_usuario = Tipo_usuario.query.all()

    if not all_tipos_usuario:
        data = {
            "message": "No se encontraron tipos de usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = tipos_usuarios_schema.dump(all_tipos_usuario)

    data = {
        "message": "Todos los registros de tipos de usuario han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_usuario_routes.route('/get_tipo_usuario/<int:id_tipo_usuario>', methods=['GET'])
def get_tipo_usuario(id_tipo_usuario):
    tipo_usuario = Tipo_usuario.query.get(id_tipo_usuario)

    if not tipo_usuario:
        data = {
            "message": "No se encontró el tipo de usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = tipo_usuario_schema.dump(tipo_usuario)

    data = {
        "message": "Tipo de usuario encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_usuario_routes.route('/update_tipo_usuario/<int:id_tipo_usuario>', methods=['PUT'])
def update_tipo_usuario(id_tipo_usuario):
    tipo_usuario = Tipo_usuario.query.get(id_tipo_usuario)

    if not tipo_usuario:
        data = {
            "message": "No se encontró el tipo de usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    data = request.get_json()

    tipo_usuario.nombre = data.get('nombre')

    db.session.commit()

    result = tipo_usuario_schema.dump(tipo_usuario)

    data = {
        "message": "Tipo de usuario actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@tipo_usuario_routes.route('/delete_tipo_usuario/<int:id_tipo_usuario>', methods=['DELETE'])
def delete_tipo_usuario(id_tipo_usuario):
    tipo_usuario = Tipo_usuario.query.get(id_tipo_usuario)

    if not tipo_usuario:
        data = {
            "message": "No se encontró el tipo de usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_usuario)
    db.session.commit()

    data = {
        "message": "Tipo de usuario eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)
