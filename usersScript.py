import sys
from my_package.toolsModule import (userNameValidator,passwordValidator,emailValidator,idValidator,jsonRead,passwordChecker)
from my_package.usersCrudModule import (register,login,users,updateUserEmail,statusChanger)

try:
    if len(sys.argv) != 3:
        raise Exception("Ingresa tus credenciales por favor")

    usersDB = jsonRead()
    if len(usersDB) == 0:
        if "admin@email.com" == sys.argv[1] and "admin" == sys.argv[2]:
            register("administrador", "admin", "admin@email.com", "admin", 38)
            print(f"Administrador {sys.argv[1]} logueado con éxito")
        else:
            raise Exception("Credenciales erróneas.")
        
    for user in usersDB:
        if user["email"] == sys.argv[1] and user["password"] == sys.argv[2]:
            print(f"Administrador {user["email"]} logueado con éxito")
            break
        else:
            raise Exception("Credenciales erróneas.")

    loop = True
    while loop:
        print("""
==============
  Bienvenido
==============
1. Login.
2. Register.
3. Listar usuarios.
4. Cambiar estado usuario (sólo administradores).
5. Actualizar el Email.
6. Salir.
""")
        option = input("Ingrese la operacion a realizar: ")
        if option == "2":
            regLoop = True
            while regLoop:
                userName = input('Ingrese su nombre (min 4, max 10, sin números ni símbolos) - "cancelar" para salir al menú.: ')
                if userName == "cancelar":
                    regLoop = False
                    continue
                resultUser = userNameValidator(userName)
                if not resultUser[0]:
                    print(resultUser[1])
                    continue
                else:
                    regLastNameLoop = True
                    while regLastNameLoop:
                        userLastName = input('Ingrese su apellido - "cancelar" para salir al menú: ')
                        if userLastName == "cancelar":
                            regLastNameLoop = False
                            continue
                        resultLastName = userNameValidator(userLastName)
                        if not resultLastName[0]:
                            print(resultLastName[1])
                            continue
                        else:
                            regEmailLoop = True
                            while regEmailLoop:
                                userEmail = input('Ingrese un E-mail válido - "cancelar" para salir al menú: ')
                                if userEmail == "cancelar":
                                    regEmailLoop = False
                                    continue
                                resultEmail = emailValidator(userEmail)
                                if not resultEmail[0]:
                                    print(resultEmail[1])
                                    continue
                                else:
                                    regPassLoop = True
                                    while regPassLoop:
                                        userPass = input('Ingrese su password (min 4, max 8, min una mayúscula, una minúscula, un número) - "cancelar" para salir al menú: ')
                                        if userPass == "cancelar":
                                            regPassLoop = False
                                            continue
                                        resultPass = passwordValidator(userPass)
                                        if not resultPass[0]:
                                            print(resultPass[1])
                                            continue
                                        else:
                                            regAgeLoop = True
                                            while regAgeLoop:
                                                userAge = input('Ingrese su edad - "cancelar" para salir al menú: ')
                                                if userAge == "cancelar":
                                                    regAgeLoop = False
                                                    continue
                                                else:
                                                    print(register(userName, userLastName, userEmail, userPass, userAge))
                                                    break
                                            break
                                    break               
                            break
                    break

        elif option == "1":
            loginLoop = True
            while loginLoop:
                user = input('Ingresa tu email - "cancelar" para salir al menú: ')
                if user == "cancelar":
                    loginLoop = False
                    continue
                else:
                    password = input("Ingresa tu password: ")
                    result = login(user, password)
                    print(result)
                    break
        elif option == "3":
            users()
        elif option == "4":
            adminIdLoop = True
            while adminIdLoop:
                adminId = input('Ingrese su ID de administrador - "cancelar" para salir al menú: ')
                if adminId == "cancelar":
                    adminIdLoop = False
                    continue
                adminIdResult = idValidator(adminId)
                if not adminIdResult[0]:
                    print(adminIdResult[1])
                    continue
                else:
                    userIdLoop = True
                    while userIdLoop:
                        userId = input('Ingrese el ID del usuario a activar - "cancelar" para salir al menú: ')
                        if userId == "cancelar":
                            userIdLoop = False
                            continue
                        userIdResult = idValidator(userId)
                        if not userIdResult[0]:
                            print(userIdResult[1])
                            continue
                        else:
                            print(statusChanger(adminId, userId))
                            break
        elif option == "5":
            passLoop = True
            while passLoop:
                userPass = input('Ingrese su password (min 4, max 8, min una mayúscula, una minúscula, un número) - "cancelar" para salir al menú: ')
                if userPass == "cancelar":
                    passLoop = False
                    continue
                resultPass = passwordChecker(userPass)
                if not resultPass[0]:
                    print(resultPass[1])
                    continue
                else:
                    emailLoop = True
                    while emailLoop:
                        userEmail = input('Ingrese un E-mail válido - "cancelar" para salir al menú: ')
                        if userEmail == "cancelar":
                            emailLoop = False
                            continue
                        resultEmail = emailValidator(userEmail)
                        if not resultEmail[0]:
                            print(resultEmail[1])
                            continue
                        else:
                            print(updateUserEmail(userPass, userEmail))
                            break
                    break
        elif option == "6":
            loop = False
            print("Hasta luego!")
        else:
            print("Vuelva a intentar con una opcion valida.")



except Exception as error:
    print(error)
