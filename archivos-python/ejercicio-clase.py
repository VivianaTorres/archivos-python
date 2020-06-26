from flask import Flask, request, jsonify , render_template
from math import sqrt
app = Flask(__name__)

#RUTA 1
@app.route("/formula/<int:a>/<int:b>/<int:c>")
def calcular(a, b, c):
    if a!=0:
        resultado1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        resultado2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    
    return render_template("registro/resultado-ecuacion.html", resultado1=resultado1, resultado2=resultado2)

#RUTA 2
@app.route("/formula", methods=['POST'])
def formulario():
    parametroa = request.form['a']  
    parametrob = request.form['b']
    parametroc = request.form['c']
    a = int(parametroa)
    b = int(parametrob)
    c = int(parametroc)
    if a!=0:
        resultado1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        resultado2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    
    return render_template("registro/resultado-ecuacion.html", resultado1=resultado1, resultado2=resultado2)

#RUTA 3
@app.route("/formulajson", methods=['POST'])
def formulajson():
    data = request.get_json() 
    parametroa = data['a']
    parametrob = data['b']
    parametroc = data['c']
    
    a = int(parametroa)
    b = int(parametrob)
    c = int(parametroc)
    if a!=0:
        resultado1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        resultado2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    
    return render_template("registro/resultado-ecuacion.html", resultado1=resultado1, resultado2=resultado2)

@app.route("/retornajson", methods=['GET'])
def retornajson():
    ecuacion = {
            "a": 3,
            "b": 8,
            "c": 2
            }
    return jsonify(ecuacion)
