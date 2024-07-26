import cx_Oracle
from .models import Pump
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def retrieve_pump_data():
    print("Inside get pump list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM pump ORDER BY pump_id ASC')
    rows = cursor.fetchall()

    pump_list = []
    aerial_list = []
    aerial_name_dict = {}

    for row in rows:
        pump = Pump(
            pump_id=row[0], pump_name=row[1], pump_cost=row[2]
        )
        pump_list.append(pump)

        cursor.execute('SELECT aerial_id FROM aerial_pump WHERE pump_id = {}'.format(pump.pump_id))
        rows = cursor.fetchall()
        print(rows)
        aerial_list.append([i[0] for i in rows])
        print(aerial_list)

    for i in range(len(aerial_list)): 
        lst = []
        cid = 0
        for aerial_id in aerial_list[i]:
            cursor.execute('select aerial_name from aerials where aerial_id = {}'.format(aerial_id))
            row = cursor.fetchall()[0][0]
            lst.append(row)
        aerial_name_dict[i] = lst

    print(aerial_name_dict)
    cursor.close()
    con.close()
    return pump_list, aerial_name_dict

def get_pump(pump_id):
    print("Inside get pump data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM pump WHERE pump_id={}'.format(pump_id))
    rows = cursor.fetchall()

    pump = Pump()
    if rows:
        for row in rows:
            pump = Pump(
                pump_id=row[0], pump_name=row[1], pump_cost=row[2]
            )
    else:
        raise Exception(config.PUMP_DATA_NOT_FOUND)

    cursor.close()
    con.close()
    return pump

def save_pump(pump_data):
    print("Inside save pump data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'INSERT INTO pump(pump_name, pump_cost) '
        'VALUES(:pump_name, :pump_cost)'
    )
    cursor.execute(sql, pump_data)

    sql = 'SELECT MAX(Pump_ID) FROM Pump'
    cursor.execute(sql)
    pump_id = cursor.fetchall()[0][0]

    con.commit()
    cursor.close()
    con.close()
    return pump_id

def update_pump(pump_data):
    print("Inside update pump data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'UPDATE pump SET pump_name = \'{}\', pump_cost={} '
        'WHERE pump_id={}'.format(
            pump_data[1], pump_data[2], pump_data[0]
        )
    )

    cursor.execute(sql)
    con.commit()

    cursor.close()
    con.close()

def delete_pump(pump_id):
    print("Inside delete pump data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'DELETE FROM aerial_pump WHERE pump_id={}'.format(pump_id)
    cursor.execute(sql)

    sql = 'DELETE FROM pump WHERE pump_id={}'.format(pump_id)
    cursor.execute(sql)

    con.commit()

    cursor.close()
    con.close()

def get_compatibility(pump_id):
    print("Inside pump Compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select aerial_id from aerial_pump where pump_id={}'.format(pump_id)

    cursor.execute(sql)
    compatible = cursor.fetchall()
    compatible = [i[0] for i in compatible]
    sql = 'select aerial_id, aerial_name from aerials'
    cursor.execute(sql)

    aerial_data = cursor.fetchall()

    print(compatible)
    print(aerial_data)
    cursor.close()
    con.close()
    return compatible, aerial_data

def modify_compatibility(pump_id,aerial_list):
    print("Inside pump modify_compatibility data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from aerial_pump where pump_id = {}'.format(pump_id)
    print(sql)
    cursor.execute(sql)

    for aerial_id in aerial_list:
        sql = 'insert into aerial_pump(aerial_id, pump_id) values ({}, {})'.format(aerial_id,pump_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return
