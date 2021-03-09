from db import get_db
from datetime import datetime


class Editorial (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def id(cls, editorial_id):
		sql = "SELECT * FROM editorial WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % editorial_id)
		return cursor.fetchone()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM editorial"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def crear(cls, nombre):
		sql = """INSERT INTO editorial (nombre) VALUES (%s)"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre.lower()))
		cls.database().commit()
		return True

	@classmethod
	def encontrar_por_id(cls, id):
		sql = "SELECT * FROM editorial WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (id))
		return cursor.fetchone()

	@classmethod
	def existe_editorial_con_nombre(cls, nombre):
		sql = """
		SELECT *
		FROM editorial e
		WHERE e.nombre = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre))

		return cursor.rowcount > 0

	@classmethod
	def edit(cls, nombre, id):
		sql = """
			UPDATE editorial
			SET nombre = %s
			WHERE editorial.id = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre.lower(), id))
		cls.database().commit()
		return True
		
	@classmethod
	def eliminar(cls, editorial_id):
		sql = """ DELETE FROM editorial WHERE id = %s"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (str(editorial_id)))
		cls.database().commit()
		return True
