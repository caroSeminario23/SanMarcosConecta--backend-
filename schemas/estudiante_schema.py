from utils.ma import ma
from models.Estudiante import Estudiante
from marshmallow import fields
from schemas.persona_schema import Persona_Schema

class Estudiante_Schema(ma.Schema):
    class Meta:
        model = Estudiante
        fields = ('id_estudiante', 
                  'id_persona', 
                  'n_ciclo', 
                  'egresado', 
                  'persona',
                  )
    
    persona = ma.Nested(Persona_Schema)

estudiante_schema = Estudiante_Schema()
estudiantes_schema = Estudiante_Schema(many=True)