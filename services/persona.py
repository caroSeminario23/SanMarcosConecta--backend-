from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.persona import Persona
from schemas.persona_schema import persona_schema, personas_schema

persona_routes = Blueprint("persona_routes", __name__)

@persona_routes.route('/create_persona', methods=['POST'])
def create_persona():
    id_usuario = request.json('id_usuario')
    cod_identificacion = request.json('cod_identificacion')
    doc_identificacion = request.json('doc_identificacion')
    nombres = request.json('nombres')
    apellidos = request.json('apellido')
    fec_nacimiento = request.json('fec_nacimiento')
    n_celular = request.json('n_celular')
    genero = request.json('genero')

    new_persona = Persona(id_usuario, cod_identificacion, doc_identificacion, nombres, apellidos, fec_nacimiento, n_celular, genero)

    db.session.add(new_persona)
    db.session.commit()

    result = persona_schema.dump(new_persona)

    data = {
        "message": "Persona creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)
  
@persona_routes.route('/get_personas', methods=['GET'])
def get_personas():
    all_personas = Persona.query.all()

    if not all_personas:
        data = {
            "message": "No se encontraron personas",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = personas_schema.dump(all_personas)

    data = {
        "message": "Todos los registros de personas han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@persona_routes.route('/get_persona/<int:id_persona>', methods=['GET'])
def get_persona(id_persona):
    persona = Persona.query.get(id_persona)

    if not persona:
        data = {
            "message": "No se encontró la persona",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    result = persona_schema.dump(persona)

    data = {
        "message": "Persona encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@persona_routes.route('/update_persona/<int:id_persona>', methods=['PUT'])
def update_persona(id_persona):
    persona = Persona.query.get(id_persona)

    if not persona:
        data = {
            "message": "No se encontró la persona",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    persona.id_usuario = request.json('id_usuario')
    persona.cod_identificacion = request.json('cod_identificacion')
    persona.doc_identificacion = request.json('doc_identificacion')
    persona.nombres = request.json('nombres')
    persona.apellidos = request.json('apellido')
    persona.fec_nacimiento = request.json('fec_nacimiento')
    persona.n_celular = request.json('n_celular')
    persona.genero = request.json('genero')

    db.session.commit()

    result = persona_schema.dump(persona)

    data = {
        "message": "Persona actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@persona_routes.route('/delete_persona/<int:id_persona>', methods=['DELETE'])
def delete_persona(id_persona):
    persona = Persona.query.get(id_persona)

    if not persona:
        data = {
            "message": "No se encontró la persona",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(persona)
    db.session.commit()

    data = {
        "message": "Persona eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)