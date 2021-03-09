from datetime import datetime

from flask import request, render_template, session, abort, redirect
from flask import send_from_directory, url_for, redirect
from models.anuncio import Anuncio
from config import config


class AnuncioController():

    def __init__(self):
        pass

    def index(self):
        anuncios = Anuncio.all()
        return render_template('anuncios/index.html', anuncios=anuncios)

    def gen_path(self, field):
        file = request.files[field]
        name = file.filename
        if name:
            path = config['UPLOAD_FOLDER_ANUNCIOS'][1:] + name
            dbpath = config['UPLOAD_FOLDER_ANUNCIOS'] + name
            file.save(path)
            return dbpath
        else:
            return ""

    def check_path(self, anuncio, field, default):
        if (request.files[field].filename != ''):
            return self.gen_path(field)
        else:
            return anuncio[default]

    def new(self):
        if request.method == 'GET':
            fecha_de_hoy = datetime.date(datetime.now())
            return render_template('anuncios/new.html', fecha_de_hoy=fecha_de_hoy)
        elif request.method == 'POST':
            imgpath = self.gen_path('imagen')
            Anuncio.crear(request.form, imgpath)
            return self.index()

    def edit(self):
        if request.method == 'GET':
            anuncio = Anuncio.encontrar_por_id(request.args.get("anuncio_id"))
            return render_template('anuncios/edit.html', anuncio=anuncio)
        elif request.method == 'POST':
            anuncio = Anuncio.encontrar_por_id(request.form["anuncio_id"])
            imgpath = self.check_path(anuncio, 'imagen', 'ruta')
            Anuncio.edit(request.form, imgpath)
            return self.index()

    def eliminar_anuncio(self, id):
        print("hola")
        anuncios = Anuncio.all()
        anuncio = Anuncio.eliminar(id)
        return redirect (url_for("anuncio_index"))


anuncioController = AnuncioController()
