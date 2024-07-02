from utils.ma import ma
from models.Aula import Aula
from marshmallow import fields
from schemas.pabellon_schema import Pabellon_Schema 
from schemas.tipo_aula_schema import Tipo_aula_Schema 

class Aula_Schema(ma.Schema):
    class Meta:
        model = Aula
        fields = ('id_aula', 
                  'nombre', 
                  'id_pabellon', 
                  'n_piso', 
                  'id_tipo_aula', 
                  'coordenadas', 
                  'capacidad', 
                  'aforo_actual', 
                  'pabellon', 
                  'tipo_aula')
    
    pabellon = ma.Nested(Pabellon_Schema)  
    tipo_aula = ma.Nested(Tipo_aula_Schema) 

# Instancias del esquema para un solo objeto y una lista de objetos
aula_schema = Aula_Schema()
aulas_schema = Aula_Schema(many=True)
