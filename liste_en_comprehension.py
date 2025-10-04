"""
[<expression> for <value> in <list>]
[<expression> for <value> in <list> if <condition> if <condition> if .....]
[[] for <value> in <list>]
"""





# li = [1,2,3,4,5,6,7,8,9]


# for el in li:
#     print(el)





# li = [1,2,3,4,5,6,7,8,9]

# [print(el) for el in li]





# li = [1,2,3,4,5,6,7,8,9]

# nli = []

# for el in li:
#     nli.append(el)

# print(li)
# print(nli)






# li = [1,2,3,4,5,6,7,8,9]

# nli = [el for el in li]

# print(li)
# print(nli)




# li = [1,2,3,4,5,6,7,8,9]

# nli = [el + 1 for el in li]

# print(li)
# print(nli)





# li = [1,2,3,4,5,6,7,8,9]

# nli = [el for el in li if el % 2 == 0]

# print(li)

# print(nli)






# li = [1,2,3,4,5,6,7,8,9]

# nli = [el for el in li if el % 2 == 0 if el > 4]

# print(li)

# print(nli)






# li = [1,2,3,4,5,6,7,8,9]

# nli = [True if el % 2 == 0 else False for el in li]

# print(li)

# print(nli)




# li = [1,2,3,4,5,6,7,8,9]

# nli = ["o" if el % 2 == 0 else "n" for el in li]

# print(li)

# print(nli)




# dli = [

#         [1,2,3,4],
#         [10,20,30,40]
#         [100,200,300,400]
# ]

# print(dli)


dli = [

        [1,2,3,4],
        [10,20,30,40],
        [100,200,300,400]
]

ndli = [el for subli in dli for el in subli]

print(dli)
print(ndli)