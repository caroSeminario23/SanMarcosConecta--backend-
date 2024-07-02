from sqlalchemy.orm import relationship

from utils.db import db

class Pabellon(db.Model):
    __tablename__ = 'pabellon'

    id_pabellon = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
    # relaciones v2
    aula = relationship('Aula', backref='pabellon', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre