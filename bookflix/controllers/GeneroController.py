from flask import request, render_template, session, abort
from flask import send_from_directory, url_for, redirect
from models.genero import Genero


class GeneroController():

    def __init__(self):
        pass

    def index(self):
        generos = Genero.all()
        return render_template('generos/index.html', generos=generos)

    def new(self):
        errores = []
        if request.method == 'GET':
            return render_template('generos/new.html')
        elif request.method == 'POST':
            if Genero.existe_genero_con_nombre(request.form["nombre"]):
                errores.append(
                    "Ya existe un genero con el nombre especificado.")
                return render_template('generos/new.html', errores=errores)
            else:
                Genero.crear(request.form["nombre"])
                return self.index()

    def edit(self):
        errores = []
        if request.method == 'GET':
            genero = Genero.encontrar_por_id(request.args.get("genero_id"))
            return render_template('generos/edit.html', genero=genero)
        elif request.method == 'POST':
            if Genero.existe_genero_con_nombre(request.form["nombre"]):
                genero = Genero.encontrar_por_id(request.args.get("genero_id"))
                errores.append(
                    "Ya existe un genero con el nombre especificado.")
                return render_template('generos/edit.html', genero=genero, errores=errores)
            else:
                Genero.edit(request.form["nombre"], request.form["id"])
                return self.index()

    def delete(self, genero_id):
        errores = []
        errores.append("Se elimino el genero correctamente")
        genero = Genero.eliminar(genero_id)
        generos = Genero.all()
        return render_template('generos/index.html', generos=generos, errores=errores)


generoController = GeneroController()
