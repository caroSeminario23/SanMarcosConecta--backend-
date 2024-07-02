from flask import Flask
from flask_cors import CORS
from utils.db import db

from services.administrativo import administrativo_routes
from services.asistencia_admin import asistencia_admin_routes
from services.asistencia_doc import asistencia_doc_routes
from services.asistencia_est import asistencia_est_routes
from services.aula import aula_routes
from services.cargo import cargo_routes
from services.curso import curso_routes
from services.dia import dia_routes
from services.docente import docente_routes
from services.estudiante import estudiante_routes
from services.jornada import jornada_routes
from services.pabellon import pabellon_routes
from services.persona import persona_routes
from services.reserva import reserva_routes
from services.seccion import seccion_routes
from services.tipo_aula import tipo_aula_routes
from services.tipo_usuario import tipo_usuario_routes
from services.usuario import usuario_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION


app=Flask(__name__)

CORS(app, origins=['http://localhost:4200'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     allow_headers=['Content-Type', 'Authorization'])


app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(administrativo_routes, url_prefix='/administrativo_routes')
app.register_blueprint(asistencia_admin_routes, url_prefix='/asistencia_admin_routes')
app.register_blueprint(asistencia_doc_routes, url_prefix='/asistencia_doc_routes')
app.register_blueprint(asistencia_est_routes, url_prefix='/asistencia_est_routes')
app.register_blueprint(aula_routes, url_prefix='/aula_routes')
app.register_blueprint(cargo_routes, url_prefix='/cargo_routes')
app.register_blueprint(curso_routes, url_prefix='/curso_routes')
app.register_blueprint(dia_routes, url_prefix='/dia_routes')
app.register_blueprint(docente_routes, url_prefix='/docente_routes')
app.register_blueprint(estudiante_routes, url_prefix='/estudiante_routes')
app.register_blueprint(jornada_routes, url_prefix='/jornada_routes')
app.register_blueprint(pabellon_routes, url_prefix='/pabellon_routes')
app.register_blueprint(persona_routes, url_prefix='/persona_routes')
app.register_blueprint(reserva_routes, url_prefix='/reserva_routes')
app.register_blueprint(seccion_routes, url_prefix='/seccion_routes')
app.register_blueprint(tipo_aula_routes, url_prefix='/tipo_aula_routes')
app.register_blueprint(tipo_usuario_routes, url_prefix='/tipo_usuario_routes')
app.register_blueprint(usuario_routes, url_prefix='/usuario_routes')

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)