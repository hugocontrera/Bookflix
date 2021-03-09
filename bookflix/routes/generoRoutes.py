#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.GeneroController import generoController

@app.route("/genero", methods=["GET"])
def genero_index():
	return generoController.index()

@app.route("/genero/agregar", methods=["POST", "GET"])
def genero_new():
	return generoController.new()

@app.route("/genero/editar", methods=["POST", "GET"])
def genero_edit():
	return generoController.edit()

@app.route("/genero/eliminar/<genero_id>", methods=["POST", "GET"])
def genero_delete(genero_id):
	return generoController.delete(genero_id)