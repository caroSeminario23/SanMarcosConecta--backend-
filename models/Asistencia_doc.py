from sqlalchemy.orm import relationship

from utils.db import db

class Asistencia_doc(db.Model):
    __tablename__ = 'asistencia_doc'

    id_asistencia_doc = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_seccion = db.Column(db.Integer, db.ForeignKey('seccion.id_seccion'), nullable=False)
    fecha_marcado = db.Column(db.DateTime, nullable=False)
    marcada = db.Column(db.Boolean, nullable=False, default=False)

    # relaciones
    # seccion = relationship('Seccion', back_populates='asistencias_doc')
    
    # constructor de la clase
    def __init__(self, id_seccion, fecha_marcado):
        self.id_seccion = id_seccion
        self.fecha_marcado = fecha_marcado