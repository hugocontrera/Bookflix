from db import get_db


class Genero (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM genero"

		cursor = cls.database().cursor()
		cursor.execute(sql)

		return cursor.fetchall()

	@classmethod
	def crear(cls, nombre):
		sql = """INSERT INTO genero (nombre) VALUES (%s)"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre.lower()))
		cls.database().commit()
		return True

	@classmethod
	def encontrar_por_id(cls, id):
		sql = "SELECT * FROM genero WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (id))
		return cursor.fetchone()

	@classmethod
	def existe_genero_con_nombre(cls, nombre):
		sql = """
		SELECT *
		FROM genero g
		WHERE g.nombre = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre))

		return cursor.rowcount > 0

	@classmethod
	def edit(cls, nombre, id):
		sql = """
			UPDATE genero
			SET nombre = %s
			WHERE genero.id = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (nombre.lower(), id))
		cls.database().commit()
		return True

	@classmethod
	def eliminar(cls, genero_id):
		sql = """ DELETE FROM genero WHERE id = %s"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (str(genero_id)))
		cls.database().commit()
		return True
