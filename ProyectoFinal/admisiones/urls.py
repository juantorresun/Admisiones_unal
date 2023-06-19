from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path("nuevo_proceso/", views.nuevo_proceso),
    path('nuevo_proceso/crear_periodo',views.crea_proceso),
    path('cupos/',views.consultar_cupos),
    path('cupos/consultar_cupos',views.consultar_cupos),
    path('nuevos_cupos/crear_cupos',views.crear_cupos),
    path('inscripcion/',views.inscripcion),
    path('inscripcion/crear_inscripcion',views.crear_inscripcion),
    path('nuevos_cupos/',views.nuevos_cupos),
    path('consulta_mod/',views.consulta_mod),
    path('consulta_mod/modificar_inscripcion',views.modificar_inscripcion),
    path('consulta_mod/update_inscripcion',views.update_inscripcion),
    path('consulta_citacion/',views.consulta_citacion),
    path('consulta_citacion/consultar_citacion',views.consultar_citacion),
    path('consulta_resultado/',views.consulta_resultado),
    path('consulta_resultado/consultar_resultados',views.Consultar_resultados),
    path('inicio/',views.inicio),
]