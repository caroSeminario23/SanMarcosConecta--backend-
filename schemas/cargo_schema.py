from utils.ma import ma
from models.Cargo import Cargo
from marshmallow import fields

class Cargo_Schema(ma.Schema):
    class Meta:
        model = Cargo
        fields = ('id_cargo', 
                  'nombre'
                  )  

# Instancias del esquema para un solo objeto y una lista de objetos
cargo_schema = Cargo_Schema()
cargos_schema = Cargo_Schema(many=True)
