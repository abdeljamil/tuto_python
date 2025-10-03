class Item:
    """
    Classe définissait un objet utilisable en jeu
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


#code Principal

it1 = Item("Epée en mousse","Arme","Magnifique épée au tranchant inexistant")
it1.toString()
















# age = 14

# help(age)