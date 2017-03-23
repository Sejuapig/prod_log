#!/usr/bin/python
# coding: utf8
import admin.connexion as connexion

def run():
	conn = connexion.connexion()
	cursor = conn.cursor()

	cursor.execute("DROP TABLE IF EXISTS equipment_activity;")
	cursor.execute("DROP TABLE IF EXISTS installation;")
	cursor.execute("DROP TABLE IF EXISTS equipment;")
	cursor.execute("DROP TABLE IF EXISTS activity;")

	creer_table_install = "CREATE TABLE IF NOT EXISTS `installation` (`id_installation` int(11) NOT NULL, `nom_installation` varchar(100) NOT NULL, `adresse` varchar(100) NOT NULL, `code_postal` varchar(100) NOT NULL, `ville` varchar(100) NOT NULL, `latitude` float NOT NULL, `longitude` float NOT NULL) DEFAULT CHARACTER SET=utf8;"

	creer_table_equip = "CREATE TABLE IF NOT EXISTS `equipment` (`id_equipment` int(11) NOT NULL, `nom_equipment` varchar(100) NOT NULL, `id_installation` int(11) NOT NULL) DEFAULT CHARACTER SET=utf8;"

	creer_table_acti = "CREATE TABLE IF NOT EXISTS `activity` (`id_activity` int(11) NOT NULL, `nom_activity` varchar(100) NOT NULL) DEFAULT CHARACTER SET=utf8;"

	creer_table_equi_acti = "CREATE TABLE IF NOT EXISTS `equipment_activity` (`id_equipment` int(11) NOT NULL, `id_activity` int(11) NOT NULL) DEFAULT CHARACTER SET=utf8;"

	alter_table_install ="ALTER TABLE `installation` ADD PRIMARY KEY (`nom_installation`);"
	alter_table_equip ="ALTER TABLE `equipment` ADD PRIMARY KEY (`id_equipment`);"
	alter_table_acti ="ALTER TABLE `activity` ADD PRIMARY KEY (`id_activity`);"
	alter_table_equip_acti ="ALTER TABLE `equipment_activity` ADD PRIMARY KEY (`id_equipment`, `id_activity`);"
	alter_table_equip_actiFK ="ALTER TABLE `equipment_activity` ADD CONSTRAINT `fk_equipment` FOREIGN KEY (`id_equipment`) REFERENCES `E145725X`.`equipment`(`id_equipment`) ON DELETE CASCADE;"
	alter_table_equip_actiFK2 = "ALTER TABLE `equipment_activity` ADD CONSTRAINT `fk_activity` FOREIGN KEY (`id_activity`) REFERENCES `E145725X`.`activity`(`id_activity`) ON DELETE CASCADE;"

	cursor.execute(creer_table_install)
	cursor.execute(creer_table_equip)
	cursor.execute(creer_table_acti)
	cursor.execute(creer_table_equi_acti)

	cursor.execute(alter_table_install)
	cursor.execute(alter_table_equip)
	cursor.execute(alter_table_acti)
	cursor.execute(alter_table_equip_acti)
	cursor.execute(alter_table_equip_actiFK)
	cursor.execute(alter_table_equip_actiFK2)

	conn.commit()
	conn.close()
