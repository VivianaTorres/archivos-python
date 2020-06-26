from flask import Flask
app = Flask(__name__)

@app.route("/saludo/<nombre>/<apellido>")  # Ruta que abrira una funcion para el saludo con determinado nombre
def saludar(nombre, apellido): # nombre y apellido son los parametros de la funcion, deben tener el mismo nombre de la variable
    # muestra un saludo al usuario, los {} son los parametros que indican variables
    return "Hola {} {}, ¿cómo estás?".format(nombre, apellido)

@app.route("/calculadora/suma/<int:a>/mas/<int:b>") # Hace de una vez un casting --> indicando el tipo de variable. Si no se pone el tipo de variable aqui, la operacion lo que haria seria concatenar y no sumar
def calcular(a, b):
    suma = a + b
    # muestra la suma de los valores ingresados
    return "{} + {}  = {}".format(a, b, suma)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # muestra el subpath después de /path/
    return "Subpath %s" % subpath  # subpath lo que hace es enviar lo que se puso en la ruta despues del /path/ 

# ACTIVIDAD DE CLASE
@app.route("/empresa/<empresa>/nit/<nit>/<fecha>")  
def actividad(empresa, nit, fecha): 
    file = open('registros.txt','w')
    file.write("Empresa: {} \n nit: {} \n fecha: {} \n ".format(empresa, nit, fecha))
    file.close()
    return "Datos guardados"