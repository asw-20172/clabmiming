from django.contrib import admin
from .models.consulta import Consulta
from .models.data_red_social import Data_red_social
from .models.pais import Pais
from .models.palabra_clave import Palabra_clave
from .models.red_social import Red_social
from .models.carrera import Carrera
# Register your models here.
admin.site.register(Consulta)
admin.site.register(Data_red_social)
admin.site.register(Pais)
admin.site.register(Palabra_clave)
admin.site.register(Red_social)
admin.site.register(Carrera)
