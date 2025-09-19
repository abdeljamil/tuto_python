"""
Type natifs :
     None ,bool,int,float,bytes,list,dict,set,range,str
autres types:
      Final,Iterable,Iterator,Sized,Sequence,
      List[int],Dict, List, Tuple,Optional,NoReturn,Self,Any,Callable
"""

# def sum_numbers(from_number, to_number):

#     numbers = range(from_number,to_number + 1)

#     return sum(numbers)


# a = 1 

# b = 5 

# print(f"Somme des nombres de {a} à {b} = {sum_numbers(a,b)}")

# # print(type(b))




# """
# Type natifs :
#      bool,int,float,bytes,list,dict,set,range,str
# """

# def sum_numbers(from_number, to_number):

#     numbers = range(from_number,to_number + 1)

#     return sum(numbers)


# a : int = 1 

# b : int = 5 

# print(f"Somme des nombres de {a} à {b} = {sum_numbers(a,b)}")

# someData = 15 

# print(type(someData))

# someData = True 

# print(type(someData))

# someData = (1)

# print(type(someData))
# # print(type(b))





# """
# Type natifs :
#      bool,int,float,bytes,list,dict,set,range,str
# """

# def sum_numbers(from_number, to_number):

#     numbers = range(from_number,to_number + 1)

#     return sum(numbers)


# a : int = 1 

# b : int = 5 

# print(f"Somme des nombres de {a} à {b} = {sum_numbers(a,b)}")

# someData = 15 

# print(type(someData))

# someData = True 

# print(type(someData))

# someData = (1)

# print(type(someData))
# # print(type(b))







# """
# Type natifs :
#      bool,int,float,bytes,list,dict,set,range,str
# """

# def sum_numbers(from_number : int, to_number : int) -> int :

#     numbers = range(from_number,to_number + 1)

#     return sum(numbers)


# a : int = 1 

# b : int = 5 

# print(f"Somme des nombres de {a} à {b} = {sum_numbers(a,b)}")






# """
# Type natifs :
#      bool,int,float,bytes,list,dict,set,range,str
# """

# def sum_numbers(from_number : int, to_number : int) -> int :

#     numbers : range = range(from_number, to_number + 1)
 
#     return sum(numbers)


# a : int = 1 

# b : int = 5 

# print(f"Somme des nombres de {a} à {b} = {sum_numbers(a,b)}")





# def sum_number(from_number : int ,to_number : int) -> int | bool :

#     if from_number == 0 :
#         return False
    
#     numbers : range = range(from_number, to_number + 1)

#     return sum(numbers)


# a : int = 1 

# b : int = 5

# print(f"Somme des nombres de {a} à {b} = {sum_number(a, b)}")










# def sum_number(from_number : int ,to_number : int) -> int | bool :

#     if from_number == 0 :
#         return False
    
#     numbers : range = range(from_number, to_number + 1)

#     return sum(numbers)


# a : int = 1 

# b : int = 5




# from typing import Final

# n = 15 

# print(n) 

# n = 23 

# print (n)






# from typing import Final

# n : Final[int] = 2.3

# print(n) 

# n = 23 

# print (n)







# from collections.abc import Iterable


# def iterate_something (collection:Iterable) -> None :
#     for element in collection:
#         print(element)

# iterate_something([1, 2, 3])
# iterate_something(["bonjour"])
# iterate_something([4, 5, 6])







# from collections.abc import Iterable


# def iterate_something (collection:Iterable[int]) -> None :
#     for element in collection:
#         print(element)

# iterate_something([1, 2, 3])
# iterate_something(["bonjour"])
# iterate_something([4, 5, 6])





# from collections.abc import Iterable


# def iterate_something (collection:Iterable[int]) -> None :
#     for element in collection:
#         print(element)

# iterate_something([1, 2, 3])
# iterate_something([4, 5, 6])








# from collections.abc import Iterable


# def iterate_something (collection:Iterable) -> None :
#     for element in collection:
#         print(element)

# iterate_something([1, 2, 3])
# iterate_something(["236"])
# iterate_something([4, 5, 6])








# from collections.abc import Sized


# def iterate_something (collection:Sized) -> None :
#     pass

# iterate_something([1, 2, 3])
# iterate_something(["236"])
# iterate_something([4, 5, 6])







# from collections.abc import Dict, List, Tuple


# def iterate_something (collection:Dict[int,str]) -> None :
#     pass

# iterate_something({"1":"un", "2": "Deux"})







# from collections.abc import Dict, List, Optional, Tuple


# def iterate_something (collection:Optional[List, Tuple]) -> None :
#     pass




# from collections.abc import Dict, List, Optional, Tuple


# def iterate_something (collection:List[int] = []) -> None :
#     pass







# from collections.abc import Any, List


# def iterate_something (collection:List[Any]) -> None :
#     pass









# # from colletions.abc import
# from typing import Any, List


# def iterate_something (collection:List[Any]) -> None  :
#     pass







# # from collection.abc import 

# from typing import NamedTuple


# class Coord2D(NamedTuple):
    
#     x : int 

#     y : int 

# player_position = Coord2D(16,3)







#  #from collection.abc import 

# from typing import NamedTuple


# class Coord2D(NamedTuple):
    
#     x : int 

#     y : int 

# player_position = Coord2D("ok",3)









# from collection.abc import 

# from typing import NamedTuple


# class Coord2D(NamedTuple):
    
#     x : int 

#     y : int 

# player_position = Coord2D("ok",3, 6)






# from typing import Callable, List

# #<nom>(<arguments avec type...>) <type_retour>:

# def sort_like_this(collection:int, other_thing: float) -> List :
#     pass
# # Fonction sans paramétres : Callable[[],list]
# def some_function(collection: List[int],sort_methode: Callable[[int,float],list]): None
#     pass






# from typing import Callable, List

# #<nom>(<arguments avec type...>) <type_retour>:

# def sort_like_this(*args) -> List :
#     pass
# # Fonction sans paramétres : Callable[[],list]
# def some_function(collection: List[int],sort_methode: Callable[[... ,float],list]) -> None:
#     pass





# def sum (a, b) -> int:
#     return a + b 

# def sum(a: float, b:float) -> float:
#     return a + b

# sum(1,5)





# from typing import Any, overload


# @overload
# def sum(a:int, b:int) -> int: ...

# @overload
# def sum(a: float, b:float) -> float:...

# def sum(a:Any, b: Any) -> Any:
#     return a + b

# print(sum(1,6))
# print(sum(2.6,3.1))







# from typing import Any, overload


# @overload
# def sum(a:int, b:int) -> int: ...

# @overload
# def sum(a: float, b:float) -> float:...

# def sum(a:Any, b: Any) -> Any:
#     # if isinstance(a,<type>):
#     return a + b
#     #elif isinstance(a,<autre_type>):
#     pass

# print(sum(1,6))
# print(sum(2.6,3.1))









# from typing import TypeVar

# T = TypeVar ('T')

# class Group[T]:
#     def __init__(self, value: T) -> None:
#         self.value = value






# type coord2 = tuple[int, int]

# player_position: coord2 = (15,6)
# print(player_position)






# type entier = int 

# player_x:entier = 155



# from typing import TypeAlias

# coord2D: TypeAlias = tuple[int, int]


from typing import NewType

coord2D = NewType["coord2D", tuple[int, int]]

player_position: coord2D = coord2D((144,6))