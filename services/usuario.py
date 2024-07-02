from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Usuario import Usuario
from schemas.usuario_schema import usuario_schema, usuarios_schema

usuario_routes = Blueprint("usuario_routes", __name__)

@usuario_routes.route('/create_usuario', methods=['POST'])
def create_usuario():
    
    data = request.get_json()
    
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    id_tipo_usuario = data.get('id_tipo_usuario')

    new_usuario = Usuario(email, contrasenia, id_tipo_usuario)

    db.session.add(new_usuario)
    db.session.commit()

    result = usuario_schema.dump(new_usuario)

    data = {
        "message": "Usuario creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@usuario_routes.route('/get_usuarios', methods=['GET'])
def get_usuarios():
    all_usuarios = Usuario.query.all()

    if not all_usuarios:
        data = {
            "message": "No se encontraron usuarios",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = usuarios_schema.dump(all_usuarios)

    data = {
        "message": "Todos los registros de usuarios han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@usuario_routes.route('/get_usuario/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)

    if not usuario:
        data = {
            "message": "No se encontró el usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = usuario_schema.dump(usuario)

    data = {
        "message": "Usuario encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@usuario_routes.route('/update_usuario/<int:id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)

    if not usuario:
        data = {
            "message": "No se encontró el usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    data = request.get_json()

    usuario.email = data.get('email')
    usuario.contrasenia = data.get('contrasenia')
    usuario.id_tipo_usuario = data.get('id_tipo_usuario')

    db.session.commit()

    result = usuario_schema.dump(usuario)

    data = {
        "message": "Usuario actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@usuario_routes.route('/delete_usuario/<int:id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)

    if not usuario:
        data = {
            "message": "No se encontró el usuario",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(usuario)
    db.session.commit()

    data = {
        "message": "Usuario eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)
