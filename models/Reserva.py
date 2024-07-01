from sqlalchemy.orm import relationship

from utils.db import db

class Reserva(db.Model):
    __tablename__ = 'reserva'

    id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_aula = db.Column(db.Integer, db.ForeignKey('aula.id_aula'), nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    id_dia = db.Column(db.Integer, db.ForeignKey('dia.id_dia'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=True)

    # relaciones
    aula = relationship('Aula', backref='reserva1')
    persona = relationship('Persona', back_populates='reservas')
    dia = relationship('Dia', backref='reserva2')
    
    # constructor de la clase
    def __init__(self, id_aula, id_persona, id_dia, hora_inicio, hora_fin):
        self.id_aula = id_aula
        self.id_persona = id_persona
        self.id_dia = id_dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin