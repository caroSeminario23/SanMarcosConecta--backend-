from sqlalchemy.orm import relationship

from utils.db import db

class Curso(db.Model):
    __tablename__ = 'curso'

    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
    # Relaciones v2
    seccion = relationship('Seccion', backref='curso', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre