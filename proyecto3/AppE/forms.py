from django import forms


class GuitarraFormularios(forms.Form):
    modelo = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)

class ProvedorFormularios(forms.Form):
    nombre=forms.CharField(max_length=40)

class VendedorFormularios(forms.Form):
    nombre=nombre=forms.CharField(max_length=40)
    apellido=apellido=forms.CharField(max_length=40)


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)

