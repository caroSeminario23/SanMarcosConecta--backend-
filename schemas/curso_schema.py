from utils.ma import ma
from models.Curso import Curso
from marshmallow import fields

class Curso_Schema(ma.Schema):
    class Meta:
        model = Curso
        fields = ('id_curso', 
                  'nombre'
                  )  

# Instancias del esquema para un solo objeto y una lista de objetos
curso_schema = Curso_Schema()
cursos_schema = Curso_Schema(many=True)
