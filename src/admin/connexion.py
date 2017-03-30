import mysql.connector as connector
def connexion():
	try:
		return connector.connect(host = "infoweb", user = "E145725X", password ="E145725X", database = "E145725X")
	except MySQLdb.Error as e :
		print("connexion impossible")
		print(e)