from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 
from django.db import connection
from .models import Periodo, Cupo, Inscripcion
from django.contrib import messages
# Create your views here.

def index(request):
    template = loader.get_template("admisiones/index.html")
    with connection.cursor() as cursor:
        cursor.execute("call consultarperiodos()")
        results = cursor.fetchall()
    return HttpResponse(template.render( {'Periodos': results}, request))    

def nuevo_proceso(request):
    context = {"dummy": 'dummy'}
    return render(request, "admisiones/nuevo_proceso.html", context)
def crea_proceso(request):
    if request.method=="POST":
        p=Periodo()
        p.año=request.POST.get('año')
        p.semestre=request.POST.get('semestre')
        p.Tipo=request.POST.get('tipo')
        p.Estado=request.POST.get('Estado')
        p.Fecha_inicio=request.POST.get('fecha_inicio')
        p.Fecha_cierre=request.POST.get('fecha_cierre')
        cursor=connection.cursor()
        cursor.execute("call crear_periodo('"+str(p.año)+"','"+str(p.semestre)+"','"+str(p.Tipo)+"','"+str(p.Estado)+"','"+str(p.Fecha_inicio)+"','"+str(p.Fecha_cierre)+"');")
        messages.success(request, "se creo el nuevo proceso")
        context = {"dummy": 'dummy'}
        template = loader.get_template("admisiones/index.html")
        with connection.cursor() as cursor:
            cursor.execute("call consultarperiodos()")
            results = cursor.fetchall()
        return HttpResponse(template.render( {'Periodos': results}, request))    

def consultar_cupos(request):
    if request.method=="POST":
        c=Cupo()
        c.año=request.POST.get('año')
        c.semestre=request.POST.get('semestre')
        template = loader.get_template("admisiones/cupos.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_cupos('"+str(c.año)+"','"+str(c.semestre)+"')")
            results = cursor.fetchall()
        return HttpResponse(template.render( {'Cupos': results}, request))   
    else:
        return render(request,'admisiones/cupos.html', {"dummy": 'dummy'})
    
def nuevos_cupos(request):
    with connection.cursor() as cursor:
        cursor.execute("call listar_programas()")
        results = cursor.fetchall()
    context={
        "programas": results,
    }
    return render(request, "admisiones/nuevos_cupos.html", context)

def crear_cupos(request):
    if request.method=="POST":
        c=Cupo()
        c.año=request.POST.get('año')
        c.semestre=request.POST.get('semestre')
        c.tipo_programa=request.POST.get('tipo')
        c.programa=request.POST.get('Programa')
        cantidad=request.POST.get('cantidad')
        cursor=connection.cursor()
        cursor.execute("call crear_cupos('"+str(c.año)+"','"+str(c.semestre)+"','"+str(c.programa)+"','"+str(c.tipo_programa)+"','"+str(cantidad)+"');")
        messages.success(request, "se creo el nuevo proceso")
    if request.method=="POST":
        c=Cupo()
        c.año=request.POST.get('año')
        c.semestre=request.POST.get('semestre')
        template = loader.get_template("admisiones/cupos.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_cupos('"+str(c.año)+"','"+str(c.semestre)+"')")
            results = cursor.fetchall()
        return HttpResponse(template.render( {'Cupos': results}, request))   
    else:
        return render(request,'admisiones/cupos.html', {"dummy": 'dummy'})
    
def inscripcion(request):
    with connection.cursor() as cursor:
        cursor.execute("call listar_programas()")
        results = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("call listar_tipo_admision()")
        results2 = cursor.fetchall()
    context={
        "programas": results, 
        "tipos_ad":results2,
    }
    return render(request, "admisiones/inscripcion.html", context)
def crear_inscripcion(request):
    if request.method=="POST":
        i=Inscripcion()
        i.correo=request.POST.get('correo')
        i.tipo_documento=request.POST.get('tipo_doc')
        i.documento=request.POST.get('documento')
        i.nombre=request.POST.get('nombre')
        i.tipo_ins=request.POST.get('tipo_ad')
        i.programa=request.POST.get('Programa')
        i.pin=request.POST.get('pin')
        cursor=connection.cursor()
        cursor.execute("call admisiones.registrar_inscripcion('"+str(i.documento)+"','"+str(i.correo)+"','"+str(i.tipo_documento)+"','"+str(i.nombre)+"','"+str(i.programa)+"','"+str(i.tipo_ins)+"','"+str(i.pin)+"');")
        return render(request,'admisiones/insOK.html', {"dummy": 'dummy'})
    
