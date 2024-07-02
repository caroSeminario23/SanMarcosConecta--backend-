from utils.ma import ma
from models.seccion import Seccion
from marshmallow import fields
from schemas.curso_schema import Curso_Schema
from schemas.aula_schema import Aula_Schema
from schemas.docente_schema import Docente_Schema
from schemas.dia_schema import Dia_Schema
from schemas.asistencia_doc_schema import Asistencia_doc_Schema
from schemas.asistencia_est_schema import Asistencia_est_Schema

class Seccion_Schema(ma.Schema):
    class Meta:
        model = Seccion
        fields = ('id_seccion', 
                  'nombre', 
                  'id_curso', 
                  'id_aula', 
                  'id_docente',
                  'id_dia',
                  'hora_inicio',
                  'hora_fin',
                  'curso',
                  'aula',
                  'docente',
                  'dia',
                  'asistencias_doc',
                  'asistencias_est'
                  )
    
    curso = ma.Nested(Curso_Schema)
    aula = ma.Nested(Aula_Schema)
    docente = ma.Nested(Docente_Schema)
    dia = ma.Nested(Dia_Schema)
    asistencias_doc = ma.Nested(Asistencia_doc_Schema)
    asistencias_est = ma.Nested(Asistencia_est_Schema)

seccion_schema = Seccion_Schema()
secciones_schema = Seccion_Schema(many=True)
