#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask import render_template
from app import app
from controllers.AuthorController import authorController

@app.route("/autor", methods=["GET"])
def autor_index():
	return authorController.index()

@app.route("/autor/create", methods=["GET"])
def autor_create():
	return authorController.create()

@app.route("/autor/create", methods=["POST"])
def autor_create_post():
	return authorController.create_author()

@app.route("/autor/edit/<autor_id>", methods=["GET"])
def autor_edit (autor_id):
	return authorController.edit(autor_id)

@app.route("/autor/edit/<autor_id>", methods=["POST"])
def autor_edit_post (autor_id):
	return authorController.edit_author(autor_id)

@app.route("/autor/<autor_id>", methods=["GET"])
def autor (autor_id):
	return authorController.autor(autor_id)

@app.route("/autor/habilitar/<autor_id>", methods=["GET"])
def autor_habilitar(autor_id):
    return authorController.habilitar(autor_id)

@app.route("/autor/deshabilitar/<autor_id>", methods=["GET"])
def autor_deshabilitar(autor_id):
    return authorController.deshabilitar(autor_id)

