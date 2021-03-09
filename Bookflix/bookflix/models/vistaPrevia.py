from db import get_db


class VistaPrevia (object):

    @classmethod
    def database(cls):
        return get_db()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM vista_previa"

        cursor = cls.database().cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def crear(cls, data, pdfpath, imgpath):
        sql = """INSERT INTO
		vista_previa (nombre, descripcion, video, pdf, imagen, fecha_de_publicacion, activa)
		VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"""

        nombre = data.get('nombre', '')
        descripcion = data.get('descripcion', '')
        video = data.get('video', '')
        pdf = pdfpath
        imagen = imgpath
        fecha_de_publicacion = data.get('fecha_de_publicacion', '')
        activa = 1

        cursor = cls.database().cursor()
        cursor.execute(
            sql % (nombre, descripcion, video, pdf, imagen, fecha_de_publicacion, activa))
        cls.database().commit()
        return True

    @classmethod
    def encontrar_por_id(cls, id):
        sql = "SELECT * FROM vista_previa WHERE id = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def eliminar(cls, id):
        sql = """ DELETE FROM vista_previa WHERE id = %s"""
        cursor = cls.database().cursor()
        cursor.execute(sql, (str(id)))
        cls.database().commit()
        return True

    @classmethod
    def edit(cls, nombre, descripcion, video, pdfpath, imgpath, fecha_de_publicacion, id):
        sql = """
			UPDATE vista_previa
			SET nombre = '%s', descripcion = '%s', video = '%s', pdf = '%s', imagen = '%s', fecha_de_publicacion = '%s'
			WHERE vista_previa.id = '%s'
		"""
        cursor = cls.database().cursor()
        cursor.execute(sql % (nombre, descripcion, video, pdfpath, imgpath, fecha_de_publicacion, id))
        cls.database().commit()
        return True
