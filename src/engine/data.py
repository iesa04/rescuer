import cx_Oracle
from .models import Engine
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def retrieve_engine_data():
    print("Inside get engine list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select * from engine order by engine_id asc')
    rows = cursor.fetchall()

    engine_list = []
    chassis_list = []
    chassis_name_dict = {}
    for row in rows:
        engine = Engine(
            engine_id=row[0], engine_name=row[1], horsepower=row[2], peak_torque=row[3],
            dry_weight=row[4], cylinders=row[5], displacement=row[6],
            clutch_engagement_torque=row[7], governed_speed=row[8], engine_cost=row[9]
        )
        engine_list.append(engine)
        cursor.execute('select cid from chassis_engine where engine_id = {}'.format(engine.engine_id))
        rows = cursor.fetchall()
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
    return engine_list, chassis_name_dict

def get_engine(engine_id):
    print("Inside get engine data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select * from engine where engine_id={}'.format(engine_id))
    rows = cursor.fetchall()

    engine = Engine()
    if rows:
        for row in rows:
            engine = Engine(
                engine_id=row[0], engine_name=row[1], horsepower=row[2], peak_torque=row[3],
                dry_weight=row[4], cylinders=row[5], displacement=row[6],
                clutch_engagement_torque=row[7], governed_speed=row[8], engine_cost=row[9]
            )
    else:
        raise Exception(config.ENGINE_DATA_NOT_FOUND)

    cursor.close()
    con.close()
    return engine

def save_engine(engine_data):
    print("Inside engine save data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'insert into engine(engine_name, horsepower, peak_torque, dry_weight, '
        'cylinders, displacement, clutch_engagement_torque, governed_speed, engine_cost) '
        'values(:engine_name, :horsepower, :peak_torque, :dry_weight, '
        ':cylinders, :displacement, :clutch_engagement_torque, :governed_speed, :engine_cost)'
    )
    cursor.execute(sql, engine_data)

    cursor.execute('select max(engine_id) from engine')
    engine_id = cursor.fetchall()[0][0]

    con.commit()
    cursor.close()
    con.close()
    return engine_id

def update_engine(engine_data):
    print("Inside Update engine data")
    con = connect_db()
    cursor = con.cursor()

    print(engine_data)

    sql = 'update engine set engine_name = \'{}\', horsepower={}, peak_torque={}, dry_weight={}, cylinders={}, displacement={}, clutch_engagement_torque={}, governed_speed={}, engine_cost={} where engine_id= {}'.format(engine_data[1],engine_data[2],engine_data[3],engine_data[4],engine_data[5],engine_data[6],engine_data[7],engine_data[8],engine_data[9],engine_data[0])

    print(sql)

    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

def delete_engine(engine_id):
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_engine where engine_id={}'.format(engine_id)
    cursor.execute(sql)    

    sql = 'delete from engine where engine_id={}'.format(engine_id)
    cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()

def get_compatibility(engine_id):
    print("Inside Engine Compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select cid from chassis_engine where engine_id={}'.format(engine_id)

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

def modify_compatibility(engine_id,chassis_list):
    print("Inside modify_compatibility data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from chassis_engine where engine_id = {}'.format(engine_id)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        sql = 'insert into chassis_engine(cid, engine_id) values ({}, {})'.format(cid,engine_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return

    