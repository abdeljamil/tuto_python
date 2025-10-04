class Item:
    """
    Classe définissant un objet utilisable en jeu
    """
    def __init__(self,name,category,description,costValue = 1):
        self.name = name 
        self.category = category
        self.description = description
        self.costValue = costValue

    def toString (self):
        print("------------------------")
        print("[{} - {}]\n> {}\nPrix d'achat : {} po".format(self.name,self.category,self.description,self.costValue))
        print("-------------------------")
        print(__name__)


#code Principal


age = 24 

print(age.__doc__)

# it1 = Item("Epée en mousse","Arme","Magnifique épée au tranchant inexistant")

# print(it1.__doc__)

# print(it1.name)
# it1.name = "Arc"
# print(it1.name)



# print(it1.name)
# it1.__dict__["name "]= "Arc"
# print(it1.name)


# print(it1.description)    c'est ne pas du tout trop conséille 
# print(it1.__dict__["description"])

#it2 = Item("Arc en bois de hêtre","Arme","Magnifique arc des gends archers")
#it1.toString()

#it1.toString()

# print(id(it1))
# print(id(it2))



#print(dir(it1))

# if __name__ == "__main__":
#     print("Je suis dans la partie principale")


# age = 24 

# print(type(age))

"""
hasttr(), | getattr() | callable() | isinstance() 

"""

#help(isinstance)


# print(isinstance(it1,Item))



#print(it1.__dict__)







# age = 14

# help(age)