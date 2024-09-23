import re
import json

def jsonRead():
    try:
        with open("usersDB.json", "r") as file:
            usersDB = json.load(file)
        return usersDB
    except FileNotFoundError:
        with open("usersDB.json", "w") as file:
            json.dump([], file)
        return []
    

def jsonSave(usersDb):
    with open("usersDB.json", "w") as file:
        json.dump(usersDb, file)

userNamePattern = "^[a-zA-Z]+(([\'\\,\\.\\- ][a-zA-Z ])?[a-zA-Z]*)*$"# patrón de expresión regular, no admite números ni símbolos especiales (excepto comas, puntos y guiones)
passwordPattern = "(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*[0-9]+)"# patrón para password, debe contener al menos una letra minúscula, una mayúscula, un número y tener entre 4 y 8 carácteres.
emailPattern = "^[0-9a-zA-Z]+([0-9a-zA-Z]*[-._+])*[0-9a-zA-Z]+@[0-9a-zA-Z]+([-.][0-9a-zA-Z]+)*([0-9a-zA-Z]*[.])[a-zA-Z]{2,6}$"
idPattern = "^[1-9][0-9]{0,2}$"#sólo número enteros positivos distintos de 0, entre 1 y 999

def userNameValidator(userName):
    if len(userName) < 4 or len(userName) > 10:
        return (False, f"La longitud del nombre de usuario '{userName}' es incorrecto, intente nuevamente. (min 4, max 10)")
    
    result = re.search(userNamePattern, userName)
    if isinstance(result, type(None)):
        return (False, f"El nombre de usuario '{userName}' contiene carácteres no admitidos, intente nuevamente. (sólo carácteres alfabéticos)")
    
    return (True, "")

def passwordValidator(password):
    if len(password) < 4 or len(password) > 8:
        return (False, f"La longitud del password '{password}' es incorrecto, intente nuevamente. (min 4, max 8)")
    result = re.search(passwordPattern, password)
    if isinstance(result, type(None)):
        return (False, f"El password '{password}' contiene carácteres no admitidos, intente nuevamente. (min una mayúscula, una minúscula, un número)")
    return (True, "")

def passwordChecker(password):
    usersDB = jsonRead()
    for user in usersDB:
        if user["password"] == password:
            return (True, "")
    return (False, "Password incorrecto. Intente nuevamente.")

def emailValidator(email):
    result = re.search(emailPattern, email)
    if isinstance(result, type(None)):
        return (False, f"El email '{email}' contiene carácteres no admitidos, intente nuevamente. Ejemplos: juan-perez@ejemplo.com | juan.perez@ejemplo.com | juan_perez@ejemplo.com")
    
    usersDB = jsonRead()
    for user in usersDB:
        if user["email"] == email:
            return (False, f"El email '{email}' ya está registrado, intente nuevamente.")
    return (True, "")
    

def idValidator(id):
    result = re.search(idPattern, id)
    if isinstance(result, type(None)):
        return (False, f"El ID '{id}' contiene carácteres no admitidos, intente nuevamente. (Números enteros, distinto de 0, entre 1 y 999)")
    
    usersDB = jsonRead()
    for user in usersDB:
        if user["id"] == int(id):
            return (True, "")
        
    return (False, f"El ID '{id}' no fué encontrado, intente nuevamente.")
    
    