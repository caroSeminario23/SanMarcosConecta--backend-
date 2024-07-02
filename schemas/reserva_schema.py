from utils.ma import ma
from models.Reserva import Reserva
from marshmallow import fields
from schemas.aula_schema import Aula_Schema
from schemas.persona_schema import Persona_Schema
from schemas.dia_schema import Dia_Schema

class Reserva_Schema(ma.Schema):
    class Meta:
        model = Reserva
        fields = ('id_reserva',
                  'id_aula',
                  'id_persona',
                  'id_dia',
                  'hora_inicio',
                  'hora_fin',
                  'aula',
                  'persona',
                  'dia'
                  )
    
    aula = ma.Nested(Aula_Schema)
    persona = ma.Nested(Persona_Schema)
    dia = ma.Nested(Dia_Schema)

reserva_schema = Reserva_Schema()
reservas_schema = Reserva_Schema(many=True)