import sqlite3

def run():
	"""Function allowing you to connect to the database"""
	conn = sqlite3.connect('../database/installation_sportives.db')
	curseur = conn.cursor()
	return (conn, curseur)

if __name__ == '__main__':
	run()