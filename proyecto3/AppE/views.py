from django.shortcuts import render
from django.http import HttpResponse
from AppE.models import Guitarra, Vendedor,Provedor
from AppE.forms import GuitarraFormularios, VendedorFormularios,ProvedorFormularios
# Create your views here.

def inicio(req):
    return render(req,'appe/padre.html')


def guitarras(req):
    return render(req,'appe/guitarras.html')

def provedor (req):
    return render(req, 'appe/provedor.html')

def vendedor(req):
    return render(req,'appe/vendedor.html')


def guitarra_form(req):

    if req.method == "POST":  
        miFormulario = GuitarraFormularios(req.POST)  
        print(miFormulario)  

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            guitarras = Guitarra(modelo=informacion["modelo"], marca=informacion["marca"])  
            guitarras.save()  
            return render(req, 'appe/index.html')  
    else:
        miFormulario = GuitarraFormularios()  

    return render(req, 'appe/guitarra-form.html', {"miFormulario": miFormulario})


def provedor_form(req):

    if req.method == "POST":  
        miFormulario = ProvedorFormularios(req.POST)  
        print(miFormulario)  

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            provedores= Provedor(nombre=informacion["nombre"])  
            provedores.save()  
            return render(req, 'appe/index.html')  
    else:
        miFormulario = ProvedorFormularios()  

    return render(req, 'appe/provedor-form.html', {"miFormulario": miFormulario})


def vendedor_form(req):

    if req.method == "POST":  
        miFormulario = VendedorFormularios(req.POST)  
        print(miFormulario)  

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            vendedores = Vendedor(nombre=informacion["nombre"], apellido=informacion["apellido"])  
            vendedores.save()  
            return render(req, 'appe/index.html')  
    else:
        miFormulario = VendedorFormularios()  

    return render(req, 'appe/vendedor-form.html', {"miFormulario": miFormulario})


def busquedaModelo(req):
    return render(req, "AppE/busquedaModelo.html")

def buscar(req):

    if req.GET["modelo"]:

        modelo = req.GET['modelo']

        marca = Guitarra.objects.filter(modelo__icontains=modelo)

        return render(req, "AppE/resultadoBusqueda.html", {"modelo": modelo, "marca": marca})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)