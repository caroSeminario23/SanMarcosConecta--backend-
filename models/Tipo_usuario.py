from sqlalchemy.orm import relationship

from utils.db import db

class Tipo_usuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id_tipo_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
    # relaciones v2
    usuario = relationship('Usuario', backref='tipo_usuario', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre