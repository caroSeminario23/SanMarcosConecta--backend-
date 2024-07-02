from utils.ma import ma
from models.Asistencia_admin import Asistencia_admin
from marshmallow import fields
from schemas.jornada_schema import Jornada_Schema

class Asistencia_admin_Schema(ma.Schema):
    class Meta:
        model = Asistencia_admin
        fields = ('id_asistencia_admin',
                  'id_jornada', 
                  'fecha_marcado', 
                  'marcada', 
                  'jornada'
                  )
    
    jornada = ma.Nested(Jornada_Schema)

asistencia_admin_schema = Asistencia_admin_Schema()
asistencias_admin_schema = Asistencia_admin_Schema(many=True)
