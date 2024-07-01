from sqlalchemy.orm import relationship

from utils.db import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id_estudiante = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False, unique=True)
    codigo = db.Column(db.Character(8), nullable=False, unique=True)
    n_ciclo = db.Column(db.Integer, nullable=False, default=0)
    egresado = db.Column(db.Boolean, nullable=False, default=False)

    # relaciones
    persona = relationship('Persona', back_populates='estudiantes')
    asistencias_est = relationship('Asistencia_est', back_populates='estudiante', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_persona, codigo, n_ciclo, egresado):
        self.id_persona = id_persona
        self.codigo = codigo
        self.n_ciclo = n_ciclo
        self.egresado = egresado