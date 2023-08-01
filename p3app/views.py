from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

####################################
### Forms con listas de rgistros ###
####################################

# Create your views here.
def index(request):
    return render(request,"p3app/base.html")

def catalogo(request):
    ctx={"catalogo": CatalogoVenta.objects.all()} #referenciar en la tabla de catalogoventa.html
    return render(request,"p3app/catalogoventa.html",ctx)

def vendedor(request):
    ctx={"vendedores": Vendedor.objects.all()} #referenciar en la tabla de vendedor.html
    return render(request,'p3app/vendedor.html',ctx)

def socio(request):
    ctx={"socios": Socio.objects.all()} #referenciar en la tabla de socio.html
    return render(request,'p3app/socio.html',ctx)


##################################
### Forms para añadir rgistros ###
##################################

def cliente(request):
    if request.method == "POST":
        cliForm = ClienteForm(request.POST)
        if cliForm.is_valid():
            informacion = cliForm.cleaned_data
            nombre = informacion['nombre']
            email = informacion['email']
            
            # Revisa si el email ya existe en la base de datos
            if Cliente.objects.filter(nombre=nombre).exists():
                return HttpResponse("Error: Este usuario ya existe.")
            
            if Cliente.objects.filter(email=email).exists():
                return HttpResponse("Error: Correo ya vinculado a un usuario.")
            
            # SI no se encuentran valores duplicados, guarda el nuevo cliente
            cliente = Cliente(nombre=nombre, fechadenacimiento=informacion['fechadenacimiento'], email=email)
            cliente.save()
            return render(request, "p3app/base.html")
    else:
        cliForm = ClienteForm()
    return render(request, 'p3app/cliente.html', {'form': cliForm})


def catalogoform(request):
    if request.method == "POST":
        catForm = CatalogoForm(request.POST)
        if catForm.is_valid():
            informacion = catForm.cleaned_data
            articulo = informacion['articulo']
            cantidad = informacion['cantidad']
            categoria = informacion['categoria']

            # Revisa si el articulo ya existe en la base de datos
            if CatalogoVenta.objects.filter(articulo=articulo).exists():
                return HttpResponse("Error: Este artículo ya existe.")
            
            # SI no se encuentran valores duplicados, guarda el nuevo articulo
            articulo = CatalogoVenta(articulo=articulo, cantidad=cantidad, categoria=categoria )
            articulo.save()
            return render(request, "p3app/catalogoventa.html")
    else:
        catForm=CatalogoForm()
    return render(request, 'p3app/catalogoform.html', {'form': catForm})


def vendedorform(request):
    if request.method == "POST":
        vendForm = VendedorForm(request.POST)
        if vendForm.is_valid():
            informacion = vendForm.cleaned_data
            nombre = informacion['nombre']
            telefono = informacion['telefono']
            email = informacion['email']
            rfc = informacion['rfc']

            # Revisa si el vendedor ya existe en la base de datos
            if Vendedor.objects.filter(nombre=nombre).exists():
                return HttpResponse("Error: Este vendedor ya existe.")
            
            # Revisa si el telefono ya existe en la base de datos
            if Vendedor.objects.filter(telefono=telefono).exists():
                return HttpResponse("Error: Este telefono ya está registrado.")
            
             # Revisa si el vendedor ya existe en la base de datos de acuerdo a su rfc
            if Vendedor.objects.filter(rfc=rfc).exists():
                return HttpResponse("Error: Este vendedor ya está registrado.")
            
            # SI no se encuentran valores duplicados, guarda el nuevo articulo
            vendedor = Vendedor(nombre=nombre, telefono=telefono, email=email, rfc=rfc )
            vendedor.save()
            return render(request, "p3app/vendedor.html")
    else:
        vendForm=VendedorForm()
    return render(request, 'p3app/vendedorform.html', {'form': vendForm})


def socioform(request):
    if request.method == "POST":
        socForm = SocioForm(request.POST)
        if socForm.is_valid():
            informacion = socForm.cleaned_data
            empresa = informacion['empresa']
            paisdeorigen = informacion['paisdeorigen']
            

            # Revisa si la empresa ya existe en la base de datos
            if Socio.objects.filter(empresa=empresa).exists():
                return HttpResponse("Error: Esta empresa ya está registrada como socio.")
            
            # SI no se encuentran valores duplicados, guarda la información introducida
            socio = Socio(empresa=empresa, paisdeorigen=paisdeorigen )
            socio.save()
            return render(request, "p3app/socio.html")
    else:
        socForm=SocioForm()
    return render(request, 'p3app/socioform.html', {'form': socForm})


#####################################
### Forms para consultar rgistros ###
#####################################
def barraconsulta(request):
    return render(request,'p3app/barraconsulta.html')

def consultacatalogo(request):
    if request.GET['articulo']:
        articulo = request.GET['articulo']
        catalogo = CatalogoVenta.objects.filter(articulo__icontains=articulo)
        return render(request,
                      "p3app/catalogoventabuscar.html",
                      {"articulo":articulo, "catalogo":catalogo})
    
    return HttpResponse("El artículo buscado no se encuentra")