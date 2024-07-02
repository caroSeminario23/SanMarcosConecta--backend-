from utils.ma import ma
from models.jornada import Jornada
from marshmallow import fields
from schemas.administrativo_schema import Administrativo_Schema
from schemas.dia_schema import Dia_Schema
from schemas.asistencia_admin_schema import Asistencia_admin_Schema

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
                  'asistencias_admin'
                  )
    
    administrativo = ma.Nested(Administrativo_Schema)
    dia = ma.Nested(Dia_Schema)
    asistencias_admin = ma.Nested(Asistencia_admin_Schema)

jornada_schema = Jornada_Schema()
jornadas_schema = Jornada_Schema(many=True)