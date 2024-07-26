import cx_Oracle
from .models import Chassis
from home import config
from engine.models import Engine
from transmission.models import Transmission
from suspension.models import Suspension
from electricalsystem.models import ElectricalSystem

def connect_db():
	con = cx_Oracle.connect(config.db_connect)
	return con

def retrieve_data():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from chassis order by cid asc')
	rows = cursor.fetchall()

	chassisList = []
	for row in rows:
		chassisRow = Chassis(cid=row[0], chassis_name=row[1], frontal_airbags=row[2], seating_capacity=row[3], side_roll_protection=row[4], front_gawr=row[5], rear_gawr=row[6], chassis_cost=row[7], status=row[8])
		chassisList.append(chassisRow)
	print(chassisList)

	cursor.close()
	con.close()
	return chassisList

def retrieve_chassis_names():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select chassis_name from chassis where status=\'ACTIVE\' order by cid asc')
	rows = cursor.fetchall()

	chassisList = [i[0] for i in rows]

	print(chassisList)

	cursor.close()
	con.close()
	return chassisList

def ct_chassis_get(chassis):
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from chassis where status=\'ACTIVE\' and chassis_name = \'{}\''.format(chassis))
	chassis_data = cursor.fetchall()[0]
	print(chassis_data)

	cid = chassis_data[0]

	#Engine Data
	cursor.execute('select engine_id from chassis_engine where cid = {}'.format(cid))
	rows = cursor.fetchall()
	engine_id_list= [i[0] for i in rows]
	print(engine_id_list)

	engine_list = []

	for i in engine_id_list:
		cursor.execute('select * from engine where engine_id = {}'.format(i))
		row = cursor.fetchall()[0]
		print(row)
		engine = Engine(
			engine_id=row[0], engine_name=row[1], horsepower=row[2], peak_torque=row[3],
			dry_weight=row[4], cylinders=row[5], displacement=row[6],
			clutch_engagement_torque=row[7], governed_speed=row[8], engine_cost=row[9]
		)
		engine_list.append(engine)

	#Transmission Data
	cursor.execute('select transmission_id from chassis_transmission where cid = {}'.format(cid))
	rows = cursor.fetchall()
	transmission_id_list= [i[0] for i in rows]
	print(transmission_id_list)

	transmission_list = []

	for i in transmission_id_list:
		cursor.execute('select * from transmission where tid = {}'.format(i))
		row = cursor.fetchall()[0]
		print(row)
		transmission = Transmission(
			tid=row[0], transmission_name=row[1], transmission_type=row[2],
			gears=row[3], max_torque=row[4], weight=row[5],
			transmission_cost=row[6]
		)
		transmission_list.append(transmission)

	#Electricals Data
	cursor.execute('select electrical_id from chassis_electricals where cid = {}'.format(cid))
	rows = cursor.fetchall()
	electrical_id_list= [i[0] for i in rows]
	print(electrical_id_list)

	electrical_system_list = []

	for i in electrical_id_list:
		cursor.execute('select * from electrical_system where electrical_id = {}'.format(i))
		row = cursor.fetchall()[0]
		print(row)
		electrical_system = ElectricalSystem(
			electrical_id=row[0], electrical_name=row[1], electrical_cost=row[2]
		)
		electrical_system_list.append(electrical_system)
	
	#Front Suspension Data
	cursor.execute('select * from suspension where suspension_id in (select front_suspension_id from chassis_frontaxle_suspension where cid = {})'.format(cid))
	rows = cursor.fetchall()
	print(rows)

	front_suspension_list = []

	for row in rows:
		print(row)
		suspensionRow = Suspension(suspension_id=row[0], suspension_name=row[1], suspension_cost=row[2])
		front_suspension_list.append(suspensionRow)

	#Rear Suspension Data
	cursor.execute('select * from suspension where suspension_id in (select rear_suspension_id from chassis_rearaxle_suspension where cid = {})'.format(cid))
	rows = cursor.fetchall()
	print(rows)

	rear_suspension_list = []

	for row in rows:
		print(row)
		suspensionRow = Suspension(suspension_id=row[0], suspension_name=row[1], suspension_cost=row[2])
		rear_suspension_list.append(suspensionRow)

	return chassis_data, engine_list, transmission_list, electrical_system_list,front_suspension_list,rear_suspension_list

def get_chassis(cid):
	print("inside get_chassis data")

	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from chassis where cid={}'.format(cid))
	rows= cursor.fetchall()

	chassisRow = Chassis
	if (rows!=[]) :
		for row in rows:
			chassisRow = Chassis(cid=row[0], chassis_name=row[1], frontal_airbags=row[2], seating_capacity=row[3], side_roll_protection=row[4], front_gawr=row[5], rear_gawr=row[6], chassis_cost=row[7])
			print(chassisRow.cid)
	else:
		raise Exception(config.CHASSIS_DATA_NOT_FOUND)
		cursor.close()
		con.close()
	cursor.close()
	con.close()
	return chassisRow


