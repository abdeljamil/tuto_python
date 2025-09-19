# class Player:
#     def __init (self,name,level):
#         self.name = name
#         self.leve = level

# P = Player ("Chuck NORRIS",50)

"""
Boutons,étiquettes, champs de texte, tableaux
"""

# from abc import ABC, abstractmethod


# class Widget (ABC):
#     def test(self):
#         print("Test !")

#     @classmethod
#     @abstractmethod
#     def render(self):
#         pass


# class Button(Widget):
#     def render(self):
#         print("Rendu d'une bouton......")

# class Label(Widget):
#     def render(self):
#         print("Rendu d'une étiquette.....")

# class TextField(Widget):
#         def test(self):
#             print("Nouveau Test !")

#         def render(self):
#            print("Rendu d'un champ de text....")


# btn = Button()
# btn.test()
# btn.render()


 
# txf = TextField()
# txf.test()
# txf.render()



















from abc import ABC, abstractmethod


# Une interface
class Widget (ABC):

    @classmethod
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def command(self):
        pass

    @abstractmethod
    def pack(self):
        pass
