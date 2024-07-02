from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Reserva import Reserva
from schemas.reserva_schema import reserva_schema, reservas_schema

reserva_routes = Blueprint("reserva_routes", __name__)

@reserva_routes.route('/create_reserva', methods=['POST'])
def create_reserva():
    id_aula = request.json('id_aula')
    id_persona = request.json('id_persona')
    id_dia = request.json('id_dia')
    hora_inicio = request.json('hora_inicio')
    hora_fin = request.json('hora_fin')

    new_reserva = Reserva(id_aula, id_persona, id_dia, hora_inicio, hora_fin)

    db.session.add(new_reserva)
    db.session.commit()

    result = reserva_schema.dump(new_reserva)

    data = {
        "message": "Reserva creada correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@reserva_routes.route('/get_reservas', methods=['GET'])
def get_reservas():
    all_reservas = Reserva.query.all()

    if not all_reservas:
        data = {
            "message": "No se encontraron reservas",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = reservas_schema.dump(all_reservas)

    data = {
        "message": "Todos los registros de reservas han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@reserva_routes.route('/get_reserva/<int:id_reserva>', methods=['GET'])
def get_reserva(id_reserva):
    reserva = Reserva.query.get(id_reserva)

    if not reserva:
        data = {
            "message": "No se encontró la reserva",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = reserva_schema.dump(reserva)

    data = {
        "message": "Reserva encontrada",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@reserva_routes.route('/update_reserva/<int:id_reserva>', methods=['PUT'])
def update_reserva(id_reserva):
    reserva = Reserva.query.get(id_reserva)

    if not reserva:
        data = {
            "message": "No se encontró la reserva",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    id_aula = request.json('id_aula')
    id_persona = request.json('id_persona')
    id_dia = request.json('id_dia')
    hora_inicio = request.json('hora_inicio')
    hora_fin = request.json('hora_fin')

    reserva.id_aula = id_aula
    reserva.id_persona = id_persona
    reserva.id_dia = id_dia
    reserva.hora_inicio = hora_inicio
    reserva.hora_fin = hora_fin

    db.session.commit()

    result = reserva_schema.dump(reserva)

    data = {
        "message": "Reserva actualizada correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)
  
@reserva_routes.route('/delete_reserva/<int:id_reserva>', methods=['DELETE'])
def delete_reserva(id_reserva):
    reserva = Reserva.query.get(id_reserva)

    if not reserva:
        data = {
            "message": "No se encontró la reserva",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(reserva)
    db.session.commit()

    data = {
        "message": "Reserva eliminada correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)