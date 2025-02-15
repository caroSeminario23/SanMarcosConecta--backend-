from utils.ma import ma
from models.Tipo_usuario import Tipo_usuario
from marshmallow import fields

class Tipo_usuario_Schema(ma.Schema):
    class Meta:
        model = Tipo_usuario
        fields = ('id_tipo_usuario', 
                  'nombre'
                  )

tipo_usuario_schema = Tipo_usuario_Schema()
tipos_usuarios_schema = Tipo_usuario_Schema(many=True)