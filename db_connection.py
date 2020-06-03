import pymysql.cursors

def connect():
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='zeus7777',
                                 db='shema',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def input_contry(conn,id_user,contry):
    cursor = conn.cursor()
    command = f"INSERT INTO requests (id_user, contry) VALUES (%s, %s)"
    cursor.execute(command, (id_user, contry))
    conn.commit()


def input_type_ip(conn,id_user,ip):
    cursor = conn.cursor()
    sql = "Update requests set type_ip = %s where id_user = %s "
    cursor.execute(sql, (ip,id_user))
    conn.commit()


def input_type_blacklists(conn,id_user,type):
    cursor = conn.cursor()
    sql = "Update requests set type_blacklists = %s where id_user = %s "
    cursor.execute(sql, (type,id_user))
    conn.commit()


def input_city(conn,id_user,city):
    cursor = conn.cursor()
    sql = "Update requests set city = %s where id_user = %s "
    cursor.execute(sql, (city,id_user))
    conn.commit()


def input_zip(conn,id_user,zip):
    cursor = conn.cursor()
    sql = "Update requests set zip = %s where id_user = %s "
    cursor.execute(sql, (zip,id_user))
    conn.commit()

def input_ip(conn,id_user,ip):
    cursor = conn.cursor()
    sql = "Update requests set ip = %s where id_user = %s "
    cursor.execute(sql, (ip, id_user))
    conn.commit()



def delete_request(conn,id_user):
    cursor = conn.cursor()
    sql = "Delete from requests where id_user = %s"
    cursor.execute(sql, (id_user))
    conn.commit()


def select_request(conn,id_user):
    cursor = conn.cursor()
    sql = "SELECT* FROM requests where id_user = %s"
    cursor.execute(sql, (id_user))
    return cursor

def reg_user(conn,id_user,nickname):
    c = conn.cursor()
    sql = f"INSERT INTO users (id_user, nickname,balance) VALUES (%s, %s, %s)"
    c.execute(sql, (id_user, nickname,0))
    conn.commit()

def select_users(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    return cursor

def add_funds(conn,id,sum):
    c = conn.cursor()
    bal = get_balanse(get_user_dict_balanse(conn,id))
    bal+=sum
    sql = "Update users set balance = %s where id_user = %s"
    c.execute(sql, (bal, id))
    conn.commit()

def reduce_funds(conn,id,sum):
    c = conn.cursor()
    bal = get_balanse(get_user_dict_balanse(conn,id))
    if bal < sum:
        bal-=sum
        sql = "Update users set balance = %s where id_user = %s"
        c.execute(sql, (bal, id))
        conn.commit()
        return True
    else:
        return False


def get_user_dict_balanse(conn,id):
    cursor = conn.cursor()
    sql = "SELECT balance FROM users where id_user = %s "
    cursor.execute(sql,(id))
    return cursor

def get_balanse(dict):
    for d in dict:
        return d['balance']



