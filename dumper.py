import pymysql

connection = pymysql.connect(host='db',
                             user='isucon',
                             password='isucon',
                             db='isubata',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    # Read a single record
    sql = "select name, data from image "
    cursor.execute(sql)
    for i in cursor.fetchall():
        with open(i["name"]) as f:
            f.write(i["data"]) 

