from utils.ma import ma
from models.Asistencia_est import Asistencia_est
from marshmallow import fields
from schemas.seccion_schema import Seccion_Schema  
from schemas.estudiante_schema import Estudiante_Schema  

class Asistencia_est_Schema(ma.Schema):
    class Meta:
        model = Asistencia_est
        fields = ('id_asistencia_est', 
                  'id_seccion', 
                  'id_estudiante', 
                  'fecha_marcado', 
                  'marcada', 
                  'seccion', 
                  'estudiante')
    
    seccion = ma.Nested(Seccion_Schema) 
    estudiante = ma.Nested(Estudiante_Schema) 

# Instancias del esquema para un solo objeto y una lista de objetos
asistencia_est_schema = Asistencia_est_Schema()
asistencias_est_schema = Asistencia_est_Schema(many=True)
