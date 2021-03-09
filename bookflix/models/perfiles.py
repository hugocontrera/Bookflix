from db import get_db


class Perfiles (object):

    @classmethod
    def database(cls):
        return get_db()

    @classmethod
    def encontrar_por_id(cls, id_perfil):
        sql = "SELECT * FROM perfiles WHERE perfiles.id = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql % id_perfil)
        return cursor.fetchone()

    @classmethod
    def user_id (cls, user_id):
        sql = "SELECT * FROM perfiles WHERE id_usuario = %s"
        cursor = cls.database().cursor()
        cursor.execute(sql % user_id)
        return cursor.fetchall()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM perfiles"
        cursor = cls.database().cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def crear(cls, data):
        sql = """INSERT INTO perfiles
        (nombre, foto, id_usuario)
        VALUES (%s)"""
        parametros = str(list(data.values())).strip('[]')
        cursor = cls.database().cursor()
        cursor.execute(sql % parametros)
        cls.database().commit()
        return True

    @classmethod
    def eliminar(cls, id):
        sql = """ DELETE FROM perfiles WHERE id = %s"""
        cursor = cls.database().cursor()
        cursor.execute(sql, (str(id)))
        cls.database().commit()
        return True

    @classmethod
    def edit(cls, nombre, foto, id_perfil):
        sql = """
            UPDATE perfiles
            SET nombre = '%s', foto = '%s'
            WHERE id = %s
        """
        cursor = cls.database().cursor()
        cursor.execute(sql % (nombre, foto, id_perfil))
        cls.database().commit()
        return True

    @classmethod
    def existe_perfil_con_nombre(cls, nombre):
        sql = """
        SELECT *
        FROM perfiles p
        WHERE p.nombre = %s
        """
        cursor = cls.database().cursor()
        cursor.execute(sql, (nombre))

        return cursor.rowcount > 0
