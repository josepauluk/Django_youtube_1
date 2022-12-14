from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #Primera Vista

    p1=Persona('Profesor Juan', 'Díaz')

    #nombre='Juan'
    #apellido='Díaz'
    ahora=datetime.datetime.now()
    
    doc_externo=open('C:/Users/JosePc/Proyecto/info/info/plantillas/miplantilla.html')

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({'nombre_persona':p1.nombre, 'apellido_persona':p1.apellido, 'momento_actual':ahora})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Hasta luego alumnos')

def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento = '''<html>
    <body>
    <h2>
        Fecha y hora actuales %s
    </h2>
    </body>
    </html>''' % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, anio):
    #edadActual=18
    periodo=anio-2022
    edadFutura=edad+periodo
    documento= '''<html>
    <body>
    <h2>
        En el año %s tendrás %s años 
    </h2>
    </body>
    </html>'''%(anio, edadFutura)

    return HttpResponse(documento)