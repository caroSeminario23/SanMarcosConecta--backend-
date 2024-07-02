from sqlalchemy.orm import relationship

from utils.db import db

class Tipo_aula(db.Model):
    __tablename__ = 'tipo_aula'

    id_tipo_aula = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
    # relaciones v2
    aula = relationship('Aula', backref='tipo_aula', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre