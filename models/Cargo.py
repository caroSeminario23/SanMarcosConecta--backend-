from sqlalchemy.orm import relationship

from utils.db import db

class Cargo(db.Model):
    __tablename__ = 'cargo'

    id_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(150), nullable=False, unique=True)
    
    # Relaciones v2
    administrativo = relationship('Administrativo', backref='cargo', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre