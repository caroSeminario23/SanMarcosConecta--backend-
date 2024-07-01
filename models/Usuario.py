from sqlalchemy.orm import relationship

from utils.db import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contrasenia = db.Column(db.String(255), nullable=False)
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id_tipo_usuario'), nullable=False)

    # relaciones
    tipo_usuario = relationship('Tipo_usuario', backref='usuario1')
    persona = relationship('Persona', back_populates='usuario', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, email, contrasenia, id_tipo_usuario):
        self.email = email
        self.contrasenia = contrasenia
        self.id_tipo_usuario = id_tipo_usuario