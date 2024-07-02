from utils.ma import ma
from models.Administrativo import Administrativo
from marshmallow import fields
from schemas.persona_schema import Persona_Schema
from schemas.cargo_schema import Cargo_Schema

class Administrativo_Schema(ma.Schema):
    class Meta:
        model=Administrativo
        fields = ('id_administrativo',
                'id_persona',
                'id_cargo',
                'activo',
                'persona',
                'cargo'
                )
    
    persona=ma.Nested(Persona_Schema)
    cargo=ma.Nested(Cargo_Schema)
        
administrativo_schema = Administrativo_Schema()
administrativos_schema = Administrativo_Schema(many=True)
