import cx_Oracle
from .models import Suspension
from home import config

def connect_db():
	con = cx_Oracle.connect(config.db_connect)
	return con

def retrieve_data():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from suspension')
	rows = cursor.fetchall()
	print(rows)

	suspensionList = []
	chassis_list_front = []
	chassis_list_rear = []
	chassis_name_dict_front = {}
	chassis_name_dict_rear = {}
	for row in rows:
		suspensionRow = Suspension(suspension_id=row[0], suspension_name=row[1], suspension_cost=row[2])
		suspensionList.append(suspensionRow)
       
		cursor.execute('SELECT cid FROM Chassis_Frontaxle_suspension WHERE front_suspension_id = {}'.format(suspensionRow.suspension_id))
		rows = cursor.fetchall()
		print(rows)
		chassis_list_front.append([i[0] for i in rows])
		print(chassis_list_front)

		cursor.execute('SELECT cid FROM Chassis_Rearaxle_suspension WHERE rear_suspension_id = {}'.format(suspensionRow.suspension_id))
		rows = cursor.fetchall()
		print(rows)
		chassis_list_rear.append([i[0] for i in rows])
		print(chassis_list_rear)

	for i in range(len(chassis_list_front)): 
		lst = []
		cid = 0
		for cid in chassis_list_front[i]:
		    cursor.execute('select chassis_name from chassis where cid = {}'.format(cid))
		    row = cursor.fetchall()[0][0]
		    lst.append(row)
		chassis_name_dict_front[i] = lst

	print(chassis_name_dict_front)

	for i in range(len(chassis_list_rear)): 
		lst = []
		cid = 0
		for cid in chassis_list_rear[i]:
		    cursor.execute('select chassis_name from chassis where cid = {}'.format(cid))
		    row = cursor.fetchall()[0][0]
		    lst.append(row)
		chassis_name_dict_rear[i] = lst
        
	print(chassis_name_dict_rear)
	print(suspensionList)

	cursor.close()
	con.close()
	return suspensionList, chassis_name_dict_front, chassis_name_dict_rear


def get_suspension(suspension_id):
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM suspension WHERE suspension_id={}'.format(suspension_id))
    rows = cursor.fetchall()

    suspension = Suspension()
    if rows:
        suspension_data = rows[0]
        suspension = Suspension(
            suspension_id=suspension_data[0], suspension_name=suspension_data[1], suspension_cost=suspension_data[2]
        )
    else:
        raise Exception("SUSPENSION_DATA_NOT_FOUND")

    cursor.close()
    con.close()
    return suspension

def save_suspension(suspension_data):
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'INSERT INTO suspension(suspension_name, suspension_cost) '
        'VALUES(:suspension_name, :suspension_cost)'
    )

    cursor.execute(sql, suspension_data)
    con.commit()

    cursor.execute("select max(suspension_id) from suspension")
    suspension_id = cursor.fetchall()[0][0]

    cursor.close()
    con.close()
    return suspension_id

def update_suspension(suspension_data):
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'UPDATE suspension SET suspension_name=\'{}\', suspension_cost={} '
        'WHERE suspension_id={}'.format(suspension_data[1],suspension_data[2],suspension_data[0], )
    )
    print(sql)
    cursor.execute(sql)
    con.commit()

    cursor.close()
    con.close()

def delete_suspension(suspension_id):
    con = connect_db()
    cursor = con.cursor()

    sql = 'DELETE FROM chassis_frontaxle_suspension WHERE front_suspension_id={}'.format(suspension_id)
    cursor.execute(sql)

    sql = 'DELETE FROM chassis_rearaxle_suspension WHERE rear_suspension_id={}'.format(suspension_id)
    cursor.execute(sql)        

    sql = 'DELETE FROM suspension WHERE suspension_id={}'.format(suspension_id)
    cursor.execute(sql)
    con.commit()

    cursor.close()
    con.close()

def get_fa_compatibility(suspension_id):
    print("Inside get_fa_compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select cid from chassis_frontaxle_suspension where FRONT_SUSPENSION_ID={}'.format(suspension_id)

    cursor.execute(sql)
    compatible = cursor.fetchall()
    compatible = [i[0] for i in compatible]
    sql = 'select cid, chassis_name from chassis'
    cursor.execute(sql)

    chassis_data = cursor.fetchall()

    print(compatible)
    print(chassis_data)
    cursor.close()
    con.close()
    return compatible, chassis_data

def modify_fa_compatibility(suspension_id,chassis_list):
    print("Inside modify_fa_compatibility")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_frontaxle_suspension where  FRONT_SUSPENSION_ID = {}'.format(suspension_id)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        sql = 'insert into chassis_frontaxle_suspension(cid,  FRONT_SUSPENSION_ID) values ({}, {})'.format(cid,suspension_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return

def get_ra_compatibility(suspension_id):
    print("Inside get_ra_compatibility")

    con = connect_db()
    cursor = con.cursor()


    sql = 'select cid from chassis_rearaxle_suspension where REAR_SUSPENSION_ID={}'.format(suspension_id)
    cursor.execute(sql)
    compatible = cursor.fetchall()
    compatible = [i[0] for i in compatible]
    sql = 'select cid, chassis_name from chassis'
    cursor.execute(sql)

    chassis_data = cursor.fetchall()

    print(compatible)
    print(chassis_data)
    cursor.close()
    con.close()
    return compatible, chassis_data

def modify_ra_compatibility(suspension_id,chassis_list):
    print("Inside modify_ra_compatibility")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_rearaxle_suspension where  REAR_SUSPENSION_ID = {}'.format(suspension_id)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        print(sql)
        sql = 'insert into chassis_rearaxle_suspension(cid,  REAR_SUSPENSION_ID) values ({}, {})'.format(cid,suspension_id)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return    