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






# user_logged = False

# def decorator(func):
#     def wrapper():
#         if user_logged:
#             return func()
#         else:
#             print("Vous devez être connecté")
#     return wrapper

# @decorator

# def profile():
#     print("Le profil membre...")

# profile()








# user_logger = False

# def decorator(func):
#     def wrapper():
#         if user_logger:
#             return func()
#         else:
#             print("Vous devez être connecté..")
#     return wrapper

# @decorator

# def profile():
#     print("Le profil membre....")

# def article():
#     print("Les articles...")


# profile()
# article()









# user_logged = False

# def check_user_logged(func):
#     def wrapper():
#         if user_logged:
#             return func()
#         else:
#             print("Vous devez être connecté.")
#     return wrapper


# @check_user_logged
# def profile():
#     print("Le profil membre....")

# @check_user_logged
# def article():
#     print("Les articles......")


# profile()
# article()







# user_name = "jason"

# def check_user(username):
#     def decorator(func):
#         def wrapper():
#             if username == user_name:
#                 return func()
#             else:
#                 print("Utilisateur inconnu...")
#         return wrapper
#     return decorator


# @check_user ("jason")
# def profile():
#     print("Le profil membre....")

# profile()







# user_admin = "jason"

# def check_user(username):
#     def decorator(func):
#         def wrapper():
#             return func
#         if user_admin == user_admin:
#             return func()
#         else:
#             print("Utilisateur Inconnu")
#         return wrapper
#     return decorator

# @check_user("Toto")
# def profil():
#     print("Le profil membre....")

# profil()








# import functools

# user_admin = "jason"

# def check_user(username):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper():
#             """
#                 Le wrapper....
#             """
#             return func
#         if username == user_admin:
#             return func()
#         else:
#             print("Utilisateur Inconnu")
#         return wrapper
#     return decorator

# @check_user("jason")
# def profile():
#     """
#         Page d'accès au profil de l'utilisateur    
#     """
#     print("Le profil membre....")

# help(profile)

















# class player:
#     def __init__(self,name):
#         self._name = name

#     def get_name(self):
#         return self._name
    
#     def set_name(self,name):
#         if len(name) <= 25 :
#             self._name = name
#         else:
#             print("Nom incorrect (25 cractéres max.)")

    
#     def one_method():
#         pass

#     def another_method():
#         pass

#     name = property(get_name,set_name)
#     one_method = staticmethod(one_method)
#     another_method = classmethod(another_method)













# class player:
#     def __init__(self,name):
#         self._name = name

#     def get_name(self):
#         return self._name
    
#     def set_name(self,name):
#         if len(name) <= 25 :
#             self._name = name
#         else:
#             print("Nom incorrect (25 cractéres max.)")

#     @classmethod
#     def one_method():
#         pass

#     @staticmethod
#     def another_method():
#         pass

#     name = property()
#     name.setter(set_name)














# class player:
#     def __init__(self,name):
#         self._name = name
#     @property
#     def get_name(self):
#         return self._name
#     @property.setter
#     def set_name(self,name):
#         if len(name) <= 25 :
#             self._name = name
#         else:
#             print("Nom incorrect (25 cractéres max.)")















# class player:
#     def __init__(self,name):
#         self._name = name
#     @property
#     def get_name(self):
#         return self._name
    
#     @property.setter
#     def set_name(self,name):
#         if len(name) <= 25 :
#             self._name = name
#         else:
#             print("Nom incorrect (25 cractéres max.)")

#     @property.deleter
#     def del_name(self):
#         pass

#     @classmethod
#     def one_method():
#         pass
    
#     @staticmethod
#     def another_method():
#         pass






# def is_logged():
#     pass

# def is_admin():
#     pass


# @is_logged
# @is_admin
# def admin_panel():
#     pass

# admin_panel()






def profilling():
    pass

@profilling
def admin_panel():
    pass

admin_panel()