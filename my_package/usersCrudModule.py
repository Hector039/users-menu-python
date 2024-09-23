from my_package.clientModule import Client
from my_package.toolsModule import jsonRead, jsonSave

def register(firstName, lastName, email, password, age):
    try:            
        usersDB = jsonRead()
        newId = len(usersDB) + 1
        newClient = Client(firstName, lastName, email, password, age, newId)
        newClient.set_roleChanger()
        usersDB.append(newClient.__dict__)
        jsonSave(usersDB)
        
        return f"Registro exitoso! {newClient} Ya puedes loguearte con tus credenciales."
    except Exception as error:
        print(error)
    
    
def login(email, password):
    try:
        usersDB = jsonRead()
        for user in usersDB:
            if user["email"] == email and user["password"] == password:
                return f"Login correcto! Bienvenido {user["firstName"]}"

        return "Email o password incorrecto, intente nuevamente."                                 
    except Exception as error:
        print(error)

def users():
    try:
        usersDB = jsonRead()
        if len(usersDB) == 0:
            print("Aún no hay usuarios registrados.")
        else:
            print("*****************************")
            for user in usersDB:
                print(f"- ID: {user["id"]} - {user["firstName"]} {user["lastName"]} - Email: {user["email"]} - Rol: {user["role"]} - Estado: {user["status"]}\n")
            print("*****************************")
    except Exception as error:
        print(error)

def statusChanger(adminId, userId):
    try:            
        result = Client.statusChanger(adminId, userId)

        return result
    except Exception as error:
        print(error)

def updateUserEmail(password, newEmail):
    try:            
        result = Client.updateUserEmail(password, newEmail)

        return result
    except Exception as error:
        print(error)