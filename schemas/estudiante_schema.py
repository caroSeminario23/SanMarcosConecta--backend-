from utils.ma import ma
from models.estudiante import Estudiante
from marshmallow import fields
from schemas.persona_schema import Persona_Schema
from schemas.asistencia_est_schema import Asistencia_est_Schema

class Estudiante_Schema(ma.Schema):
    class Meta:
        model = Estudiante
        fields = ('id_estudiante', 
                  'id_persona', 
                  'n_ciclo', 
                  'egresado', 
                  'persona',
                  'asistencias_est'
                  )
    
    persona = ma.Nested(Persona_Schema)
    asistencias_est = ma.Nested(Asistencia_est_Schema)

estudiante_schema = Estudiante_Schema()
estudiantes_schema = Estudiante_Schema(many=True)