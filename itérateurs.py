# Tutoriel Python: itérateurs 



# word = "Hello"

# for letter in word: # iter() / next()
#     print(letter)




# list = [1,2,3,4,5] # list est itérable 

# for value in list:
#     print(value)



# list = [1,2,3,4,5] # list est itérable 
# iterator = iter(list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# list = [1,2,3,4,5] # list est itérable      print(next(iterator))
# iterator = iter(list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))






# list = [1,2,3,4,5] # list est itérable 
# iterator = iter(list)

# while True:
#  try:
#       print(next(iterator))
#  except StopIteration:
#     break



"""
__iter__()  -> iter()
__next__()  -> next()
"""





# class R:
#     def __init__(self,end):
#         if end <= 0 :
#             raise ValueError("Point d'arrêt de l'intervalle invalide")
#         self.current = 0
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.current += 1

#         if self.current > self.end:
#             raise StopIteration
        
#         return self.current - 1
    

# ran =  R (10)

# for v in ran:
#     print(v)




# class R:
#     def __init__(self,end):
#         if end <= 0 :
#             raise ValueError("Point d'arrêt de l'intervalle invalide")
#         self.current = 0
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.current += 1

#         if self.current > self.end:
#             raise StopIteration
        
#         return self.current - 1
    


# try:
#  ran =  R (-10)                           c'est la valeur negative 
# except ValueError as e:
#     print(e)
# else:
#     for v in ran:
#         print(v)









# class R:
#     def __init__(self,end):
#         if end <= 0 :
#             raise ValueError("Point d'arrêt de l'intervalle invalide") 
#         self.current = 0
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.current += 1

#         if self.current > self.end:
#             raise StopIteration
        
#         return self.current - 1
    


# try:
#  ran =  R (40)     # c'est la valeur positive
# except ValueError as e:
#     print(e)
# else:
#     for v in ran:
#         print(v)



class Inventory:  # class list
    def __init__(self,name):
        self.name = name
        self.content = []

    def __iter__(self):
        return iter(self.content)
    
    def __next__(self):
        return next(self.content)
    
    def add(self,item):
        self.content.append(item)


chest = Inventory("Large malle")

chest.add("épée en bois")

chest.add("Potion de soins mineurs")
chest.add("Marque d'honneur")


for item in chest:
    print(item)