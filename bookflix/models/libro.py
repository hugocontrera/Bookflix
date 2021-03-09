from db import get_db
from datetime import datetime
from models.capitulo import Capitulo

class Libro (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def completo (cls, libro_id):
		sql = "UPDATE libro SET completo = 1 WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % libro_id)
		cls.database().commit()
		return True

	@classmethod
	def all_leidos (cls, perfil_id):
		sql = """
			SELECT l.*
			FROM leido AS r
			INNER JOIN libro AS l ON l.id = r.libro_id
			WHERE r.perfil_id = %s

			UNION

			SELECT l.*
			FROM leyendo AS r
			INNER JOIN libro AS l ON l.id = r.libro_id
			WHERE r.perfil_id = %s AND l.activo=0
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (perfil_id, perfil_id))
		return cursor.fetchall()

	@classmethod
	def all_leyendo (cls, perfil_id):
		#sql = "SELECT libro_id FROM leyendo WHERE perfil_id = %s"
		sql = "SELECT l.* FROM leyendo AS r, libro AS l WHERE r.perfil_id = %s AND l.id = r.libro_id"
		cursor = cls.database().cursor()
		cursor.execute(sql % perfil_id)
		return cursor.fetchall()

	@classmethod
	def leyendo(cls, libro_id, perfil_id):
		sql = "SELECT * FROM leyendo WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		return cursor.fetchone()

	@classmethod
	def all_favorito (cls, perfil_id):
		sql = "SELECT l.* FROM favorito AS r, libro AS l WHERE r.perfil_id = %s AND l.id = r.libro_id"
		cursor = cls.database().cursor()
		cursor.execute(sql % perfil_id)
		return cursor.fetchall()

	@classmethod
	def favorito(cls, libro_id, perfil_id):
		sql = "SELECT * FROM favorito WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		return cursor.fetchone()

	@classmethod
	def agregar_favorito (cls, libro_id, perfil_id):
		sql = "INSERT INTO favorito (libro_id, perfil_id) VALUES ('%s', '%s')"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		cls.database().commit()
		return True

	@classmethod
	def eliminar_favorito (cls, libro_id, perfil_id):
		sql = "DELETE FROM favorito WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		cls.database().commit()
		return True

	@classmethod
	def update_leyendo (cls, libro_id, capitulo_id, perfil_id):
		leyendo = cls.leyendo (libro_id, perfil_id)
		if (leyendo):
			sql = "UPDATE leyendo SET capitulo_id = %s WHERE id = %s"
			sql %= (capitulo_id, leyendo["id"])
		else:
			leido = cls.leido (libro_id, perfil_id)
			if (leido):
				return False
			sql = "INSERT INTO leyendo (libro_id, capitulo_id, perfil_id) VALUES ('%s', '%s', '%s')"
			sql %= (libro_id, capitulo_id, perfil_id)
		cursor = cls.database().cursor()
		cursor.execute(sql)
		cls.database().commit()
		return True

	@classmethod
	def eliminar_leyendo (cls, libro_id, perfil_id):
		sql = "DELETE FROM leyendo WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (libro_id, perfil_id))
		cls.database().commit()
		return True

	@classmethod
	def leido (cls, libro_id, perfil_id):
		sql = "SELECT * FROM leido WHERE libro_id = %s AND perfil_id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % (libro_id, perfil_id))
		return cursor.fetchone()

	@classmethod
	def update_leido (cls, libro_id, perfil_id):
		leido = cls.leido (libro_id, perfil_id)
		if (leido == None):
			cls.eliminar_leyendo (libro_id, perfil_id)
			sql = "INSERT INTO leido (libro_id, perfil_id) VALUES ('%s', '%s')"
			sql %= (libro_id, perfil_id)
			cursor = cls.database().cursor()
			cursor.execute(sql)
			cls.database().commit()
		return True

	@classmethod
	def search (cls, sql):
		cursor = cls.database().cursor()
		cursor.execute(sql)
		libros = cursor.fetchall()
		return libros

	@classmethod
	def search_autor(cls, name):
		sql = "SELECT * FROM autor AS a, libro AS l WHERE a.nombre LIKE '%%%s%%' AND l.autor = a.id"
		return cls.search (sql % name)

	@classmethod
	def search_name(cls, name):
		sql = "SELECT * FROM libro WHERE nombre LIKE '%%%s%%'"
		return cls.search (sql % name)

	@classmethod
	def search_editorial(cls, name):
		sql = "SELECT * FROM editorial AS e, libro AS l WHERE e.nombre LIKE '%%%s%%' AND l.editorial = e.id"
		return cls.search (sql % name)

	@classmethod
	def search_genero(cls, name):
		sql = "SELECT * FROM genero AS g, libro AS l WHERE g.nombre LIKE '%%%s%%' AND l.genero = g.id"
		return cls.search (sql % name)

	@classmethod
	def id(cls, libro_id):
		sql = "SELECT * FROM libro WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql % libro_id)
		libro = cursor.fetchone()
		libro["capitulos"] = Capitulo.libro(libro["id"])
		return libro

	@classmethod
	def isbn (cls, isbn):
		sql = "SELECT * FROM libro WHERE isbn = '%s'"
		cursor = cls.database().cursor()
		cursor.execute(sql % isbn)
		return cursor.fetchone()

	@classmethod
	def existe_isbn (cls, isbn):
		return not (cls.isbn(isbn) is None)

	@classmethod
	def all(cls):
		sql = "SELECT * FROM libro"
		cursor = cls.database().cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def commit (cls, form, sql, imgpath, extra = tuple()):
		name = form.get('nombre', '')
		isbn = form.get('isbn', '')
		pdate = datetime.strptime(form["fechaPublicacion"], "%Y-%m-%d")
		if form["fechaVencimiento"]:
			vdate = datetime.strptime(form["fechaVencimiento"], "%Y-%m-%d")
		else:
			vdate = None
		sinopsis = form.get('sinopsis', '')
		editorial = form.get('editorial', '')
		genero = form.get('genero', '')
		autor = form.get('autor', '')
		cursor = cls.database().cursor()
		cursor.execute(sql % ((name, isbn, pdate, vdate, imgpath, sinopsis, editorial, genero, autor) + extra))
		cls.database().commit()

	@classmethod
	def crear(cls, form, imgpath):
		sql = """INSERT INTO
		libro (nombre, isbn, fecha_publicacion, fecha_vencimiento, ruta_img, sinopsis, editorial, genero, autor)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
		cls.commit (form, sql, imgpath)
		return True

	@classmethod
	def edit(cls, form, imgpath, libro_id):
		sql = """
		UPDATE libro SET
		nombre = '%s',
		isbn = '%s',
		fecha_publicacion = '%s',
		fecha_vencimiento = '%s',
		ruta_img = '%s',
		sinopsis = '%s',
		editorial = '%s',
		genero = '%s',
		autor = '%s'
		WHERE id = '%s'
		"""
		cls.commit (form, sql, imgpath, (libro_id,))
		return True

	@classmethod
	def habilitar(cls, libro_id):
		sql = "UPDATE libro SET activo = 1 WHERE libro.id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (libro_id))
		cls.database().commit()
		return True

	@classmethod
	def deshabilitar(cls, libro_id):
		sql = "UPDATE libro SET activo = 0 WHERE libro.id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (libro_id))
		cls.database().commit()
		return True

	@classmethod
	def el_perfil_dio_una_reseña_al_libro(cls, id_perfil, id_libro):
		sql = """
			SELECT l.*
			FROM libro AS l
			INNER JOIN reseña AS r ON r.libro_id = l.id
			INNER JOIN perfiles AS p ON r.perfil_id = p.id
			WHERE p.id=%s AND l.id=%s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (id_perfil, id_libro))

		return cursor.rowcount > 0

	@classmethod
	def el_perfil_leyo_el_libro(cls, id_perfil, id_libro):
		sql = """
			SELECT l.*
			FROM libro AS l
			INNER JOIN leido AS lei ON l.id = lei.libro_id
			INNER JOIN perfiles AS p ON lei.perfil_id = p.id
			WHERE p.id=%s AND l.id=%s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (id_perfil, id_libro))

		return cursor.rowcount > 0

	@classmethod
	def librosLecturas(cls):
		sql = """
			SELECT t1.*, IF(t2.lecturas IS NULL, 0, t2.lecturas) as 'lecturas'
			FROM 
				(SELECT * FROM libro) t1
			LEFT JOIN
				(SELECT COUNT(*) AS 'lecturas', libro_id FROM leido GROUP BY libro_id) t2
			ON (t1.id = t2.libro_id)
			ORDER BY lecturas DESC
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql)
		cls.database().commit()
		return cursor.fetchall()

	@classmethod
	def obtenerCantidadDeReseñasDeUnLibro(cls, id_libro):
		sql = """
			SELECT COUNT(*) as cantidad
			FROM libro as l
			INNER JOIN reseña as r WHERE l.id = r.libro_id AND l.id=%s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (id_libro))
		cls.database().commit()
		return cursor.fetchall()

	@classmethod
	def obtenerCalificacionTotalDeUnLibro(cls, id_libro):
		sql = """
			SELECT SUM(r.calificacion) as total
			FROM libro as l
			INNER JOIN reseña as r WHERE l.id = r.libro_id AND l.id=%s
		"""
		cursor = cls.database().cursor()
		cursor.execute(sql, (id_libro))
		cls.database().commit()
		return cursor.fetchall()