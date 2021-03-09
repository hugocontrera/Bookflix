#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from flask import render_template
from app import app
from controllers.AnuncioController import anuncioController


@app.route("/anuncio", methods=["GET"])
def anuncio_index():
    return anuncioController.index()


@app.route("/anuncio/agregar", methods=["POST", "GET"])
def anuncio_new():
    return anuncioController.new()


@app.route("/anuncio/editar", methods=["POST", "GET"])
def anuncio_edit():
    return anuncioController.edit()


@app.route("/eliminar_anuncio/<string:id>", methods=["POST", "GET"])
def eliminar_anuncio(id):
    return anuncioController.eliminar_anuncio(id)
