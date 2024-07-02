from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Persona import Persona
from schemas.persona_schema import persona_schema, personas_schema

persona_routes = Blueprint("persona_routes", __name__)

@persona_routes.route('/create_persona', methods=['POST'])
def create_persona():
    
    data = request.get_json()
    
    id_usuario = data.get('id_usuario')
    cod_identificacion = data.get('cod_identificacion')
    doc_identificacion = data.get('doc_identificacion')
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    fec_nacimiento = data.get('fec_nacimiento')
    n_celular = data.get('n_celular')
    genero = data.get('genero')

    new_persona = Persona(id_usuario, nombres, cod_identificacion, doc_identificacion, apellidos, fec_nacimiento, n_celular, genero)

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
    
    data = request.get_json()

    persona.id_usuario = data.get('id_usuario')
    persona.cod_identificacion = data.get('cod_identificacion')
    persona.doc_identificacion = data.get('doc_identificacion')
    persona.nombres = data.get('nombres')
    persona.apellidos = data.get('apellido')
    persona.fec_nacimiento = data.get('fec_nacimiento')
    persona.n_celular = data.get('n_celular')
    persona.genero = data.get('genero')

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