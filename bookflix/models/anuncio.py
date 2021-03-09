from db import get_db


class Anuncio (object):

    @classmethod
    def database(cls):
        return get_db()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM anuncio"

        cursor = cls.database().cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def crear(cls, data, imgpath):
        sql = """INSERT INTO
		anuncio (titulo, contenido, fecha_de_publicacion, ruta)
		VALUES ('%s', '%s', '%s', '%s')"""

        titulo = data.get('titulo', '')
        contenido = data.get('contenido', '')
        fecha_de_publicacion = data.get('fecha_de_publicacion', '')

        cursor = cls.database().cursor()
        cursor.execute(
            sql % (titulo, contenido, fecha_de_publicacion, imgpath))
        cls.database().commit()
        return True

    @classmethod
    def encontrar_por_id(cls, id):
        sql = "SELECT * FROM anuncio WHERE id = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def edit(cls, data, imgpath):
        sql = """
			UPDATE anuncio
			SET titulo = '%s', contenido = '%s', fecha_de_publicacion = '%s', ruta = '%s'
			WHERE anuncio.id = '%s'
		"""

        titulo = data.get('titulo', '')
        contenido = data.get('contenido', '')
        fecha_de_publicacion = data.get('fecha_de_publicacion', '')
        anuncio_id = data.get('anuncio_id', '')

        cursor = cls.database().cursor()
        cursor.execute(
            sql % (titulo, contenido, fecha_de_publicacion, imgpath, anuncio_id))
        cls.database().commit()
        return True

    @classmethod
    def eliminar(cls, id):
        sql = """ DELETE FROM anuncio WHERE id = %s"""
        cursor = cls.database().cursor()
        cursor.execute(sql, (str(id)))
        cls.database().commit()
        return True
