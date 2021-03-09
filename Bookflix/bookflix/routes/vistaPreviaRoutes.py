#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from flask import render_template
from app import app
from controllers.VistaPreviaController import vistaPreviaController


@app.route("/vista_previa", methods=["GET"])
def vista_previa_index():
    return vistaPreviaController.index()


@app.route("/vista_previa/agregar", methods=["POST", "GET"])
def vista_previa_new():
    return vistaPreviaController.new()

@app.route("/vista_previa/eliminar/<id>", methods=["POST", "GET"])
def vista_previa_eliminar(id):
    return vistaPreviaController.delete(id)

# ruta modificar vista previa
@app.route("/vista_previa/modificar/<id>", methods=["GET", "POST"])
def vista_previa_modificar(id):
    return vistaPreviaController.modificar(id)