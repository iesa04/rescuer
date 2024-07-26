import cx_Oracle
from .models import UserType, AdminDetail, CustomerDetail, SupplierDetail
from home import config

def connect_db():
	con = cx_Oracle.connect(config.db_connect)
	return con

def retrieve_user_types():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from user_type')
	rows = cursor.fetchall()
	print(rows)
	user_type_List = []

	for row in rows:
		user_type_row = UserType(user_type_code = row[0], user_type_name = row[1])
		user_type_List.append(user_type_row)
	print(user_type_List)

	cursor.close()
	con.close()
	return user_type_List

def get_admin_data():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from users inner join admin_detail on users.user_id = admin_detail.user_id order by users.user_id asc')
	rows = cursor.fetchall()
	print(rows)
	admin_List = []

	for row in rows:
		admin_row = AdminDetail(user_id = row[0], username = row[1], password  = row[2],name = row[3],user_type_code = row[4],admin_phone_number = row[6])
		admin_List.append(admin_row)
	print(admin_List)

	cursor.close()
	con.close()
	return admin_List

def get_customer_data():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from users inner join customer_detail on users.user_id = customer_detail.user_id')
	rows = cursor.fetchall()
	print(rows)
	customer_List = []

	for row in rows:
		customer_row = CustomerDetail(user_id = row[0], username = row[1], password  = row[2],name = row[3],user_type_code = row[4],FDID = row[6])
		customer_List.append(customer_row)
	print(customer_List)

	cursor.close()
	con.close()
	return customer_List

def get_supplier_data():
	con = connect_db()
	cursor = con.cursor()

	# fetchall() is used to fetch all records from result set
	cursor.execute('select * from users inner join supplier_detail on users.user_id = supplier_detail.user_id')
	rows = cursor.fetchall()
	print(rows)
	supplier_List = []

	for row in rows:
		supplier_row = SupplierDetail(user_id = row[0], username = row[1], password  = row[2],name = row[3],user_type_code = row[4],supplier_state= row[6])
		supplier_List.append(supplier_row)
	print(supplier_List)

	cursor.close()
	con.close()
	return supplier_List

def save_admin(admin):
	print("Inside save admin:\n", admin)
	con = connect_db()
	cursor = con.cursor()

	#sql = ('insert into users(username, password, name, user_type_code) values (:username,:password,:name, AD)')
	sql = ('insert into users(username, password, name, user_type_code) values (\'{}\',\'{}\',\'{}\', \'{}\')'.format(admin[0], admin[1], admin[2], 'AD'))
	print(sql)
	cursor.execute(sql)
	con.commit()

	sql = 'select user_id from users where username = \'{}\''.format(admin[0])
	cursor.execute(sql)
	uid = cursor.fetchall()[0][0]
	con.commit()	
	print(uid)

	sql = 'insert into admin_detail values(\'{}\',\'{}\')'.format(uid, admin[3])
	cursor.execute(sql)
	con.commit()	

	cursor.close()
	con.close()

def delete_admin(user_id):
	print("Inside admin Delete data")
	con = connect_db()
	cursor = con.cursor()

	print(user_id)
	sql = ('delete from admin_detail where user_id = ' + str(user_id))

	print(sql)
	try:
		cursor.execute(sql)
		con.commit()
	except cx_Oracle.Error as error:
		print(error)

	sql = ('delete from users where user_id = ' + str(user_id))

	print(sql)
	try:
		cursor.execute(sql)
		con.commit()
	except cx_Oracle.Error as error:
		print(error)

	print("Deleted")

	cursor.close()
	con.close()