from datetime import datetime

from flask import request, render_template, session, redirect, url_for, flash
# from app.models.AuthModel import authmodel
# from app.helpers.Utility import sendResponse
from models.usuario import Usuario
from models.plan import Plan
from models.perfiles import Perfiles
from models.libro import Libro
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Author
from models.anuncio import Anuncio


class UserController():

    def __init__(self):
        pass

    def index(self, perfil_id=None):
        if perfil_id != None:
            try:
                int(perfil_id)
                session["perfil_id"] = perfil_id
            except:
                pass
        libros = Libro.all()
        editoriales = Editorial.all()
        generos = Genero.all()
        autores = Author.all()
        cant = 0
        mostrar = []
        for libro in libros:
            if cant < 6:
                mostrar.append(libro)
            cant = cant + 1

        return render_template('index.html', libros=mostrar, editoriales=editoriales, generos=generos, autores=autores)

    def panel_de_control(self):
        return render_template('panel_de_control.html')

    def cobrar_usuario (self):
        usuarios = Usuario.all()
        return render_template('usuarios/cobros.html', usuarios=usuarios)

    def cobrar_usuario_all (self):
        Usuario.cobrar_all()
        return redirect (url_for("cobro_index"))

    def modificar_tarjeta (self, errores=[]):
        user_id = session["id"]
        usuario = Usuario.encontrar_por_id (user_id)
        return render_template('usuarios/modificar_tarjeta.html', errores=errores, usuario=usuario)

    def modificar_tarjeta_upload (self):
        errores = []
        user_id = session["id"]
        hoy = datetime.today()
        tarjetaNumero = request.form["tarjetaNumero"]
        tarjetaPin = request.form["tarjetaPin"]
        tarjetaFechaDeExpiracion = datetime.strptime(request.form["tarjetaFechaDeExpiracion"], "%Y-%m-%d")
        tarjetaNumero_valido = len(tarjetaNumero) != 16 and  tarjetaNumero[-1] != 5
        tarjetaPin_valido = len(tarjetaPin) != 3
        if (hoy >= tarjetaFechaDeExpiracion) or tarjetaNumero_valido or tarjetaPin_valido:
            errores.append(
                'Los datos proporcionados acerca la tarjeta de crédito no son válidos.')
        if errores:
            return self.modificar_tarjeta (errores)
        else:
            Usuario.modificar_tarjeta (user_id, tarjetaNumero, tarjetaPin, tarjetaFechaDeExpiracion)
            return redirect (url_for("ver_perfiles", id=session['id']))

    def register(self):
        planes = Plan.all()
        return render_template('registrar.html', planes=planes)

    def registeruser(self):
        # _firstname = request.form.get('firstname', '')
        # _lastname = request.form.get('lastname', '')
        # _email = request.form.get('email', '')
        # _password = request.form.get('password', '')
        # return sendResponse(authmodel.registerUser(_firstname,_lastname,_email,_password))

        errores = []

        email = request.form["email"]
        if Usuario.existe_usuario_con_email(email):
            errores.append(
                'El email ya esta en uso, por favor seleccione otro.')

        contraseña = request.form["password"]
        # https://kite.com/python/answers/how-to-check-if-a-string-contains-letters-in-python
        tiene_letras = contraseña.lower().islower()
        # https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
        tiene_numeros = '0' in contraseña or '1' in contraseña or '2' in contraseña or '3' in contraseña or '4' in contraseña or '5' in contraseña or '6' in contraseña or '7' in contraseña or '8' in contraseña or '9' in contraseña
        tiene_simbolos = "'" in contraseña or '¿' in contraseña or '?' in contraseña or '¡' in contraseña or '!' in contraseña or '#' in contraseña or '@' in contraseña or '.' in contraseña or '-' in contraseña or '_' in contraseña
        longitud_de_caracteres_valido = (contraseña.__len__() >= 8)
        contraseña_valida = tiene_letras and tiene_numeros and tiene_simbolos and longitud_de_caracteres_valido

        if not contraseña_valida:
            errores.append(
                'Contraseña inválida.')

        # El número de la tarjeta tiene que ser de 16 digitos
        # El pin de la tiene que ser de 3 digitos
        tarjetaNumero_valido = (request.form["tarjetaNumero"].__len__() != 16)
        tarjetaPin_valido = (request.form["tarjetaPin"].__len__() != 3)

        # https://learnandlearn.com/python-programming/python-reference/python-get-current-date
        # Pregunto si la fecha de expiración ingresada para la tarjeta es mayor al día de hoy ...
        # ... con esto compruebo si es válida o no.
        feha_de_hoy = datetime.today()
        tarjetaFechaDeExpiracion = datetime.strptime(
            request.form["tarjetaFechaDeExpiracion"], "%Y-%m-%d")
        if (feha_de_hoy >= tarjetaFechaDeExpiracion) or tarjetaNumero_valido or tarjetaPin_valido:
            errores.append(
                'Los datos proporcionados acerca la tarjeta de crédito no son válidos.')

        if errores:
            # Solo entra aca si el arreglo tiene elementos, osea que hay errores.
            planes = Plan.all()
            usuario = request.form
            return render_template('registrar.html', planes=planes, errores=errores, usuario=usuario)
        else:
            # Solo entra aca si el arreglo esta vacio, esto significa que no hay ...
            # ... errores y el registro se realiza de forma exitosa.
            usuario = Usuario.crear(request.form)
            mensaje_de_exito = "Enhorabuena, ¡Su usuario fue creado con exito!"
            return render_template("login.html", mensaje_de_exito=mensaje_de_exito)

    # Login GET
    def login(self):
        return render_template("login.html")

    # Login POST
    def loginuser(self):
        errores = []

        # Me fijo si existe el usuario ingresado y luego pregunto si la contraseña ingresada es correcta
        usuario = Usuario.encontrar_por_email(request.form["email"])
        perfiles = Perfiles.all()
        if usuario:
            # Luego de saber que el usuario buscado existe, pregunto si la contraseña es correcta
            if (usuario["contraseña"] != request.form["password"]):
                errores.append("Los datos ingresados son incorrectos.")
                return render_template("login.html", errores=errores)

            session["id"] = usuario["id"]

            # session["perfil_id"] = request.form["perfil_id"] TODAVÍA NO HICIMOS NADA ACERCA DE LOS PERFILES
            session["admin"] = (usuario["email"] == "admin@gmail.com")
            # se conecta a perfiles

            if session["admin"]:
                return render_template('panel_de_control.html')
            elif not usuario["tarjeta_valida"]:
                return redirect (url_for("modificar_tarjeta"))
            else:
                return redirect (url_for("ver_perfiles", id=session['id']))
        else:
            errores.append("No existe ninguna cuenta con el email ingresado.")
            return render_template("login.html", errores=errores)

    def logout(self):
        session.pop("id", None)
        session.pop("admin", None)
        session.pop("perfil_id", None)
        return self.index()

    def hello(self, name):
        saludo = "!Hola " + name + "!"
        return "<h1>" + saludo + "</h1>"

    def user_id(self, id):
        user = Usuario.encontrar_por_id(id)
        if user:
            return render_template("/usuarios/read.html", usuario=user)
        else:
            return "<h1> No existe ningun usuario con esa id</h1>"

    # ver perfil de usuario sus datos
    def ver_perfil(self, id):
        user = Usuario.encontrar_por_id(id)
        if user:
            return render_template("/usuarios/perfil.html", usuario=user)
        else:
            return "<h1> No existe ningun usuario con esa id</h1>"

    # ver perfiles de usuario
    def ver_perfiles(self, id):
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.user_id(id)
        plan = Plan.encontrar_por_id (user["plan_id"])

        return render_template("/usuarios/perfiles.html", perfiles=perfiles, usuario=user, plan=plan)

    # crear un perfil funciona falta redireccionar a la pagina ver_perfil
    def crear_perfil(self, id):
        errores = []
        p = []
        user = Usuario.encontrar_por_id(id)
        perfiles = Perfiles.all()
        planes = Plan.all()
        contador = 0
        ok = False
        if user['plan_id'] == 2:
            for perfil in perfiles:  # cuento cuantos perfiles tengo y los guardo en otro arreglo
                if perfil['id_usuario'] == user['id']:
                    contador = contador + 1
                    p.append(perfil)
            print(p)
            if contador < 4:
                if request.method == 'POST':
                    for per in p:
                        if per['nombre'] == request.form["nombre"]:
                            ok = True
                    if ok == True:
                        errores.append(
                            "Ya existe un perfil con el nombre especificado.")

                    else:
                        foto = request.form['foto']
                        nombre = request.form['nombre']
                        Perfiles.crear(dict
                                       ([('nombre', nombre), ('foto', foto), ('id_usuario', id)]))
                        return redirect(url_for('ver_perfiles', id=session['id']))
            else:

                flash('Ya no puede agregar mas contactos!!!!!')
            return render_template("/usuarios/crearPerfil.html", usuario=user, errores=errores)
            # return redirect(url_for('ver_perfiles', id=session['id'], errores=errores))
        else:
            if user['plan_id'] == 1:
                for perfil in perfiles:
                    if perfil['id_usuario'] == user['id']:
                        contador = contador + 1
                        p.append(perfil)

            if contador < 2:
                if request.method == 'POST':
                    for per in p:
                        if per['nombre'] == request.form["nombre"]:
                            ok = True
                    if ok == True:
                        errores.append(
                            "Ya existe un perfil con el nombre especificado.")

                    else:
                        foto = request.form['foto']
                        nombre = request.form['nombre']
                        Perfiles.crear(dict
                                       ([('nombre', nombre), ('foto', foto), ('id_usuario', id)]))
                        return redirect(url_for('ver_perfiles', id=session['id']))
            else:

                flash('Ya no puede agregar mas contactos!!!!!')

            return render_template("/usuarios/crearPerfil.html", p=p, usuario=user, errores=errores)

    # modificar un perfil
    def modificar_perfil(self, id_perfil):
        errores = []
        arreglo = []
        perfil = Perfiles.encontrar_por_id(id_perfil)
        user = Usuario.encontrar_por_id(session['id'])
        ok = False
        perfiles = Perfiles.all()
        for p in perfiles:
            if p['id_usuario'] == user['id']:
                arreglo.append(p)
        if request.method == 'GET':
            return render_template("/usuarios/modificarPerfil.html", perfil=perfil, usuario=user, errores=errores)

        else:
            if request.method == 'POST':
                for a in arreglo:
                    if a['nombre'] == request.form['nombre']:
                        ok = True
                if ok == True:
                    errores.append("ya existe el nombre especificado.")
                    nombre = request.form['nombre']
                    return render_template("/usuarios/modificarPerfil.html", perfil=perfil, usuario=user, errores=errores, nombre=nombre)
                else:
                    nombre = request.form['nombre']
                    foto = request.form['foto']
                    Perfiles.edit(nombre, foto, id_perfil)
                    return redirect(url_for('ver_perfiles', id=session['id']))

    # eliminar perfil

    def eliminar_perfil(self, id_perfil):
        print("el id perfil es", id_perfil)
        perfiles = Perfiles.encontrar_por_id(id_perfil)
        Perfiles.eliminar(id_perfil)
        return redirect(url_for('ver_perfiles', id=session['id']))

    def ver_anuncio(self):
        anuncios = Anuncio.all()
        return render_template("usuarios/anuncios.html", anuncios=anuncios)

    # ver perfil de usuario sus datos
    def ver_perfiles_con_sesion(self):
        return redirect(url_for('ver_perfiles', id=session['id']))

    # ver perfil de usuario sus datos
    def usuario_detalles(self):
        usuario = Usuario.encontrar_por_id(session['id'])
        perfiles_creados = Usuario.cantidad_de_perfiles_creados_por_el_usuario_con_id(
            session['id'])
        plan = Plan.encontrar_por_id(usuario['plan_id'])
        return render_template('usuarios/detalles.html', usuario=usuario, plan=plan, perfiles_creados=perfiles_creados)

    # Ruta para poder visualizar el formulario de cambio de plan de un usuario
    def modificar_plan(self):
        if request.method == 'GET':
            planes = Plan.all()
            usuario = Usuario.encontrar_por_id(session['id'])
            plan_del_usuario = Plan.encontrar_por_id(usuario['plan_id'])
            return render_template('usuarios/modificar_plan.html', planes=planes, id_plan_del_usuario=plan_del_usuario['id'])

        elif request.method == 'POST':
            errores = []
            cantidad_perfiles_del_usuario = Plan.numero_de_perfiles_del_usuario_con_id(
                session['id'])['COUNT(*)']
            plan_nuevo = Plan.encontrar_por_id(request.form['plan_id'])

            if (plan_nuevo['perfiles_max'] >= cantidad_perfiles_del_usuario):
                # Solo entra aca cuando el usuario puede cambiar de plan
                Usuario.modificar_plan_id(session['id'], plan_nuevo['id'])

                usuario = Usuario.encontrar_por_id(session['id'])
                perfiles_creados = Usuario.cantidad_de_perfiles_creados_por_el_usuario_con_id(
                    session['id'])
                plan = Plan.encontrar_por_id(usuario['plan_id'])
                mensaje_de_exito = "Enhorabuena, ¡Su plan fue actualizado con exito!"
                return render_template('usuarios/detalles.html', usuario=usuario, plan=plan, perfiles_creados=perfiles_creados, mensaje_de_exito=mensaje_de_exito)
            else:
                # Solo entra aca cuando el usuario tiene más perfiles creados de los que permite el plan nuevo.
                # Por lo tanto no se puede cambiar el plan
                planes = Plan.all()
                usuario = Usuario.encontrar_por_id(session['id'])
                plan_del_usuario = Plan.encontrar_por_id(usuario['plan_id'])

                perfiles_a_borrar = abs(
                    plan_nuevo['perfiles_max'] - cantidad_perfiles_del_usuario)
                errores.append("El usuario actual excede la cantidad maxima de perfiles permitidos, debera borrar " +
                               str(perfiles_a_borrar) + " perfil/es para poder realizar el cambio.")
                return render_template('usuarios/modificar_plan.html', planes=planes, id_plan_del_usuario=plan_del_usuario['id'], errores=errores)

    def suscripcionForm(self):
        return render_template('usuarios/suscripcionesForm.html')

    def suscripcionShow(self):
        m = {
            '1': 'Enero',
            '2': 'Febrero',
            '3': 'Marzo',
            '4': 'Abril',
            '5': 'Mayo',
            '6': 'Junio',
            '7': 'Julio',
            '8': 'Agosto',
            '9': 'Septiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre'
        }

        año = request.form['año']
        mes = request.form['mes']
        mes_string = m[str(mes)]
        usuarios = Usuario.suscripciones_dado_año_y_mes(año, mes)
        usuarios_cantidad = len(Usuario.suscripciones_dado_año_y_mes(año, mes))
        return render_template(
            'usuarios/suscripcionesShow.html',
            año=año,
            mes=mes_string,
            usuarios=usuarios,
            usuarios_cantidad=usuarios_cantidad
        )

usercontroller = UserController()
