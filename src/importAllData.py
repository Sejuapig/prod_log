import admin.ajout_bd_equipment as equip
import admin.ajout_bd_activity as act
import admin.ajout_bd_install as inst
import admin.ajout_bd_equipment_activity as equip_act
import admin.cr_tb_bd as create

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

print('done')