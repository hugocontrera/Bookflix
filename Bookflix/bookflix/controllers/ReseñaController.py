from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
from models.reseña import Reseña
from controllers.BookController import BookController

class ReseñaController():

	def __init__(self):
		pass

	# Llama al indice de bookRoutes
	def index(self, id_libro):
		return BookController.libro(self, id_libro)

	def new(self, id_libro):
		if request.method == 'GET':
			return render_template ('reseñas/new.html')
		elif request.method == 'POST':
			perfil_id = session['perfil_id']
			calificacion = request.form['calificacion']
			comentario = request.form['comentario']
			# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
			# 0 (for false) or 1 (for true)
			spoiler = 0
			for campo in request.form:
				if campo == "spoiler":
					spoiler = 1

			Reseña.new(perfil_id, id_libro, calificacion, comentario, spoiler)
			return self.index(id_libro)

	def edit(self, reseña_id):
		reseña = Reseña.encontrar_por_id(reseña_id)
		if request.method == 'GET':
			return render_template ('reseñas/edit.html', reseña=reseña)
		elif request.method == 'POST':
			perfil_id = session['perfil_id']
			calificacion = request.form['calificacion']
			comentario = request.form['comentario']
			
			# 0 (for false) or 1 (for true)
			spoiler = 0
			for campo in request.form:
				if campo == "spoiler":
					spoiler = 1
			Reseña.edit(reseña_id, calificacion, comentario, spoiler)
			return self.index(request.form['libro_id'])

	def delete(self, id_libro, reseña_id, perfil_id):
		Reseña.delete(id_libro, reseña_id, perfil_id)
		return self.index(id_libro)

reseñaController = ReseñaController()