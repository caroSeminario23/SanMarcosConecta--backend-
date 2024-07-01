from sqlalchemy.orm import relationship

from utils.db import db

class Asistencia_est(db.Model):
    __tablename__ = 'asistencia_est'

    id_asistencia_est = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'), nullable=False)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    fecha_marcado = db.Column(db.DateTime, nullable=False)
    marcada = db.Column(db.Boolean, nullable=False, default=False)

    # relaciones
    seccion = relationship('Seccion', back_populates='asistencias_est')
    estudiante = relationship('Estudiante', back_populates='asistencias_est')
    
    # constructor de la clase
    def __init__(self, id_seccion, id_estudiante, fecha_marcado):
        self.id_seccion = id_seccion
        self.id_estudiante = id_estudiante
        self.fecha_marcado = fecha_marcado