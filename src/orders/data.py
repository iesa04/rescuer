import cx_Oracle
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def ct_orders_data(fdid):
    print("Inside get ct orders data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT order_id, order_date, status, cost FROM orders WHERE FDID = \'{}\' ORDER BY order_date ASC'.format(fdid))
    order_list = cursor.fetchall()

    cursor.close()
    con.close()

    print(order_list)
    return order_list

def ad_orders_data():
    print("Inside get ad orders data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT order_id, fdid,order_date, status, cost FROM orders ORDER BY order_date ASC')
    order_list = cursor.fetchall()

    cursor.close()
    con.close()

    print(order_list)
    return order_list    


def ct_order_detail_data(order_id):
    print("Inside get ct order detail data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT AERIAL_ID, CID, ENGINE_ID, TRANSMISSION_ID, ELECTRICAL_ID, FRONT_SUSPENSION_ID, REAR_SUSPENSION_ID, PUMP_ID, QUANTITY, SUBCOST FROM order_details WHERE order_id = \'{}\''.format(order_id))
    rows = cursor.fetchall()

    print(rows)
    order_detail = []

    for row in rows:
        row = list(row)
        #Replace numbers with data
        cursor.execute('SELECT AERIAL_NAME FROM aerials WHERE aerial_id = {}'.format(row[0]))
        temp = cursor.fetchall()[0][0]
        row[0] = temp

        cursor.execute('SELECT CHASSIS_NAME FROM chassis WHERE cid = {}'.format(row[1]))
        temp = cursor.fetchall()[0][0]
        row[1] = temp

        cursor.execute('SELECT ENGINE_NAME FROM engine WHERE ENGINE_ID = {}'.format(row[2]))
        temp = cursor.fetchall()[0][0]
        row[2] = temp

        cursor.execute('SELECT TRANSMISSION_NAME FROM TRANSMISSION WHERE tid = {}'.format(row[3]))
        temp = cursor.fetchall()[0][0]
        row[3] = temp

        cursor.execute('SELECT ELECTRICAL_NAME FROM Electrical_System WHERE ELECTRICAL_ID = {}'.format(row[4]))
        temp = cursor.fetchall()[0][0]
        row[4] = temp

        cursor.execute('SELECT Suspension_Name FROM Suspension WHERE SUSPENSION_ID = {}'.format(row[5]))
        temp = cursor.fetchall()[0][0]
        row[5] = temp

        cursor.execute('SELECT Suspension_Name FROM Suspension WHERE SUSPENSION_ID = {}'.format(row[6]))
        temp = cursor.fetchall()[0][0]
        row[6] = temp

        cursor.execute('SELECT Pump_Name FROM Pump WHERE PUMP_ID = {}'.format(row[7]))
        temp = cursor.fetchall()[0][0]
        row[7] = temp

        order_detail.append(row)

        row.append(row[8]*row[9])

        print(row)

    cursor.close()
    con.close()
    return order_detail

def ct_configure_aerial():
    print("Inside get ct configure aerial")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT aerial_id, aerial_name,status FROM aerials where status=\'ACTIVE\' ORDER BY aerial_id ASC')
    aerial_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(aerial_list)
    return aerial_list


def ct_configure_chassis(aerial_id):
    print("Inside get ct configure chassis data")
    print("aerial id : ", aerial_id)
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select CID, Chassis_Name,status from chassis where status=\'ACTIVE\' and cid in (select cid from aerial_chassis where Aerial_ID = {})'.format(aerial_id))
    chassis_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(chassis_list)
    return chassis_list

def ct_configure_engine(chassis_id):
    print("Inside get ct configure engine")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select Engine_ID, Engine_Name from Engine where Engine_Id in (select Engine_Id from chassis_Engine where CID = {})'.format(chassis_id))
    engine_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(engine_list)
    return engine_list

def ct_configure_transmission(chassis_id):
    print("Inside get ct configure transmission")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select TID, Transmission_Name from transmission where TID in (select transmission_id from chassis_Transmission where CID = {})'.format(chassis_id))
    engine_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(engine_list)
    return engine_list

def ct_configure_electricals(chassis_id):
    print("Inside get ct configure electricals")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select electrical_id, Electrical_Name from Electrical_System where electrical_id in (select electrical_id from chassis_electricals where CID = {})'.format(chassis_id))
    electrical_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(electrical_list)
    return electrical_list

def ct_configure_front_suspension(chassis_id):
    print("Inside get ct front susp")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select suspension_id, suspension_Name from suspension where suspension_id in (select front_suspension_id from chassis_frontaxle_suspension where CID = {})'.format(chassis_id))
    front_suspension_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(front_suspension_list)
    return front_suspension_list
    
def ct_configure_rear_suspension(chassis_id):
    print("Inside get ct front susp")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select suspension_id, suspension_Name from suspension where suspension_id in (select rear_suspension_id from chassis_rearaxle_suspension where CID = {})'.format(chassis_id))
    rear_suspension_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(rear_suspension_list)
    return rear_suspension_list

def ct_configure_pump(aerial_id):
    print("Inside get ct pump")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('select pump_id, pump_Name from pump where pump_id in (select pump_id from aerial_pump where aerial_id = {})'.format(aerial_id))
    pump_list = cursor.fetchall()

    cursor.close()
    con.close()
    print(pump_list)
    return pump_list

def ct_configure_summary(order_detail_list):
    con = connect_db()
    cursor = con.cursor()

    order_summary = []
    subcost = 0

    cursor.execute('select Aerial_Name, Aerial_Cost from Aerials where Aerial_id = {}'.format(order_detail_list[0]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]

    cursor.execute('select Chassis_Name, Chassis_Cost from Chassis where CID = {}'.format(order_detail_list[1]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
      
    cursor.execute('select Engine_Name, Engine_Cost from Engine where Engine_id = {}'.format(order_detail_list[2]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
       
    cursor.execute('select Transmission_Name, Transmission_Cost from Transmission where TID = {}'.format(order_detail_list[3]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
       
    cursor.execute('select Electrical_Name, Electrical_Cost from Electrical_System where electrical_id = {}'.format(order_detail_list[4]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
          
    cursor.execute('select suspension_Name, suspension_Cost from Suspension where Suspension_id = {}'.format(order_detail_list[5]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
       
    cursor.execute('select suspension_Name, suspension_Cost from Suspension where Suspension_id = {}'.format(order_detail_list[6]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]
       
    cursor.execute('select pump_Name, pump_Cost from pump where pump_id = {}'.format(order_detail_list[7]))
    row = cursor.fetchall()[0]
    order_summary.append(row[0])
    print(row)
    subcost += row[1]

    cursor.close()
    con.close()       
    print(order_summary)
    return order_summary, subcost

def create_order(request):
    print("Inside create order data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('INSERT INTO Orders(FDID, ORDER_DATE) VALUES (\'{}\',sysdate)'.format(request.session['fdid']))
    cursor.execute('SELECT MAX(Order_ID) FROM ORDERS')
    order_id = cursor.fetchall()[0][0]

    con.commit()
    cursor.close()
    con.close()
    print(order_id)
    return order_id

def place_order(order_id, request):
    print("Inside place order ")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT MAX(Order_ID) FROM ORDERS')
    order_id = cursor.fetchall()[0][0]
    
    order_detail_list = request.session['order_detail_list']

    cost = 0

    for item in order_detail_list:
        cursor.execute('INSERT INTO Order_Details(ORDER_ID, AERIAL_ID , CID , ENGINE_ID , TRANSMISSION_ID, ELECTRICAL_ID, FRONT_SUSPENSION_ID,  REAR_SUSPENSION_ID, PUMP_ID, QUANTITY, SUBCOST ) VALUES({},{},{},{},{},{},{},{},{},{},{})'.format(order_id, item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9]))  
        cost += item[8]*item[9]

    cursor.execute('UPDATE ORDERS SET Cost = {} WHERE Order_ID = {}'.format(round(cost,2), order_id))
    con.commit()
    cursor.close()
    con.close()
    print(order_id)
    return 

def ad_update_order_status(order_id,status):
    print("Inside ad_update_order_status")
    con = connect_db()
    cursor = con.cursor()

    sql = 'update orders set status=\''+status+'\' where order_id='+ str(order_id)
    print(sql)
    cursor.execute(sql)

    con.commit()
    cursor.close()
    con.close()     