from utils.ma import ma
from models.Persona import Persona
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema

class Persona_Schema(ma.Schema):
    class Meta:
        model = Persona
        fields = ('id_persona',
                  'id_usuario',
                  'cod_identificacion',
                  'doc_identificacion',
                  'nombres',
                  'apellidos',
                  'fec_nacimiento',
                  'n_celular',
                  'genero',
                  'usuario'
                  )
    
    usuario = ma.Nested(Usuario_Schema)

persona_schema = Persona_Schema()
personas_schema = Persona_Schema(many=True)