def consulta_mod (request):
    context={
        "dummy": 'dummy'
    }
    return render(request, "admisiones/Consulta_mod.html", context)
    
def modificar_inscripcion (request):
    if request.method=="POST":
        with connection.cursor() as cursor:
            cursor.execute("call listar_programas()")
            results = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("call listar_tipo_admision()")
            results2 = cursor.fetchall()
        i=Inscripcion()
        i.documento=request.POST.get('documento')
        i.pin=request.POST.get('pin')
        template = loader.get_template("admisiones/modificar_inscripcion.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_inscripcion('"+str(i.documento)+"','"+str(i.pin)+"')")
            results3 = cursor.fetchall()
        context={
            "programas": results, 
            "tipos_ad":results2,
            'Aspirante': results3,
        }
        return HttpResponse(template.render( context, request))   
    else:
        return render(request,'admisiones/modificar_inscripcion.html', {"dummy": 'dummy'})
    
def update_inscripcion(request):
    if request.method=="POST":
        i=Inscripcion()
        i.periodo=request.POST.get('peridoid')
        i.correo=request.POST.get('correo')
        i.documento=request.POST.get('documento')
        i.nombre=request.POST.get('nombre')
        i.tipo_ins=request.POST.get('tipo_ad')
        i.programa=request.POST.get('Programa')
        cursor=connection.cursor()
        cursor.execute("call admisiones.modificar_inscripcion('"+str(i.documento)+"','"+str(i.periodo)+"','"+str(i.correo)+"','"+str(i.nombre)+"','"+str(i.programa)+"','"+str(i.tipo_ins)+"');")
        with connection.cursor() as cursor:
            cursor.execute("call listar_programas()")
            results = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("call listar_tipo_admision()")
            results2 = cursor.fetchall()
        i=Inscripcion()
        i.documento=request.POST.get('documento')
        i.pin=request.POST.get('pin')
        template = loader.get_template("admisiones/modificar_inscripcion.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_inscripcion('"+str(i.documento)+"','"+str(i.pin)+"')")
            results3 = cursor.fetchall()
        context={
            "programas": results, 
            "tipos_ad":results2,
            'Aspirante': results3,
        }
        messages.success(request, "Actualizacion exitosa." )
        return HttpResponse(template.render( context, request))   
    else:
        return render(request,'admisiones/modificar_inscripcion.html', {"dummy": 'dummy'})



def consulta_citacion (request):
    context={
        "dummy": 'dummy'
    }
    return render(request, "admisiones/Consulta_citacion.html", context)
    
def consultar_citacion (request):
    if request.method=="POST":

        i=Inscripcion()
        i.documento=request.POST.get('documento')
        i.pin=request.POST.get('pin')
        template = loader.get_template("admisiones/resultado_citacion.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_inscripcion('"+str(i.documento)+"','"+str(i.pin)+"')")
            results = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_citacion_prueba('"+str(i.documento)+"','"+str(i.pin)+"')")
            results2 = cursor.fetchall()     
        context={          
            'Aspirante': results,
            'Citacion': results2,
        }
        return HttpResponse(template.render( context, request))   
    else:
        return render(request,'admisiones/Consulta_citacion.html', {"dummy": 'dummy'})
    
def consulta_resultado (request):
    context={
        "dummy": 'dummy'
    }
    return render(request, "admisiones/Consulta_resultados.html", context)
    
def Consultar_resultados (request):
    if request.method=="POST":

        i=Inscripcion()
        i.documento=request.POST.get('documento')
        i.pin=request.POST.get('pin')
        template = loader.get_template("admisiones/resultado_examen.html")
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_inscripcion('"+str(i.documento)+"','"+str(i.pin)+"')")
            results = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("call admisiones.consultar_resultado_examen('"+str(i.documento)+"','"+str(i.pin)+"')")
            results2 = cursor.fetchall()     
        context={          
            'Aspirante': results,
            'Resultado_examen': results2,
        }
        return HttpResponse(template.render( context, request))   
    else:
        return render(request,'admisiones/Consulta_resultados.html', {"dummy": 'dummy'})
def inicio (request):
    context={
        "dummy": 'dummy'
    }
    return render(request, "admisiones/inicio.html", context)