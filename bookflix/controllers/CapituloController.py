from flask import request, render_template, session, redirect
from flask import send_file, send_from_directory, url_for
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.libro import Libro
from models.capitulo import Capitulo
from controllers.BookController import bookController
from config import config
from datetime import datetime
import os


class CapituloController(AbstractController):

	def capitulo (self, capitulo_id):
		capitulo = Capitulo.id(capitulo_id)
		libro_id = capitulo["libro_id"]
		if "perfil_id" in session:
			perfil_id = session["perfil_id"]
			print ("perfil: ", perfil_id, "leyendo: ", capitulo_id)
			Libro.update_leyendo (libro_id, capitulo_id, perfil_id)
		else:
			print ("no hay perfil en session")
		return send_file(capitulo["ruta"][3:])

	@AbstractController.validate
	def new(self, libro_id, errores=[]):
		return render_template('capitulos/agregar.html', errores=errores)

	@AbstractController.validate
	def new_capitulo(self, libro_id):
		errores = self.upload(libro_id)
		if (len(errores) == 0):
			return redirect (url_for("libro", libro_id=libro_id))
		else:
			return self.new (libro_id, errores)

	@AbstractController.validate
	def new_completo(self, libro_id, errores=[]):
		return render_template('capitulos/unico.html', errores=errores)

	@AbstractController.validate
	def new_completo_capitulo(self, libro_id):
		libro = Libro.id (libro_id)
		pdfpath = self.gen_path('archivo')
		Capitulo.crear(libro_id, libro["fecha_publicacion"], pdfpath)
		Libro.completo(libro_id)
		return redirect (url_for("libro", libro_id=libro_id))

	def gen_path(self, field):
		file = request.files[field]
		name = file.filename
		path = config['UPLOAD_FOLDER'][1:] + name
		dbpath = config['UPLOAD_FOLDER'] + name
		file.save(path)
		return dbpath

	@AbstractController.validate
	def upload(self, libro_id):
		libro = Libro.id (libro_id)
		pdate = datetime.strptime(request.form["fechaPublicacion"], "%Y-%m-%d")
		errores = []
		if pdate.date() < libro["fecha_publicacion"]:
			errores.append("La fecha de publicación no puede ser anterior a la del libro ", libro["fecha_publicacion"])
		if "fechaVencimiento" in request.form and request.form["fechaVencimiento"]:
			vdate = datetime.strptime(request.form["fechaVencimiento"], "%Y-%m-%d")
			if libro["fecha_vencimiento"][0] != '0':
				lvdate = datetime.strptime(libro["fecha_vencimiento"], "%Y-%m-%d")
			else:
				lvdate = None
			if lvdate and vdate.date() > lvdate.date():
				errores.append("Fecha de vencimiento ingresada es mayor que la fecha de vencimiento del libro")
			elif vdate.date() < pdate.date():
				errores.append("Fecha de vencimiento ingresada es menor que la fecha de publicación")
		else:
			vdate = None
		if (len(errores) == 0):
			pdfpath = self.gen_path('archivo')
			Capitulo.crear(libro_id, pdate, pdfpath)
		return errores #redirect (url_for("libro", libro_id=libro_id))

capituloController = CapituloController()
