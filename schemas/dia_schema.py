from utils.ma import ma
from models.Dia import Dia
from marshmallow import fields

class Dia_Schema(ma.Schema):
    class Meta:
        model = Dia
        fields = ('id_dia', 
                  'nombre')

# Instancias del esquema para un solo objeto y una lista de objetos
dia_schema = Dia_Schema()
dias_schema = Dia_Schema(many=True)
