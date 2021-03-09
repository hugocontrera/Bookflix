#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from flask import render_template
from app import app
from controllers.CapituloController import capituloController


@app.route("/libro/<libro_id>/new", methods=["GET"])
def capitulo_upload(libro_id):
    return capituloController.new(libro_id)

@app.route("/libro/<libro_id>/new", methods=["POST"])
def capitulo_upload_file(libro_id):
    return capituloController.new_capitulo(libro_id)

@app.route("/libro/<libro_id>/new_completo", methods=["GET"])
def capitulo_completo(libro_id):
    return capituloController.new_completo(libro_id)

@app.route("/libro/<libro_id>/new_completo", methods=["POST"])
def capitulo_completo_file(libro_id):
    return capituloController.new_completo_capitulo(libro_id)

@app.route("/capitulo/<capitulo_id>", methods=["GET"])
def capitulo(capitulo_id):
    return capituloController.capitulo(capitulo_id)