def save_chassis(chassis):
	print(chassis)
	con = connect_db()
	cursor = con.cursor()

	sql = ('insert into chassis(chassis_name, frontal_airbags, seating_capacity, side_roll_protection, front_gawr, rear_gawr, chassis_cost) '
        'values(:chassis_name,:frontal_airbags,:seating_capacity,:side_roll_protection,:front_gawr,:rear_gawr,:chassis_cost)')

	cursor.execute(sql, chassis)
	con.commit()

	cursor.execute('select max(cid) from chassis')
	cid = cursor.fetchall()[0][0]

	cursor.close()
	con.close()
	return cid
	
def update_chassis(chassis):
	print("Inside Update Chassis:")
	print(chassis[0])
	con = connect_db()
	cursor = con.cursor()


	print(chassis)
	#sql = ('update chassis set chassis_name=:chassis_name, frontal_airbags=:frontal_airbags, seating_capacity=:seating_capacity, side_roll_protection=:side_roll_protection, front_gawr=:front_gawr, rear_gawr=:rear_gawr, chassis_cost=:chassis_cost where cid=:cid')
	#sql = ('update chassis set chassis_name=:chassis[1], frontal_airbags=:chassis[2],seating_capacity=:chassis[3], side_roll_protection=:chassis[4], front_gawr=:chassis[5], rear_gawr=:chassis[6], chassis_cost=:chassis[7] where cid=:chassis[0]')
	#sql = ('update chassis set chassis_name=:1, frontal_airbags=:2,seating_capacity=:3, side_roll_protection=:4, front_gawr=:5, rear_gawr=:6, chassis_cost=:7 where cid=:8')
	sql = ('update chassis set chassis_name=\''+chassis[1]+'\', frontal_airbags=\''+chassis[2]+'\', seating_capacity='+chassis[3]+', side_roll_protection=\''+chassis[4]+'\', front_gawr='+chassis[5]+', rear_gawr='+chassis[6]+', chassis_cost='+chassis[7]+' where cid='+chassis[0])

	print(sql)
	try:
		cursor.execute(sql)
		con.commit()
	except cx_Oracle.Error as error:
		print(error)

	print("Updated")

	cursor.close()
	con.close()

def delete_chassis(cid):
	print("Inside Delete data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	cursor.execute('delete from chassis_engine where cid='+str(cid))
	cursor.execute('delete from chassis_transmission where cid='+str(cid))
	cursor.execute('delete from chassis_electricals where cid='+str(cid))
	cursor.execute('delete from chassis_frontaxle_suspension where cid='+str(cid))
	cursor.execute('delete from chassis_rearaxle_suspension where cid='+str(cid))
	cursor.execute('delete from aerial_chassis where cid='+str(cid))

	sql = ('delete from chassis where cid='+str(cid))
	try:
		cursor.execute(sql)
		con.commit()
		print("Deleted")
	except cx_Oracle.Error as error:
		print(error)

	

	cursor.close()
	con.close()

def save_engine_compatibility(engine_id_list, cid):
	print("Inside save chassis engine data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	for i in engine_id_list:
		sql = ('INSERT INTO Chassis_Engine(CID, Engine_ID) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	con.commit()
	cursor.close()
	con.close()
	return

def save_transmission_compatibility(transmission_id_list, cid):
	print("Inside save chassis transmission data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	for i in transmission_id_list:
		sql = ('INSERT INTO Chassis_transmission(CID, transmission_id) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	con.commit()
	cursor.close()
	con.close()
	return

def save_electrical_compatibility(electricals_id_list, cid):
	print("Inside save chassis electricals data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	for i in electricals_id_list:
		sql = ('INSERT INTO chassis_electricals(CID, electrical_id) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	con.commit()
	cursor.close()
	con.close()
	return

def save_suspension_compatibility(fa_suspension_id_list,ra_suspension_id_list, cid):
	print("Inside save chassis suspension data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	for i in fa_suspension_id_list:
		sql = ('INSERT INTO chassis_frontaxle_suspension(CID, front_suspension_id) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	for i in ra_suspension_id_list:
		sql = ('INSERT INTO chassis_rearaxle_suspension(CID, rear_suspension_id) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	con.commit()
	cursor.close()
	con.close()
	return


def save_aerials_compatibility(aerial_id_list, cid):
	print("Inside save chassis aerials data")
	con = connect_db()
	cursor = con.cursor()

	print(cid)
	for i in aerial_id_list:
		sql = ('INSERT INTO aerial_chassis(CID, aerial_id) VALUES({},{})'.format(cid, i))
		cursor.execute(sql)

	con.commit()
	cursor.close()
	con.close()
	return

def update_chassis_status(cid,status):
    print("Inside update_chassis_status data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'update chassis set status=\''+status+'\' where cid='+ str(cid)
    print(sql)
    cursor.execute(sql)

    if status != 'ACTIVE':
	    sql = 'delete from aerial_chassis where cid='+ str(cid)
	    print(sql)
	    cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()     