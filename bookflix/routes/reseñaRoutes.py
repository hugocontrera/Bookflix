#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.ReseñaController import reseñaController
from controllers.BookController import bookController
import json

# @app.route("/reseña", methods=["GET"])
# def reseña_index():
# 	return reseñaController.index()

@app.route("/reseña/agregar", methods=["POST", "GET"])
def reseña_new():
	libro_id = (request.args.get('libro_id'))
	return reseñaController.new(libro_id)

@app.route("/reseña/editar", methods=["POST", "GET"])
def reseña_editar():
	reseña_id = (request.args.get('reseña_id'))
	return reseñaController.edit(reseña_id)
	# return reseñaController.editar(libro_id)

@app.route("/reseña/eliminar", methods=["POST", "GET"])
def reseña_eliminar():
	libro_id = (request.args.get('libro_id'))
	reseña_id = (request.args.get('reseña_id'))
	perfil_id = (request.args.get('perfil_id'))
	return reseñaController.delete(libro_id, reseña_id, perfil_id)
	
	# return bookController.libro(libro_id)