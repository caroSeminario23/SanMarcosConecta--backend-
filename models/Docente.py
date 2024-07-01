from sqlalchemy.orm import relationship

from utils.db import db

class Docente(db.Model):
    __tablename__ = 'docente'

    id_docente = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False, unique=True)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    
    # relaciones
    persona = relationship('Persona', back_populates='docentes')
    
    # constructor de la clase
    def __init__(self, id_persona):
        self.id_persona = id_persona