from db import get_db

class Reseña (object):

	@classmethod
	def database(cls):
		return get_db()

	# Devuelve todas las reseñas
	@classmethod
	def all(cls):
		sql = "SELECT * FROM reseña"

		cursor = cls.database().cursor()
		cursor.execute(sql)

		return cursor.fetchall()

	# https://stackoverflow.com/questions/9387839/mysql-if-not-null-then-display-1-else-display-0
	# https://stackoverflow.com/questions/20840505/show-null-values-that-does-not-match-with-another-table-sql-server
	# Devuelve todas las reseñas junto con nuevos campos que es el id, nombre y foto del que creo la reseña
	# Si alguno de los campos de id, nombre o foto no existen van a mostrar un valor por defecto
	@classmethod
	def reseñas_de_un_libro_con_id(cls, id_libro):
		sql = """
			SELECT IF(p.nombre IS NULL, '-1', p.id) AS perfil_id, IF(p.nombre IS NULL, '[No está disponible]', p.nombre) AS perfil_nombre, IF(p.foto IS NULL, '../../static/img/noavatar.jpg', p.foto) AS perfil_foto, r.*
			FROM reseña AS r
			LEFT JOIN perfiles AS p ON (p.id = r.perfil_id)
            WHERE r.libro_id = %s
		"""

		cursor = cls.database().cursor()
		cursor.execute(sql, (id_libro))

		return cursor.fetchall()

	@classmethod
	def new(cls, perfil_id, id_libro, calificacion, comentario, spoiler):
		sql = """
			INSERT INTO reseña (perfil_id, libro_id, calificacion, comentario, spoiler)
			VALUES (%s, %s, %s, %s, %s)
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (perfil_id, id_libro, calificacion, comentario, spoiler))
		cls.database().commit()
		return True

	@classmethod
	def edit(cls, reseña_id, calificacion, comentario, spoiler):
		sql = """
			UPDATE reseña
			SET calificacion = %s, comentario = %s, spoiler = %s
			WHERE reseña.id = %s
		"""
		
		cursor = cls.database().cursor()
		cursor.execute(sql, (calificacion, comentario, spoiler, reseña_id))
		cls.database().commit()
		return True

	@classmethod
	def delete(cls, libro_id, reseña_id, perfil_id):
		sql = """
			DELETE FROM reseña
			WHERE id = %s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (reseña_id))
		cls.database().commit()
		return True

	@classmethod
	def encontrar_por_id(cls, id_reseña):
		sql = "SELECT * FROM reseña WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (id_reseña))		
		return cursor.fetchone()
