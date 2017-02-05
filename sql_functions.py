# Here we created methods to work with mysql
from my_first_swp_project import run_query


def insert_friend():
    name = raw_input("nombre: \n")
    email = raw_input("email: \n")
    phone = raw_input("telefono: \n")
    best_frien = raw_input("Mejor amigo?: \n")
    friend_since = raw_input("amigo desde: \n")

    query = "INSERT INTO friends(name, email, phone, best_frien, friend_since) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, email, phone, best_frien, friend_since)

    run_query(query)

def delete_friend():
     name_to_erase = raw_input("Nombre de la persona que desea eliminar:\n")
     query = "DELETE FROM friends WHERE name='%s'" % name_to_erase

     run_query(query)

def show_friends():
    query = "SELECT name, email, phone, best_frien, friend_since FROM friends"
    result = run_query(query)
    print result

def find_friend_by_name():
    name = raw_input("A que amigo buscas?\n")
    query = "SELECT * FROM friends WHERE name='%s'" % name
    result = run_query(query)
    print result

def update_data():
    name_to_edit = raw_input("Que amigo deseas editar? \n")
    data_to_edit = raw_input("Que dato deseas editar de el? \n")
    new_data = raw_input("Cual es el nuevo dato?\n")

    if data_to_edit == 'nombre':
        query = "UPDATE friends SET name='%s' WHERE name='%s'" % (new_data, name_to_edit)
        result = run_query(query)

    elif data_to_edit == 'email':
        query = "UPDATE friends SET email='%s' WHERE name='%s'" % (new_data, name_to_edit)
        run_query(query)

    else:
        query = "UPDATE friends SET phone='%s' WHERE name='%s'" % (new_data, name_to_edit)
        run_query(query)


action = int(raw_input("Que deseas hacer?\n"))
if action is 1:
    insert_friend()
elif action is 2:
    delete_friend()
elif action is 3:
    show_friends()
elif action is 4:
    find_friend_by_name()
else:
    update_data()
