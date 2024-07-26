import cx_Oracle
from .models import ElectricalSystem
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def retrieve_electrical_system_data():
    print("Inside get electrical system list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM electrical_system ORDER BY electrical_id ASC')
    rows = cursor.fetchall()

    electrical_system_list = []
    chassis_list = []
    chassis_name_dict = {}

    for row in rows:
        electrical_system = ElectricalSystem(
            electrical_id=row[0], electrical_name=row[1], electrical_cost=row[2]
        )
        electrical_system_list.append(electrical_system)

        cursor.execute('SELECT cid FROM chassis_electricals WHERE electrical_id = {}'.format(electrical_system.electrical_id))
        rows = cursor.fetchall()
        print(rows)
        chassis_list.append([i[0] for i in rows])
        print(chassis_list)

    for i in range(len(chassis_list)): 
        lst = []
        cid = 0
        for cid in chassis_list[i]:
            cursor.execute('select chassis_name from chassis where cid = {}'.format(cid))
            row = cursor.fetchall()[0][0]
            lst.append(row)
        chassis_name_dict[i] = lst

    print(chassis_name_dict)
    cursor.close()
    con.close()
    return electrical_system_list, chassis_name_dict

def get_electrical_system(electrical_id):
    print("Inside get electrical system data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM electrical_system WHERE electrical_id={}'.format(electrical_id))
    rows = cursor.fetchall()

    electrical_system = ElectricalSystem()
    if rows:
        for row in rows:
            electrical_system = ElectricalSystem(
                electrical_id=row[0], electrical_name=row[1], electrical_cost=row[2]
            )
    else:
        raise Exception(config.ELECTRICAL_SYSTEM_DATA_NOT_FOUND)

    cursor.close()
    con.close()
    return electrical_system

def save_electrical_system(electrical_system_data):
    print("Inside save electrical system data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'INSERT INTO electrical_system(electrical_name, electrical_cost) '
        'VALUES(:electrical_name, :electrical_cost)'
    )

    cursor.execute(sql, electrical_system_data)

    sql = 'SELECT MAX(Electrical_Id) FROM electrical_system'
    cursor.execute(sql)
    electrical_id = cursor.fetchall()[0][0]
    
    con.commit()
    cursor.close()
    con.close()
    return electrical_id

def update_electrical_system(electrical_system_data):
    print("Inside update electrical system data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'UPDATE electrical_system SET electrical_name = \'{}\', electrical_cost={} '
        'WHERE electrical_id={}'.format(
            electrical_system_data[1], electrical_system_data[2], electrical_system_data[0]
        )
    )

    cursor.execute(sql)
    con.commit()

    cursor.close()
    con.close()

def delete_electrical_system(electrical_id):
    print("Inside delete electrical system data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'DELETE FROM chassis_electricals WHERE electrical_id={}'.format(electrical_id)
    cursor.execute(sql)

    sql = 'DELETE FROM electrical_system WHERE electrical_id={}'.format(electrical_id)
    cursor.execute(sql)
    
    con.commit()
    cursor.close()
    con.close()

def get_compatibility(electrical_id):
    print("Inside electricals Compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select cid from chassis_electricals where electrical_id={}'.format(electrical_id)

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

def modify_compatibility(electrical_id,chassis_list):
    print("Inside electricals modify_compatibility data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_electricals where electrical_id = {}'.format(electrical_id)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        sql = 'insert into chassis_electricals(cid, electrical_id) values ({}, {})'.format(cid,electrical_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return