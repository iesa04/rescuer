import cx_Oracle
from .models import Aerial
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def retrieve_aerial_data():
    print("Inside get aerial list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM aerials ORDER BY aerial_id ASC')
    rows = cursor.fetchall()

    aerial_list = []
    chassis_list = []
    chassis_name_dict = {}

    for row in rows:
        aerial = Aerial(
            aerial_id=row[0], class_id=row[1], aerial_name=row[2], basket=row[3],
            hstyle_jack=row[4], downjack=row[5], stabilizer_spread=row[6],
            structural_ladder_warranty=row[7], flow_capacity=row[8], minimum_angle=row[9],
            maximum_angle=row[10], wind_rating=row[11], ice_rating=row[12],
            horizontal_ladder_reach=row[13], vertical_ladder_reach=row[14],
            dry_payload_capacity=row[15], wet_payload_capacity=row[16],
            tank=row[17], aerial_cost=row[18],status=row[19]
        )
        aerial_list.append(aerial)

        cursor.execute('SELECT cid FROM aerial_chassis WHERE aerial_id = {}'.format(aerial.aerial_id))
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
    return aerial_list, chassis_name_dict

def get_aerial(aerial_id):
    print("Inside get aerial data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM aerials WHERE aerial_id = {}'.format(aerial_id))
    rows = cursor.fetchall()

    aerial = Aerial()
    if rows:
        for row in rows:
            aerial = Aerial(
                aerial_id=row[0], class_id=row[1], aerial_name=row[2], basket=row[3],
                hstyle_jack=row[4], downjack=row[5], stabilizer_spread=row[6],
                structural_ladder_warranty=row[7], flow_capacity=row[8], minimum_angle=row[9],
                maximum_angle=row[10], wind_rating=row[11], ice_rating=row[12],
                horizontal_ladder_reach=row[13], vertical_ladder_reach=row[14],
                dry_payload_capacity=row[15], wet_payload_capacity=row[16],
                tank=row[17], aerial_cost=row[18]
            )
    else:
        raise Exception("Aerial data not found")

    cursor.close()
    con.close()
    return aerial

def save_aerial(aerial_data):
    print("Inside save aerial data")
    print(aerial_data)

    con = connect_db()
    cursor = con.cursor()

    sql = (
        'INSERT INTO aerials (class_id, aerial_name, basket, hstyle_jack, downjack, '
        'stabilizer_spread, structural_ladder_warranty, flow_capacity, minimum_angle, '
        'maximum_angle, wind_rating, ice_rating, horizontal_ladder_reach, '
        'vertical_ladder_reach, dry_payload_capacity, wet_payload_capacity, tank, aerial_cost) '
        'VALUES (:class_id, :aerial_name, :basket, :hstyle_jack, :downjack, '
        ':stabilizer_spread, :structural_ladder_warranty, :flow_capacity, :minimum_angle, '
        ':maximum_angle, :wind_rating, :ice_rating, :horizontal_ladder_reach, '
        ':vertical_ladder_reach, :dry_payload_capacity, :wet_payload_capacity, :tank, :aerial_cost)'
    )
    cursor.execute(sql, aerial_data)

    sql = 'SELECT MAX(Aerial_ID) FROM Aerials'
    cursor.execute(sql)
    aerial_id = cursor.fetchall()[0][0]

    con.commit()
    cursor.close()
    con.close()
    return aerial_id

def update_aerial(aerial_data):
    print("Inside update aerial data")
    con = connect_db()
    cursor = con.cursor()

    sql = (
        'UPDATE aerials SET class_id = :class_id, aerial_name = :aerial_name, '
        'basket = :basket, hstyle_jack = :hstyle_jack, downjack = :downjack, '
        'stabilizer_spread = :stabilizer_spread, structural_ladder_warranty = :structural_ladder_warranty, '
        'flow_capacity = :flow_capacity, minimum_angle = :minimum_angle, '
        'maximum_angle = :maximum_angle, wind_rating = :wind_rating, ice_rating = :ice_rating, '
        'horizontal_ladder_reach = :horizontal_ladder_reach, vertical_ladder_reach = :vertical_ladder_reach, '
        'dry_payload_capacity = :dry_payload_capacity, wet_payload_capacity = :wet_payload_capacity, '
        'tank = :tank, aerial_cost = :aerial_cost '
        'WHERE aerial_id = :aerial_id'
    )

    cursor.execute(sql, aerial_data)
    con.commit()

    cursor.close()
    con.close()

def delete_aerial(aerial_id):
    print("Inside delete aerial data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'DELETE FROM aerial_pump WHERE aerial_id = {}'.format(aerial_id)
    cursor.execute(sql)

    sql = 'DELETE FROM aerial_chassis WHERE aerial_id = {}'.format(aerial_id)
    cursor.execute(sql)

    sql = 'DELETE FROM aerials WHERE aerial_id = {}'.format(aerial_id)
    cursor.execute(sql)

    con.commit()

    cursor.close()
    con.close()

def get_compatibility(aerial_id):
    print("Inside chassis Compatibility")

    con = connect_db()
    cursor = con.cursor()

    sql = 'select cid from aerial_chassis where aerial_id={}'.format(aerial_id)

    cursor.execute(sql)
    compatible = cursor.fetchall()
    compatible = [i[0] for i in compatible]
    sql = 'select cid, chassis_name from chassis where status=\'ACTIVE\''
    cursor.execute(sql)

    chassis_data = cursor.fetchall()

    print(compatible)
    print(chassis_data)
    cursor.close()
    con.close()
    return compatible, chassis_data

def modify_compatibility(aerial_id,chassis_list):
    print("Inside electricals modify_compatibility data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from aerial_chassis where aerial_id = {}'.format(aerial_id)
    print(sql)
    cursor.execute(sql)

    for cid in chassis_list:
        sql = 'insert into aerial_chassis(cid, aerial_id) values ({}, {})'.format(cid,aerial_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return

def save_pump_compatibility(aerial_id,pump_list):
    print("Inside save_pump_compatibility")
    con = connect_db()
    cursor = con.cursor()

    sql = 'delete from aerial_pump where aerial_id = {}'.format(aerial_id)
    print(sql)
    cursor.execute(sql)

    for pump_id in pump_list:
        sql = 'insert into aerial_pump(aerial_id,pump_id) values ({}, {})'.format(aerial_id,pump_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()
    return

def update_aerial_status(aerial_id,status):
    print("Inside update_aerial_status data")
    con = connect_db()
    cursor = con.cursor()

    sql = 'update aerials set status=\''+status+'\' where aerial_id='+ str(aerial_id)
    print(sql)
    cursor.execute(sql)
    
    if status != 'ACTIVE':
        sql = 'delete from aerial_chassis where aerial_id='+ str(aerial_id)
        print(sql)
        cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()     