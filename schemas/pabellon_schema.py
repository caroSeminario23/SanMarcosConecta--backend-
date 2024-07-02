from utils.ma import ma
from models.Pabellon import Pabellon
from marshmallow import fields

class Pabellon_Schema(ma.Schema):
    class Meta:
        model = Pabellon
        fields = ('id_pabellon', 
                  'nombre'
                  )

pabellon_schema = Pabellon_Schema()
pabellones_schema = Pabellon_Schema(many=True)