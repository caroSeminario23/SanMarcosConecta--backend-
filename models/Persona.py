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
    genero = db.Column(db.String(1), nullable=False) # M: Masculino, F: Femenino

    # relaciones
    # usuario = relationship('Usuario', back_populates='personas')
    # administrativos = relationship('Administrativo', back_populates='persona', cascade='all, delete-orphan')
    # docentes = relationship('Docente', back_populates='persona', cascade='all, delete-orphan')
    # estudiantes = relationship('Estudiante', back_populates='persona', cascade='all, delete-orphan')
    # reservas = relationship('Reserva', back_populates='persona')
    
    # relaciones v2
    docente = relationship('Docente', backref='persona', cascade='all, delete-orphan')
    estudiante = relationship('Estudiante', backref='persona', cascade='all, delete-orphan')
    administrativo = relationship('Administrativo', backref='persona', cascade='all, delete-orphan')
    reserva = relationship('Reserva', backref='persona', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_usuario, nombres, cod_identificacion, doc_identificacion, apellidos, fec_nacimiento, n_celular, genero):
        self.id_usuario = id_usuario
        self.cod_identificacion = cod_identificacion
        self.doc_identificacion = doc_identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.n_celular = n_celular
        self.genero = genero