from utils.ma import ma
from models.Tipo_aula import Tipo_aula
from marshmallow import fields

class Tipo_aula_Schema(ma.Schema):
    class Meta:
        model = Tipo_aula
        fields = ('id_tipo_aula', 
                  'nombre'
                  )

tipo_aula_schema = Tipo_aula_Schema()
tipos_aulas_schema = Tipo_aula_Schema(many=True)
