from sqlalchemy.orm import relationship

from utils.db import db

class Seccion(db.Model):
    __tablename__ = 'seccion'

    id_seccion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False, unique=True)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    id_aula = db.Column(db.Integer, db.ForeignKey('aula.id_aula'), nullable=False)
    id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=False)
    id_dia = db.Column(db.Integer, db.ForeignKey('dia.id_dia'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

    # relaciones
    # curso = relationship('Curso', backref='seccion1')
    # aula = relationship('Aula', backref='seccion2')
    # docente = relationship('Docente', back_populates='secciones')
    # dia = relationship('Dia', backref='seccion3')
    # asistencias_doc = relationship('Asistencia_doc', back_populates='seccion')
    # asistencias_est = relationship('Asistencia_est', back_populates='seccion')
    
    # relaciones v2
    asistencia_doc = relationship('Asistencia_doc', backref='seccion', cascade='all, delete-orphan')
    asistencia_est = relationship('Asistencia_est', backref='seccion', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, nombre, id_curso, id_aula, id_docente, id_dia, hora_inicio, hora_fin):
        self.nombre = nombre
        self.id_curso = id_curso
        self.id_aula = id_aula
        self.id_docente = id_docente
        self.id_dia = id_dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin