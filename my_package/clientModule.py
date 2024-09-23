import datetime
from my_package.toolsModule import jsonRead, jsonSave


class User:
    def __init__(self, id, status, role, created):
        self.id = id
        self.status = status
        self.role = role
        self.created = created
        
class Client(User):
    date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    def __init__(self, firstName, lastName, email, password, age, id, status=False, role="user", created=date):
        super().__init__(id, status, role, created)
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.age = age
        

    def __str__(self):
        return f"Cliente {self.firstName} {self.lastName}, registrado con email {self.email} en fecha {self.created}"
    
    def set_roleChanger(self):
        if self.password == "admin" and self.email == "admin@email.com":
            self.role = "admin"
            self.status = True

    @staticmethod
    def updateUserEmail(password, newEmail):
        usersDB = jsonRead()
        for user in usersDB:
            if user["password"] == password:
                user["email"] = newEmail
                jsonSave(usersDB)
                return f"Nuevo Email {newEmail} actualizado correctamente."
        
        return "Password de usuario incorrecto."

    @staticmethod
    def statusChanger(adminId, userId):
        usersDB = jsonRead()
        for admin in usersDB:
            if admin["id"] == int(adminId) and admin["role"] == "admin":
                for user in usersDB:
                    if user["id"] == int(userId):
                        if not user["status"]:
                            user["status"] = True
                            jsonSave(usersDB)
                            return f"Usuario ID {userId} activado correctamente."
                        else:
                            user["status"] = False
                            jsonSave(usersDB)
                            return f"Usuario ID {userId} desactivado correctamente."
        return f"Admin ID {adminId} sin privilegios."