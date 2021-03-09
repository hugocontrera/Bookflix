from db import get_db
from models.libro import Libro

class Author (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, autor_id):
		sql = "SELECT * FROM autor WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % autor_id)
		return cursor.fetchone()

	@classmethod
	def libros (cls, autor_id):
		sql = "SELECT * FROM libro WHERE autor = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % autor_id)
		return cursor.fetchall()

	@classmethod
	def existe(cls, name):
		sql = "SELECT * FROM autor WHERE nombre = '%s'"
		cursor = cls.database().cursor()
		cursor.execute(sql % name)
		return not (cursor.fetchone() is None)

	@classmethod
	def all(cls):
		sql = "SELECT * FROM autor"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def all_active(cls):
		sql = "SELECT * FROM autor WHERE activo = 1"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def edit (cls, autor_id, name):
		sql = "UPDATE autor SET nombre = '%s' WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (name, autor_id))
		cls.database().commit()
		return True

	@classmethod
	def crear(cls, name):
		sql = "INSERT INTO autor (nombre) VALUES ('%s')"
		cursor = cls.database().cursor()
		cursor.execute(sql % name)
		cls.database().commit()
		return True

	@classmethod
	def habilitar(cls, autor_id):
		sql = "UPDATE autor SET activo = 1 WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, autor_id)
		cls.database().commit()
		return True

	@classmethod
	def deshabilitar(cls, autor_id):
		sql = "UPDATE autor SET activo = 0 WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, autor_id)
		cls.database().commit()
		return True

