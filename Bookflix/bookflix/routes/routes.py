#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from flask import render_template
from app import app
from controllers.UserController import usercontroller


@app.route("/", methods=["GET"])
def index():
    return usercontroller.index()

@app.route("/<perfil_id>", methods=["GET"])
def perfil(perfil_id):
    return usercontroller.index(perfil_id)

@app.route("/panel_de_control", methods=["GET"])
def panel_de_control():
    return usercontroller.panel_de_control()


@app.route("/register", methods=["GET"])
def register():
    return usercontroller.register()


@app.route("/register", methods=["POST"])
def registeruser():
    return usercontroller.registeruser()


@app.route("/login", methods=["GET"])
def login():
    return usercontroller.login()


@app.route("/login", methods=["POST"])
def loginuser():
    return usercontroller.loginuser()


@app.route("/logout", methods=["GET", "POST"])
def logout():
    return usercontroller.logout()

# ruta para ver perfil
@app.route("/ver_perfil/<id>", methods=["GET", "POST"])
def ver_perfil(id):
    return usercontroller.ver_perfil(id)

# ruta ver perfiles
@app.route("/ver_perfiles/<id>", methods=["GET", "POST"])
def ver_perfiles(id):
    return usercontroller.ver_perfiles(id)

# ruta crear un perfil
@app.route("/crear_perfil/<id>", methods=["GET", "POST"])
def crear_perfil(id):
    return usercontroller.crear_perfil(id)

# ruta modificar un perfil
@app.route("/modificar_perfil/<id>", methods=["GET", "POST"])
def modificar_perfil(id):
    return usercontroller.modificar_perfil(id)

# ruta para ver los perfiles a partir de la información de la sesion
@app.route("/ver_perfiles_con_sesion", methods=["GET"])
def ver_perfiles_con_sesion():
    return usercontroller.ver_perfiles_con_sesion()

@app.route("/eliminar_perfil/<id>")
def eliminar_perfil(id):
    return usercontroller.eliminar_perfil(id)

# Ruta para que un usuario pueda visualizar sus detalles de su cuenta
@app.route("/usuario_detalles", methods=["GET"])
def usuario_detalles():
    return usercontroller.usuario_detalles()

@app.route("/ver_anuncio")
def ver_anuncio():
    return usercontroller.ver_anuncio()


# Borrar a futuro
@app.route("/hello/<name>")
def hello(name):
    return usercontroller.hello(name)


@app.route("/user/<id>")
def user_id(id):
    return usercontroller.user_id(id)

@app.route("/modificar_plan", methods=["GET", "POST"])
def modificar_plan():
    return usercontroller.modificar_plan()

@app.route("/cobro_index", methods=["GET"])
def cobro_index():
    return usercontroller.cobrar_usuario()

@app.route("/cobro_all", methods=["GET"])
def cobro_all():
    return usercontroller.cobrar_usuario_all()

@app.route("/modificar_tarjeta", methods=["GET"])
def modificar_tarjeta():
    return usercontroller.modificar_tarjeta()

@app.route("/modificar_tarjeta", methods=["POST"])
def modificar_tarjeta_upload():
    return usercontroller.modificar_tarjeta_upload()

@app.route("/suscripciones", methods=["GET"])
def suscripcionForm():
    return usercontroller.suscripcionForm()

@app.route("/suscripciones", methods=["POST"])
def suscripcionShow():
    return usercontroller.suscripcionShow()
