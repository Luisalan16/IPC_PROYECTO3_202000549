from flask import Blueprint, request, render_template
from controller.controller import *

home = Blueprint('home', __name__)


# --------Ruta Inicio/Home--------
@home.route('/home')
def index():
    return "siu"


# --------Ruta /ObtenerUsuarios--------
@home.route('/ObtenerUsers', methods=['GET'])
def getUsers():
    return 'Aqui obtengo la lista'


# --------Ruta /MandarMensaje--------
@home.route('/MandarMensaje', methods=['POST'])
def postMessage():
    print(request.data)
    Mensaje1 = request.data
    send = Mensaje(Mensaje1)
    return send 
   

# --------Ruta /MandarMensajes--------
@home.route('/MandarMensajes', methods=['POST'])
def postMessages():
    return "f"

# --------Ruta /ObtenerMensajes--------
@home.route('/ObtenerMensajes', methods=['GET'])
def getMessages():
    mensajes = Mensaje()
    return (mensajes)

# --------Ruta /MandarPerfiles--------
@home.route('/MandarPerfiles', methods=['POST'])
def postProfiles():
    return 'Aqui envio los perfiles'


# --------Ruta /ObtenerPesos--------
@home.route('/ObtenerPesos', methods=['GET'])
def getWeight():
    return 'Aqui obtengo los pesos'


# --------Ruta /Reset--------
@home.route('/Reset', methods=['DELETE'])
def deleteInfo():
    return 'Aqui se borra todo'