from flask import request, render_template, session, abort
from flask import send_from_directory, url_for
#from app.models.AuthModel import authmodel
#from app.helpers.Utility import sendResponse

class AbstractController():

	def validate (func):
		def val (*args, **kwargs):
			if "admin" in session and session["admin"]:
				return func (*args, **kwargs)
			else:
				abort(401)
		return val


