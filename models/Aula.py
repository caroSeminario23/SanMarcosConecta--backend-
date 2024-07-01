from sqlalchemy.orm import relationship

from utils.db import db

class Aula(db.Model):
    __tablename__ = 'aula'

    id_aula = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    id_pabellon = db.Column(db.Integer, db.ForeignKey('pabellon.id_pabellon'), nullable=False)
    n_piso = db.Column(db.Integer, nullable=False)
    id_tipo_aula = db.Column(db.Integer, db.ForeignKey('tipo_aula.id_tipo_aula'), nullable=False)
    coordenadas = db.Column(db.Point, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    aforo_actual = db.Column(db.Integer, nullable=False, default=0)

    # relaciones
    pabellon = relationship('Pabellon', backref='aula1')
    tipo_aula = relationship('Tipo_aula', backref='aula2')
    
    # constructor de la clase
    def __init__(self, nombre, id_pabellon, n_piso, id_tipo_aula, coordenadas, capacidad):
        self.nombre = nombre
        self.id_pabellon = id_pabellon
        self.n_piso = n_piso
        self.id_tipo_aula = id_tipo_aula
        self.coordenadas = coordenadas
        self.capacidad = capacidad