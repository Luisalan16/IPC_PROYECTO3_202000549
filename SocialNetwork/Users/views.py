from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from .forms import xmlFile
from .models import File


# Create your views here.

# ------Pagina Presentación------
def WebsiteHome(request):
    return render (request, 'Publicacion/index.html', {})

# ------Pagina Inicio ChapinChat------
def Chapinchat(resquest):
    return render (resquest, 'Publicacion/chapin.html', {})

# ------Pagina Lista de Usuarios------
def getUsers(request):
    return render (request, 'Publicacion/getUsers.html', {})

# ------Pagina Documentación------
def Documentation(request):
    context = {
        'STATIC_URL': '/static/',
    }
    return render (request, 'Publicacion/document.html', context)

# ------Pagina Creador------
def Creator(request):
    return render (request, 'Publicacion/creador.html', {})

# ------Leer xml------
def Lectura(file):
    tree = ET.parse(file)
    root = tree.getroot()

    datos = []
    for child in root:
        dato = {}
        dato['codigo'] = child.find('codigo').text
        dato['nombre'] = child.find('nombre').text
        datos.append(dato)
    return datos
# ------Leer xml------
def Cargarfile(request):
    if request.method == 'POST':
        form = xmlFile(request.POST, request.FILES)
        if form.is_valid():
            
            xml_file = request.FILES['archivo']
            xmlcontent = [line.decode('utf-8').strip() for line in xml_file]
            print(xmlcontent)
            return render(request, 'Publicacion/getUsers.html', {'xmlcontent': xmlcontent})
            
    else:
        form = xmlFile()
    return render(request, 'Publicacion/chapin.html', {'form': form})



def Upload(request):
    if request.method == 'POST':
        form = xmlFile(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            tree = ET.parse(archivo)
            root = tree.getroot()
            
            for Juegos in root.findall('Plataforma'):
                codigo = Juegos.find('codigo').text
                nombre = Juegos.find('nombre').text
                juego = File(codigo=codigo, nombre=nombre)
                juego.save()
            return redirect('listaUsers')
    else:
        form = xmlFile()
        return render(request, 'Publicacion/chapin.html', {'form':form})
    
def Lista(request):
    plataformas = File.objects.all()
    context = {'plataformas': plataformas}
    return render(request, 'Publicacion/getUsers.html', context)