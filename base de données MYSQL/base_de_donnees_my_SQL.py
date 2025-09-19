"""
cursor.rowcount
cursor.lastrowid
"""

# import mysql.connector as MC

# try:
#     conn = MC.connector(host = 'localhost',database = 'datatest', user = 'root', password = '')

#     cursor = conn.cursor()

#     req = 'SELECT * FROM ninjatable'

#     cursor .execute (req)

#     ninjalist = cursor.fetchall()

#     for ninja in ninjalist:

#         print('prenom : {}'.format(ninja[1]))

#     #fetchone,fetchmany, fetchall
# except MC.error as err:

#     print(err)

# finally:

#     if(conn.is_connected()):

#         cursor.close()

#         conn.close()






import mysql.connector as MC

try:
    conn = MC.connector(host = 'localhost',database = 'datatest', user = 'root', password = '')

    cursor = conn.cursor()

    req = 'INSERT INTO `ninjatable`(`ninja_firstname`,`ninja_lastname`) VALUES (%s,%s,%s)'
    infos = (cursor.lastrowid,'Shikamaru','Nara')

    cursor .execute (req,infos)
    conn.commit()

    req = 'SELECT * FROM ninjatable'
    cursor .execute (req)
    
    ninjalist = cursor.fetchall()

    for ninja in ninjalist:

        print('prenom : {}'.format(ninja[1]))

    #fetchone,fetchmany, fetchall
except MC.error as err:

    print(err)

finally:

    if(conn.is_connected()):

        cursor.close()

        conn.close()