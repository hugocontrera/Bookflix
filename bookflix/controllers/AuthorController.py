from flask import request, render_template, session, abort, redirect
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse
from controllers.AbstractController import AbstractController
from models.autor import Author
from models.libro import Libro
from models.genero import Genero
from config import config

class AuthorController(AbstractController):

	def __init__(self):
		pass

	def index(self):
		autores = Author.all()
		return render_template('autores/index.html', autores=autores)

	def autor (self, autor_id):
		autor = Author.id (autor_id)
		libros = Author.libros(autor_id)
		data = []
		for libro in libros:
			autor = Author.id(libro["autor"])
			genero = Genero.encontrar_por_id(libro["genero"])
			data.append({"libro": libro, "autor": autor, "genero": genero})
		return render_template('autores/show.html', autor=autor, libros = data)

	@AbstractController.validate
	def create (self, errores = []):#formulario
		return render_template ('autores/agregar.html', errores=errores)

	@AbstractController.validate
	def create_author (self):
		name = request.form.get('nombre', '')
		if Author.existe (name):#chequear que no existe
			return self.create (["Ya existe un autor con ese nombre"])
		Author.crear (name)
		return self.index()

	@AbstractController.validate
	def edit (self, autor_id):#formulario
		return render_template('autores/editar.html')

	@AbstractController.validate
	def edit_author (self, autor_id):
		autor = Author.id (autor_id)
		name = request.form.get('nombre', '')
		if name != autor["nombre"] and Author.existe (name):#chequear que no existe
			return self.create (["Ya existe un autor con ese nombre"])
		else:
			Author.edit (autor_id, name)
			return self.index()

	@AbstractController.validate
	def habilitar(self, autor_id):
		Author.habilitar(autor_id)
		return redirect (url_for("autor_index"))

	@AbstractController.validate
	def deshabilitar(self, autor_id):
		Author.deshabilitar(autor_id)
		return redirect (url_for("autor_index"))

authorController = AuthorController()

