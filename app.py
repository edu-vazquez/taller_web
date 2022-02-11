from flask import Flask, escape, request, render_template, url_for   #IMPORTA LA LIBRERIA

app = Flask(__name__)       #PARA LLAMAR AL FLASK

@app.route("/")             #DEFINELA RUTA DE INICIO QUE SERA APLICADA A LA FUNCION hola()

def hola():                 #DEFINE LA FUNCION hola()
    return "Hi Penguins!"   #RETORNA: Hi Penguins!

@app.route("/coach")                                    #DEFINELA UNA NUEVA RUTA /coach
def hola_coaches():                                     #DEFINIMOS LA FUNCION QUE SERA DEVUELTA 
    nombre = "Edu"                                     #INICIALIZAMOS UN DATO
    devolver = request.args.get("nombre", nombre)       #DEFINIMOS QUE SERA DEVUELTO
    return f"Hola, {escape(devolver)}"                  #RETORNAMOS HTML

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")