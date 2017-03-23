import admin.ajout_bd_equipment as equip
import admin.ajout_bd_activity as act
import admin.ajout_bd_install as inst
import admin.ajout_bd_equipment_activity as equip_act
import admin.cr_tb_bd as create

import RestServer.RecupBD as serv

def run():
	"""Main function allowing you to run the different parts of our application"""
	print('create database')
	#create.run()

	print('add equipment in the database')
	#equip.run()

	print('add activity in the database')
	#act.run()

	print('add installation in the database')
	#inst.run()

	print('add equipment_activity in the database')
	#equip_act.run()

	print('test bd')
	#serv.run()

	#print('test Server')
	#pdl.index()
	import RestServer.rest_PDL as pdl


if __name__ == '__main__':
	run()