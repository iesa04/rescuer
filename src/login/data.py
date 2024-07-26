import cx_Oracle
from users.models import AdminDetail
from home import config

def connect_db():
	con = cx_Oracle.connect(config.db_connect)
	return con

def validate_data(cred):
	con = connect_db()
	cursor = con.cursor()

	cursor.execute('select * from users where username = \'{}\' and password = \'{}\''.format(cred[0],cred[1]))
	rows = cursor.fetchall()

	if (rows!=[]) :
		for row in rows:
			user = AdminDetail(user_id=row[0], username=row[1], name=row[3], user_type_code=row[4])
			print(user.user_id)
	else:
		raise Exception(config.USER_DATA_NOT_FOUND)
		cursor.close()
		con.close()

	print(user)

	cursor.close()
	con.close()
	return user

def retrieve_fdid(username):
	con = connect_db()
	cursor = con.cursor()

	cursor.execute('select user_id from users where username = \'{}\''.format(username))
	user_id = cursor.fetchall()[0][0]

	cursor.execute('select fdid from customer_detail where user_id= \'{}\''.format(user_id))
	fdid = cursor.fetchall()[0][0]

	print(fdid)

	cursor.close()
	con.close()
	return fdid

def validate_signup(cred):
	print("SQL")
	con = connect_db()
	cursor = con.cursor()

	sql = 'select * from fire_department where fdid = \'{}\' and hqzip = \'{}\''.format(cred[0],cred[1])
	print(sql)
	cursor.execute(sql)
	rows = cursor.fetchall()

	if rows == []:
		print("ERROR")
		cursor.close()
		con.close()	
		raise Exception(config.FIRE_DEPARTMENT_DATA_NOT_FOUND)
	
	else:
		dept = rows[0]
	cursor.close()
	con.close()
	print(rows)

	return dept

def validate_username(username):
	con = connect_db()
	cursor = con.cursor()

	sql = 'select count(*) from users where username = \'{}\''.format(username)
	print(sql)
	cursor.execute(sql)
	rows = cursor.fetchall()
	print(rows)
	ct = rows[0][0]
	if ct == 0:
		cursor.close()
		con.close()
		return True		
	else:
		print("ERROR")
		cursor.close()
		con.close()
		raise Exception(config.USERNAME_EXISTS)

def validate_fdid_zip(fdid):
	con = connect_db()
	cursor = con.cursor()

	sql = 'select count(*) from customer_detail where fdid = \'{}\''.format(fdid)
	print(sql)
	cursor.execute(sql)
	rows = cursor.fetchall()
	print(rows)
	ct = rows[0][0]
	if ct == 0:
		cursor.close()
		con.close()
		return True		
	else:
		print("ERROR")
		cursor.close()
		con.close()
		raise Exception(config.FDID_USER_EXISTS)		

def save_customer(customer,name):
	print("Inside save customer:\n", customer)
	con = connect_db()
	cursor = con.cursor()

	#sql = ('insert into users(username, password, name, user_type_code) values (:username,:password,:name, AD)')
	sql = ('insert into users(username, password, name, user_type_code) values (\'{}\',\'{}\',\'{}\', \'{}\')'.format(customer[2], customer[3], name, 'CT'))
	print(sql)
	cursor.execute(sql)
	con.commit()

	sql = 'select user_id from users where username = \'{}\''.format(customer[2])
	cursor.execute(sql)
	uid = cursor.fetchall()[0][0]
	con.commit()	
	print(uid)

	sql = 'insert into customer_detail values(\'{}\',\'{}\')'.format(uid, customer[0])
	cursor.execute(sql)
	con.commit()	

	cursor.close()
	con.close()