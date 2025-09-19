"""
Notation d'une décorateur :

funct = decorator(func)
@decorator 

#callable (fonction,methode)
#int  (14, -26)
# str ("bonjour")
"""

# def decorateur (func):
#     print("-------------------")
#     return func

# def hello ():
#     print("---------------------")
#     print("Hello !")

    
# #age = property(_getage,_setage)
# #func = classmethod(func)

# hello = decorateur(hello)
# def hi():
#     print("Hi  !")

# hello()
# hi()




# def decorateur (func):
#     print("-------------------")
#     return func

# @decorator
# def hello ():
#     print("---------------------")
#     print("Hello !")

    
# #age = property(_getage,_setage)
# #func = classmethod(func)

# hello = decorateur(hello)
# def hi():
#     print("Hi  !")

# hello()
# hi()




# user_logged = True


# def profile():
#     print("Le profil membre....")
    
# profile()






# user_logged = True


# def decorator(func):

#     def wrapper():
#         if user_logged:
#             return func()
#         else:
#             print("Vous devez être connecté.")

#     return wrapper
    
# @decorator

# def profile():
#    print("Le profil membre....")

# profile()


user_logged = False

def decorator(func):
    def wrapper():
        if user_logged:
            return func()
        else:
            print("Vous devez être connecté")
    return wrapper

@decorator

def profile():
    print("Le profil membre...")

profile()