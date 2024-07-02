from utils.ma import ma
from models.asistencia_doc import Asistencia_doc
from marshmallow import fields
from schemas.Seccion_Schema import Seccion_Schema

class Asistencia_doc_Schema(ma.Schema):
    class Meta:
        model = Asistencia_doc
        fields = ('id_asistencia_doc', 
                  'id_seccion', 
                  'fecha_marcado', 
                  'marcada', 
                  'seccion'
                  )
    
    seccion = ma.Nested(Seccion_Schema)

asistencia_doc_schema = Asistencia_doc_Schema()
asistencias_doc_schema = Asistencia_doc_Schema(many=True)
