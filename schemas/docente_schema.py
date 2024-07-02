from utils.ma import ma
from models.Docente import Docente
from marshmallow import fields
from schemas.persona_schema import Persona_Schema

class Docente_Schema(ma.Schema):
    class Meta:
        model = Docente
        fields = ('id_docente', 
                  'id_persona', 
                  'activo', 
                  'persona'
                  )  

    persona = ma.Nested(Persona_Schema)

# Instancias del esquema para un solo objeto y una lista de objetos
docente_schema = Docente_Schema()
docentes_schema = Docente_Schema(many=True)
