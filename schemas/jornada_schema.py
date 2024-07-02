from utils.ma import ma
from models.Jornada import Jornada
from marshmallow import fields
from schemas.administrativo_schema import Administrativo_Schema
from schemas.dia_schema import Dia_Schema

class Jornada_Schema(ma.Schema):
    class Meta:
        model = Jornada
        fields = ('id_jornada', 
                  'id_administrativo', 
                  'id_dia', 
                  'hora_inicio', 
                  'hora_fin',
                  'administrativo',
                  'dia',
                  )
    
    administrativo = ma.Nested(Administrativo_Schema)
    dia = ma.Nested(Dia_Schema)

jornada_schema = Jornada_Schema()
jornadas_schema = Jornada_Schema(many=True)