from utils.ma import ma
from models.Seccion import Seccion
from marshmallow import fields
from schemas.curso_schema import Curso_Schema
from schemas.aula_schema import Aula_Schema
from schemas.docente_schema import Docente_Schema
from schemas.dia_schema import Dia_Schema

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
                  'dia'
                  )
    
    curso = ma.Nested(Curso_Schema)
    aula = ma.Nested(Aula_Schema)
    docente = ma.Nested(Docente_Schema)
    dia = ma.Nested(Dia_Schema)

seccion_schema = Seccion_Schema()
secciones_schema = Seccion_Schema(many=True)
