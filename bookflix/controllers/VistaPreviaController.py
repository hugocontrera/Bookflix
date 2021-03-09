from datetime import datetime

from flask import request, render_template, session, abort
from flask import send_from_directory, url_for, redirect
from models.vistaPrevia import VistaPrevia
from config import config


class VistaPreviaController():

    def __init__(self):
        pass

    def index(self):
        vistas_previas = VistaPrevia.all()
        return render_template('vistas_previas/index.html', vistas_previas=vistas_previas)

    def new(self):
        errores = []
        fecha_de_hoy = datetime.date(datetime.now())
        if request.method == 'GET':

            return render_template('vistas_previas/new.html', fecha_de_hoy=fecha_de_hoy)
        elif request.method == 'POST':
            formulario = request.form
            # si el pdf lo hago de tipo file en el html no me puedo fijar si esta vacio
            pdfpath = self.gen_path('pdf')
            imgpath = self.gen_path('imagen')
            #print(pdfpath)
            #print(imgpath)
            if formulario['video'] == '' and pdfpath == '':
                errores.append("Es obligatorio agregar un pdf o un video")
                vista = request.form
                return render_template('vistas_previas/new.html', errores=errores, fecha_de_hoy=fecha_de_hoy, vista=vista)
            else:
                VistaPrevia.crear(formulario, pdfpath, imgpath)
                return self.index()

    def delete(self, id):
        mensajes = []
        mensajes.append("Se elimino la vista previa correctamente")
        vista = VistaPrevia.eliminar(id)
        vistas_previas = VistaPrevia.all()
        return render_template('vistas_previas/index.html', vistas_previas=vistas_previas, mensajes=mensajes)
        #no se usa el redirect ppor que tira un error en la terminal
        #return redirect(url_for('vista_previa_index', vistas_previas=vistas_previas, mensajes=mensajes))

    def modificar(self, id):
        vista_previa = VistaPrevia.encontrar_por_id(id)
        errores = []
        if request.method == 'GET':
            return render_template('vistas_previas/edit.html', vista_previa=vista_previa)
        else:
            if request.method == 'POST':

                nombre = request.form['nombre']
                descripcion = request.form['descripcion']
                video = request.form['video']
                pdfpath = self.gen_path('pdf')
                imgpath = self.gen_path('imagen')
                fecha_de_publicacion = request.form['fecha_de_publicacion']
                if video == '' and pdfpath == '':
                    errores.append("Es obligatorio agregar un pdf o un video")
                    return render_template('vistas_previas/edit.html', errores=errores, vista_previa=vista_previa)
                else:

                    VistaPrevia.edit(nombre, descripcion, video,
                                     pdfpath, imgpath, fecha_de_publicacion, id)
                    return self.index()

    def gen_path(self, field):  # pdf y imagen
        file = request.files[field]
        name = file.filename
        if name == '':
            dbpath = ''
            #print("devolvi vacio")
            return dbpath
        else:    
            print("devolvi con datos, el name es")
            print(name)
            path = config['UPLOAD_FOLDER'][1:] + name
            dbpath = config['UPLOAD_FOLDER'] + name
            file.save(path)
            return dbpath
    

vistaPreviaController = VistaPreviaController()
