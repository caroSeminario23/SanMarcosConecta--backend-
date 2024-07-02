from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.asistencia_est import Asistencia_est
from schemas.asistencia_est_schema import asistencia_est_schema, asistencias_est_schema

asistencia_est_routes = Blueprint("asistencia_est_routes", __name__)

@asistencia_est_routes.route('/create_asistencia_est', methods=['POST'])
def create_asistencia_est():
    id_seccion = request.json('id_seccion')
    id_estudiante = request.json('id_estudiante')
    fecha_marcado = request.json('fecha_marcado')

    new_asistencia_est = Asistencia_est(id_seccion, id_estudiante, fecha_marcado)
    
    db.session.add(new_asistencia_est)
    db.session.commit()
    
    result = asistencia_est_schema.dump(new_asistencia_est)
    
    data = {
        "message": "Asistencia_est creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@asistencia_est_routes.route('/get_asistencias_est', methods=['GET'])
def get_asistencias_est():
    all_asistencias_est = Asistencia_est.query.all()

    if not all_asistencias_est:
        data = {
            "message": "No se encontraron asistencias_est",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = asistencias_est_schema.dump(all_asistencias_est)

    data = {
        "message": "Todos los registros de asistencias_est han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@asistencia_est_routes.route('/get_asistencia_est/<int:id_asistencia_est>', methods=['GET'])
def get_asistencia_est(id_asistencia_est):
    asistencia_est = Asistencia_est.query.get(id_asistencia_est)

    if not asistencia_est:
        data = {
            "message": "No se encontró la asistencia_est",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = asistencia_est_schema.dump(asistencia_est)
    
    data = {
        "message": "Asistencia_est encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@asistencia_est_routes.route('/update_asistencia_est/<int:id_asistencia_est>', methods=['PUT'])
def update_asistencia_est(id_asistencia_est):
    asistencia_est = Asistencia_est.query.get(id_asistencia_est)

    if not asistencia_est:
        data = {
            "message": "No se encontró la asistencia_est",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    id_seccion = request.json('id_seccion')
    id_estudiante = request.json('id_estudiante')
    fecha_marcado = request.json('fecha_marcado')
    marcada = request.json('marcada')

    asistencia_est.id_seccion = id_seccion
    asistencia_est.id_estudiante = id_estudiante
    asistencia_est.fecha_marcado = fecha_marcado
    asistencia_est.marcada = marcada

    db.session.commit()

    result = asistencia_est_schema.dump(asistencia_est)

    data = {
        "message": "Asistencia_est actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@asistencia_est_routes.route('/delete_asistencia_est/<int:id_asistencia_est>', methods=['DELETE'])
def delete_asistencia_est(id_asistencia_est):
    asistencia_est = Asistencia_est.query.get(id_asistencia_est)

    if not asistencia_est:
        data = {
            "message": "No se encontró la asistencia_est",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(asistencia_est)
    db.session.commit()

    data = {
        "message": "Asistencia_est eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)