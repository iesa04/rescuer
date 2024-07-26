import cx_Oracle
from .models import Transmission
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con
"""
def retrieve_transmission_data():
    print("Inside get transmission list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM transmission ORDER BY tid ASC')
    rows = cursor.fetchall()

    transmission_list = []
    chassis_name_dict = {}

    for row in rows:
        transmission = Transmission(
            tid=row[0], transmission_name=row[1], transmission_type=row[2],
            gears=row[3], max_torque=row[4], weight=row[5],
            transmission_cost=row[6]
        )
        transmission_list.append(transmission)

        cursor.execute('SELECT cid FROM chassis_transmission WHERE transmission_id = {}'.format(transmission.tid))
        chassis_rows = cursor.fetchall()
        chassis_list = [i[0] for i in chassis_rows]
        print(chassis_list)

        lst = []
        for chassis_id in chassis_list:
            cursor.execute('SELECT chassis_name FROM chassis WHERE cid = {}'.format(chassis_id))
            chassis_row = cursor.fetchall()[0]
            lst.append(chassis_row[0])
        chassis_name_dict[transmission.tid] = lst

    print(chassis_name_dict)
    cursor.close()
    con.close()
    return transmission_list, chassis_name_dict
"""
def retrieve_transmission_data():
    print("Inside get transmission list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM transmission ORDER BY tid ASC')
    rows = cursor.fetchall()

    transmission_list = []
    chassis_list = []
    chassis_name_dict = {}

    for row in rows:
        transmission = Transmission(
            tid=row[0], transmission_name=row[1], transmission_type=row[2],
            gears=row[3], max_torque=row[4], weight=row[5],
            transmission_cost=row[6]
        )
        transmission_list.append(transmission)

        cursor.execute('SELECT cid FROM chassis_transmission WHERE transmission_id = {}'.format(transmission.tid))
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

    return transmission_list, chassis_name_dict


def get_transmission(tid):
    print("Inside transmission data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM transmission WHERE tid={}'.format(tid))
    rows = cursor.fetchall()

    transmission = Transmission()
    if rows:
        for row in rows:
            transmission = Transmission(
                tid=row[0], transmission_name=row[1], transmission_type=row[2],
                gears=row[3], max_torque=row[4], weight=row[5],
                transmission_cost=row[6]
            )
    else:
        raise Exception(config.TRANSMISSION_DATA_NOT_FOUND)

    cursor.close()
    con.close()
    return transmission

def save_transmission(transmission_data):
    print("Inside save transmission data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'INSERT INTO transmission(transmission_name, type, gears, '
        'max_torque, weight, transmission_cost) '
        'VALUES(:transmission_name, :transmission_type, :gears, '
        ':max_torque, :weight, :transmission_cost)'
    )
    cursor.execute(sql, transmission_data)

    sql = 'select max(tid) from transmission'
    cursor.execute(sql)
    tid=cursor.fetchall()[0][0]

    con.commit()
    cursor.close()
    con.close()

    return tid

def update_transmission(transmission_data):
    print("Inside update transmission data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'UPDATE transmission SET transmission_name = \'{}\', '
        'type = \'{}\', gears={}, '
        'max_torque={}, weight={}, transmission_cost={} '
        'WHERE tid={}'.format(
            transmission_data[1], transmission_data[2], transmission_data[3],
            transmission_data[4], transmission_data[5], transmission_data[6],
            transmission_data[0]
        )
    )

    cursor.execute(sql)
    con.commit()

    cursor.close()
    con.close()

def delete_transmission(tid):
    print("Inside delete transmission data")
    con = connect_db()
    cursor = con.cursor()
    
    sql = 'DELETE FROM chassis_transmission WHERE transmission_id={}'.format(tid)
    cursor.execute(sql)

    sql = 'DELETE FROM transmission WHERE tid={}'.format(tid)
    cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()

def get_compatibility(tid):
    print("Inside transmission Compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select cid from chassis_transmission where transmission_id={}'.format(tid)

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

def modify_compatibility(tid,chassis_list):
    print("Inside transmission modify_compatibility data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_transmission where transmission_id = {}'.format(tid)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        sql = 'insert into chassis_transmission(cid, transmission_id) values ({}, {})'.format(cid,tid)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return