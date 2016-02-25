import ajout_bd_equipment as equip
import ajout_bd_activite as act
import ajout_bd_install as inst
import cr_tb_bd as create

def lunch():
	print('create database')
	create.lunch()

	print('add equipment in the database')
	equip.lunch()

	print('add activity in the database')
	act.lunch()

	print('add installation in the database')
	inst.lunch()

if __name__ == '__main__':
	lunch()