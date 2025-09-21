"""
    Commande (en ligne) : vide
                        en attente
                        payée
                        annulée
"""

# import enum

#Une premiére façon de définir une énumération
#OrderStatus = enum.Enum("OrderStatus", ["NOTHING","PENDING","PAID","CANCELLED"])


#Une autre façon de définir une numération



# class OrderStatus(enum.Enum):
#     NOME = enum.auto() #1
#     PENDING = enum.auto()
#     PAID = enum.auto()
#     CANCELLED = enum.auto()




# class OrderStatus(enum.Enum):
#     NOME = 5 #1
#     PENDING = enum.auto()
#     PAID = enum.auto()
#     CANCELLED = enum.auto()

#Cas d'usage.....




# order_status = OrderStatus.NONE

# print(order_status.value)
# print(order_status.name)

# print(type(order_status))





# order_status = OrderStatus.PAID

# print(order_status.value)
# print(order_status.name)

# print(type(order_status))






# order1 = OrderStatus.NOME # à quoi cela correspond.....
# order2 = OrderStatus.NOME


# if order1 == OrderStatus.NOME:
#     print("Oui, La commande est vide")

# if order1 ==order2:
#     print("Oui,même statut pour les deux commandes")




# ods = OrderStatus.PENDING
# print(id(ods))

# ods = OrderStatus.PAID
# print(id(ods))






# import enum


# class OrderStatus(enum.StrEnum):
#     NONE = "Vide"
#     PENDING = "En attente de paiement"
#     PAID = "Payée"
#     CANCELLED = "Annulée"


# order_status = OrderStatus.PENDING

# if order_status == OrderStatus.PENDING:
#     print("En attente de paiement par le client")







# import enum


# class OrderStatus(enum.StrEnum):
#     NONE = 1
#     PENDING = 2
#     PAID = 1
#     CANCELLED = 3


# ods = OrderStatus.PENDING

# print(ods)




# import enum

# @enum.verify(enum.UNIQUE)
# class OrderStatus(enum.Enum):
#     NONE = 1
#     PENDING = 2
#     PAID = 1
#     CANCELLED = 3


# ods = OrderStatus.PENDING
# print(ods)






# import enum


# @enum.unique
# class OrderStatus(enum.Enum):
#     NONE = 1
#     PENDING = 2
#     PAID = 4
#     CANCELLED = 3



# ods = OrderStatus.PENDING
# print(ods)








# import enum


# @enum.verify(enum.CONTINUOUS)
# class OrderSatus(enum.Enum):
#     NONE = 1
#     PENDING = 2 
#     PAID = 3 
#     CANCELLED = 4


# ods = OrderSatus.PENDING
# print(ods)








import enum


@enum.verify(enum.CONTINUOUS)
class OrderSatus(enum.Enum):
    NONE = 1
    PENDING = 2 
    PAID = 3 
    CANCELLED = 6


ods = OrderSatus.PENDING
print(ods)