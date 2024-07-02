from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Asistencia_admin import Asistencia_admin
from schemas.asistencia_admin_schema import asistencia_admin_schema, asistencias_admin_schema

asistencia_admin_routes = Blueprint("asistencia_admin_routes", __name__)

@asistencia_admin_routes.route('/create_asistencia_admin', methods=['POST'])
def create_asistencia_admin():
    data = request.get_json()
    id_jornada = data.get('id_jornada')
    fecha_marcado = data.get('fecha_marcado')

    new_asistencia_admin = Asistencia_admin(id_jornada, fecha_marcado)
    
    db.session.add(new_asistencia_admin)
    db.session.commit()
    
    result = asistencia_admin_schema.dump(new_asistencia_admin)
    
    data = {
        "message": "Asistencia_admin creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@asistencia_admin_routes.route('/get_asistencias_admin', methods=['GET'])
def get_asistencias_admin():
    all_asistencias_admin = Asistencia_admin.query.all()
    
    if not all_asistencias_admin:
        data = {
            "message": "No se encontraron asistencias_admin",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = asistencias_admin_schema.dump(all_asistencias_admin)
    
    data = {
        "message": "Todos los registros de asistencias_admin han sido encontrados",
        "status": 200,
        "data": result
    }
    
    return make_response(jsonify(data), 200)

@asistencia_admin_routes.route('/get_asistencia_admin/<int:id_asistencia_admin>', methods=['GET'])
def get_asistencia_admin(id_asistencia_admin):
    asistencia_admin = Asistencia_admin.query.get(id_asistencia_admin)
    
    if not asistencia_admin:
        data = {
            "message": "No se encontró la asistencia_admin",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = asistencia_admin_schema.dump(asistencia_admin)
    
    data = {
        "message": "El registro de asistencia_admin ha sido encontrado",
        "status": 200,
        "data": result
    }
    
    return make_response(jsonify(data), 200)

@asistencia_admin_routes.route('/update_asistencia_admin/<int:id_asistencia_admin>', methods=['PUT'])
def update_asistencia_admin(id_asistencia_admin):
    asistencia_admin = Asistencia_admin.query.get(id_asistencia_admin)
    
    if not asistencia_admin:
        data = {
            "message": "No se encontró la asistencia_admin",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    data = request.get_json()
    
    id_jornada = data.get('id_jornada')
    fecha_marcado = data.get('fecha_marcado')
    marcada = data.get('marcada')
    
    asistencia_admin.id_jornada = id_jornada
    asistencia_admin.fecha_marcado = fecha_marcado
    asistencia_admin.marcada = marcada
    
    db.session.commit()
    
    result = asistencia_admin_schema.dump(asistencia_admin)
    
    data = {
        "message": "Asistencia_admin actualizada correctamente",
        "status": 200,
        "data": result
    }
    
    return make_response(jsonify(data), 200)
@asistencia_admin_routes.route('/delete_asistencia_admin/<int:id_asistencia_admin>', methods=['DELETE'])
def delete_asistencia_admin(id_asistencia_admin):
    asistencia_admin = Asistencia_admin.query.get(id_asistencia_admin)
    
    if not asistencia_admin:
        data = {
            "message": "No se encontró la asistencia_admin",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(asistencia_admin)
    db.session.commit()
    
    data = {
        "message": "Asistencia_admin eliminada correctamente",
        "status": 200
    }
    
    return make_response(jsonify(data), 200)

