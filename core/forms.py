from tkinter import Widget
from turtle import width
from django import forms
from django.forms import ModelForm
from .models import RepSolic


#Formulario

class RepairForm(ModelForm):
    class Meta:
        model = RepSolic
        fields = ('Nombre','Numero','Correo','Hora','Direccion','DetalleProblema','ImagenProblema')

        labels = {
			'Nombre': '',
			'Numero': '',
			'Correo': '',
			'Hora': '',
			'Direccion': '',
			'DetalleProblema': '',	
		}

        widgets = {

            'Nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'Numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de contacto'}),
            'Correo': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo'}),
            'Hora': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora Ej: 13/03/2023-14:00'}),
            'Direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'DetalleProblema': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalles del problema'}),

        }








