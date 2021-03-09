from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
from models.editorial import Editorial


class EditorialController():

	def __init__(self):
		pass

	def index(self):
		editoriales = Editorial.all()
		return render_template('editoriales/index.html', editoriales=editoriales)

	def new(self):
		errores = []
		if request.method == 'GET':
			return render_template('editoriales/new.html')
		elif request.method == 'POST':
			if Editorial.existe_editorial_con_nombre(request.form["nombre"]):
				errores.append("Ya existe una editorial con el nombre especificado.")
				return render_template('editoriales/new.html', errores=errores)
			else:
				Editorial.crear(request.form["nombre"])
				return self.index()

	def edit(self):
		errores = []
		if request.method == 'GET':
			editorial = Editorial.encontrar_por_id(request.args.get("editorial_id"))
			return render_template('editoriales/edit.html', editorial=editorial)
		elif request.method == 'POST':
			if Editorial.existe_editorial_con_nombre(request.form["nombre"]):
				editorial = Editorial.encontrar_por_id(request.args.get("editorial_id"))
				errores.append("Ya existe una editorial con el nombre especificado.")
				return render_template('editoriales/edit.html', editorial=editorial, errores=errores)
			else:
				Editorial.edit(request.form["nombre"], request.form["id"])
				return self.index()
	
	def delete(self, editorial_id):
		errores = []
		errores.append("Se elimino la editorial correctamente")
		editorial = Editorial.eliminar(editorial_id)
		editoriales = Editorial.all()
		return render_template('editoriales/index.html', editoriales=editoriales, errores=errores)
		
editorialController = EditorialController()
