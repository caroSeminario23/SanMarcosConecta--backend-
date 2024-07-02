from sqlalchemy.orm import relationship

from utils.db import db

class Asistencia_admin(db.Model):
    __tablename__ = 'asistencia_admin'

    id_asistencia_admin = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_jornada = db.Column(db.Integer, db.ForeignKey('jornada.id_jornada'), nullable=False)
    fecha_marcado = db.Column(db.DateTime, nullable=False)
    marcada = db.Column(db.Boolean, nullable=False, default=False)

    # relaciones
    # jornada = relationship('Jornada', back_populates='asistencias_admin')
    
    # constructor de la clase
    def __init__(self, id_jornada, fecha_marcado):
        self.id_jornada = id_jornada
        self.fecha_marcado = fecha_marcado