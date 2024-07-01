from sqlalchemy.orm import relationship

from utils.db import db

class Persona(db.Model):
    __tablename__ = 'persona'

    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    cod_identificacion = db.Column(db.String(8), nullable=False, unique=True)
    doc_identificacion = db.Column(db.String(9), nullable=False, unique=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(150), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    n_celular = db.Column(db.String(12), nullable=False)
    genero = db.Column(db.Character(1), nullable=False) # M: Masculino, F: Femenino

    # relaciones
    usuario = relationship('Usuario', back_populates='persona')
    administrativos = relationship('Administrativo', back_populates='persona', cascade='all, delete-orphan')
    docentes = relationship('Docente', back_populates='persona', cascade='all, delete-orphan')
    estudiantes = relationship('Estudiante', back_populates='persona', cascade='all, delete-orphan')
    reservas = relationship('Reserva', back_populates='persona')
    
    # constructor de la clase
    def __init__(self, id_usuario, nombres, apellidos, fec_nacimiento, n_celular, genero):
        self.id_usuario = id_usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.n_celular = n_celular
        self.genero = genero