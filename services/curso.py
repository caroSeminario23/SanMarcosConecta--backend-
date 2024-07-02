from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.Curso import Curso
from schemas.curso_schema import curso_schema, cursos_schema

curso_routes = Blueprint("curso_routes", __name__)

@curso_routes.route('/create_curso', methods=['POST'])
def create_curso():
    
    data = request.get_json()
    
    nombre = data.get('nombre')

    new_curso = Curso(nombre)

    db.session.add(new_curso)
    db.session.commit()

    result = curso_schema.dump(new_curso)

    data = {
        "message": "Curso creado correctamente",
        "status": 201,
        "data": result
    }

    return make_response(jsonify(data), 201)

@curso_routes.route('/get_cursos', methods=['GET'])
def get_cursos():
    all_cursos = Curso.query.all()

    if not all_cursos:
        data = {
            "message": "No se encontraron cursos",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = cursos_schema.dump(all_cursos)

    data = {
        "message": "Todos los registros de cursos han sido encontrados",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@curso_routes.route('/get_curso/<int:id_curso>', methods=['GET'])
def get_curso(id_curso):
    curso = Curso.query.get(id_curso)

    if not curso:
        data = {
            "message": "No se encontró el curso",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    result = curso_schema.dump(curso)

    data = {
        "message": "Curso encontrado",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@curso_routes.route('/update_curso/<int:id_curso>', methods=['PUT'])
def update_curso(id_curso):
    curso = Curso.query.get(id_curso)

    if not curso:
        data = {
            "message": "No se encontró el curso",
            "status": 404
        }
        return make_response(jsonify(data), 404)
    
    data = request.get_json()

    nombre = data.get('nombre')

    curso.nombre = nombre

    db.session.commit()

    result = curso_schema.dump(curso)

    data = {
        "message": "Curso actualizado correctamente",
        "status": 200,
        "data": result
    }

    return make_response(jsonify(data), 200)

@curso_routes.route('/delete_curso/<int:id_curso>', methods=['DELETE'])
def delete_curso(id_curso):
    curso = Curso.query.get(id_curso)

    if not curso:
        data = {
            "message": "No se encontró el curso",
            "status": 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(curso)
    db.session.commit()

    data = {
        "message": "Curso eliminado correctamente",
        "status": 200
    }

    return make_response(jsonify(data), 200)
