from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Asistencia_doc import Asistencia_doc
from schemas.asistencia_doc_schema import asistencia_doc_schema, asistencias_doc_schema

asistencia_doc_routes = Blueprint("Asistencia_doc_routes", __name__)

@asistencia_doc_routes.route('/create_asistencia_doc', methods=['POST'])
def create_asistencia_doc():
    id_seccion = request.json('id_seccion')
    fecha_marcado = request.json('fecha_marcado')

    new_asistencia_doc = Asistencia_doc(id_seccion, fecha_marcado)
    
    db.session.add(new_asistencia_doc)
    db.session.commit()
    
    result = asistencia_doc_schema.dump(new_asistencia_doc)
    
    data = {
        "message": "Asistencia_doc creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
@asistencia_doc_routes.route('/get_asistencias_doc', methods=['GET'])
def get_asistencias_doc():
    all_asistencias_doc = Asistencia_doc.query.all()
    
    if not all_asistencias_doc:
        data = {
            "message": "No se encontraron asistencias_doc",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = asistencias_doc_schema.dump(all_asistencias_doc)
    
    data = {
        "message": "Todos los registros de asistencias_doc han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@asistencia_doc_routes.route('/get_asistencia_doc/<int:id_asistencia_doc>', methods=['GET'])
def get_asistencia_doc(id_asistencia_doc):
    asistencia_doc = Asistencia_doc.query.get(id_asistencia_doc)
    
    if not asistencia_doc:
        data = {
            "message": "No se encontró la asistencia_doc",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = asistencia_doc_schema.dump(asistencia_doc)
    
    data = {
        "message": "El registro de asistencia_doc ha sido encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)


@asistencia_doc_routes.route('/update_asistencia_doc/<int:id_asistencia_doc>', methods=['PUT'])
def update_asistencia_doc(id_asistencia_doc):
    asistencia_doc = Asistencia_doc.query.get(id_asistencia_doc)
    
    if not asistencia_doc:
        data = {
            "message": "No se encontró la asistencia_doc",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    id_seccion = request.json('id_seccion')
    fecha_marcado = request.json('fecha_marcado')
    marcada = request.json('marcada')

    asistencia_doc.id_seccion = id_seccion
    asistencia_doc.fecha_marcado = fecha_marcado
    asistencia_doc.marcada = marcada
    
    db.session.commit()
    
    result = asistencia_doc_schema.dump(asistencia_doc)
    
    data = {
        "message": "Asistencia_doc actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@asistencia_doc_routes.route('/delete_asistencia_doc/<int:id_asistencia_doc>', methods=['DELETE'])
def delete_asistencia_doc(id_asistencia_doc):
    asistencia_doc = Asistencia_doc.query.get(id_asistencia_doc)
        
    if not asistencia_doc:
        data = {
            "message": "No se encontró la asistencia_doc",
            "status": 404
        }
        return make_response(jsonify(data), 404)
        
    db.session.delete(asistencia_doc)
    db.session.commit()
        
    data = {
        "message": "Asistencia_doc eliminada correctamente",
        "status": 200
    }
        
    return make_response(jsonify(data), 200)


