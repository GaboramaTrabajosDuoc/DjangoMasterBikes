from django.urls import path
from .views import index,arbici,repa,us,prod,job
from . import views

urlpatterns = [
    path('',index,name="index"),
    path('Arriendo', arbici,name="arriendobicis"),
    path('Reparaciones', repa,name="repa"),
    path('Nosotros', us,name="us"),
    path('Productos', prod,name="prod"),
    path('Vista tecnico', job,name="job"),
    path('delete_solic/<Nombre>', views.delete_RepSolic, name='delete-solic'),
]
