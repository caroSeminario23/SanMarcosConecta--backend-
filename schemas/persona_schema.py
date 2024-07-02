from utils.ma import ma
from models.persona import Persona
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema
from schemas.administrativo_schema import Administrativo_Schema
from schemas.docente_schema import Docente_Schema
from schemas.estudiante_schema import Estudiante_Schema
from schemas.reserva_schema import Reserva_Schema

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
                  'usuario',
                  'administrativos',
                  'docentes',
                  'estudiantes',
                  'reservas'
                  )
    
    usuario = ma.Nested(Usuario_Schema)
    administrativos = ma.Nested(Administrativo_Schema)
    docentes = ma.Nested(Docente_Schema)
    estudiantes = ma.Nested(Estudiante_Schema)
    reservas = ma.Nested(Reserva_Schema)

persona_schema = Persona_Schema()
personas_schema = Persona_Schema(many=True)