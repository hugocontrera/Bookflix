from db import get_db

class Plan (object):

	@classmethod
	def database(cls):
		return get_db()

	@classmethod
	def all(cls):
		sql = "SELECT * FROM plan"

		cursor = cls.database().cursor()
		cursor.execute(sql)

		return cursor.fetchall()

	@classmethod
	def encontrar_por_id(cls, plan_id):
		sql = "SELECT * FROM plan WHERE id = %s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (plan_id))		
		return cursor.fetchone()

	@classmethod
	def numero_de_perfiles_del_usuario_con_id(cls, usuario_id):
		sql = "SELECT COUNT(*) FROM perfiles AS p WHERE p.id_usuario=%s"
		cursor = cls.database().cursor()
		cursor.execute(sql, (usuario_id))		
		return cursor.fetchone()
