#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.EditorialController import editorialController

@app.route("/editorial", methods=["GET"])
def editorial_index():
	return editorialController.index()

@app.route("/editorial/agregar", methods=["POST", "GET"])
def editorial_new():
	return editorialController.new()

@app.route("/editorial/editar", methods=["POST", "GET"])
def editorial_edit():
	return editorialController.edit()

@app.route("/editorial/eliminar/<editorial_id>", methods=["POST", "GET"])
def editorial_delete(editorial_id):
	return editorialController.delete(editorial_id)