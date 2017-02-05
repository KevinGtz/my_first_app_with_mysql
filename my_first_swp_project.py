import MySQLdb

from keys import *

DB_HOST = localhost
DB_USER = user
DB_PASS = mysqlroot
DB_NAME = database_name

def run_query(query=''):
    the_data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*the_data)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()

    return data

# name = raw_input("nombre: \n")
# email = raw_input("email: \n")
# phone = raw_input("telefono: \n")
# best_frien = raw_input("Mejor amigo?: \n")
# friend_since = raw_input("amigo desde: \n")
#
# query = "INSERT INTO friends(name, email, phone, best_frien, friend_since) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, email, phone, best_frien, friend_since)
# name_to_erase = raw_input("Nombre de la persona que desea eliminar:\n")
# query = "DELETE FROM friends WHERE name='%s'" % name_to_erase

# run_query(query)
