import admin.ajout_bd_equipment as equip
import admin.ajout_bd_activite as act
import admin.ajout_bd_install as inst
import admin.ajout_bd_equipement_activite as equip_act
import admin.cr_tb_bd as create

def run():
	print('create database')
	create.run()

	print('add equipment in the database')
	equip.run()

	print('add activity in the database')
	act.run()

	print('add installation in the database')
	inst.run()

	print('add equipment_activity in the database')
	equip_act.run()


if __name__ == '__main__':
	run()