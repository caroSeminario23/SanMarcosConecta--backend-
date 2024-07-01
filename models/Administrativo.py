from sqlalchemy.orm import relationship

from utils.db import db

class Administrativo(db.Model):
    __tablename__ = 'administrativo'

    id_administrativo = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False, unique=True)
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargo.id_cargo'), nullable=False)
    activo = db.Column(db.Boolean, nullable=False, default=True)

    # relaciones
    persona = relationship('Persona', backref='administrativo1')
    cargo = relationship('Cargo', backref='administrativo2')
    jornadas = relationship('Jornada', back_populates='administrativo')
    
    # constructor de la clase
    def __init__(self, id_persona, id_cargo):
        self.id_persona = id_persona
        self.id_cargo = id_cargo