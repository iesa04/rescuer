import cx_Oracle
from home import config

def connect_db():
    con = cx_Oracle.connect(config.db_connect)
    return con

def retrieve_aerial_class_data():
    print("Inside get aerial class list data")
    con = connect_db()
    cursor = con.cursor()

    cursor.execute('SELECT * FROM aerial_class ORDER BY class_name ASC')
    rows = cursor.fetchall()

    aerial_class_dict = {}
    for row in rows:
        aerial_class_dict[row[0]]=row[1]

    cursor.close()
    con.close()
    return aerial_class_dict