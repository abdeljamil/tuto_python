#coding:utf-8

#-----------------------------------------------------------
# Syntaxe,
#------------------------------------------------------------

"""
__repr__()
__str__()
"""
"""name = "Jason"

print("Je m'appelle",name)
"""
"""
d1 = "Hello"
d2 = 14
d3 = 316.344
d4 = True
d5 = (12,21)
d6 = [1,2,3,"OK"]
print(d1,d2,d3,d4,d5,d6)"""

#-----------------------------------------------------------
# Syntaxe %
#------------------------------------------------------------

"""name ="Jason"

print("Je m'appelle %s" % name) # % (name,other,andother)"""

"""name = "Jason"

age = 29

print("Je m'appelle %s et j'ai %d ans" % ((name,age)))"""


#-----------------------------------------------------------
# Syntaxe avec format()
#------------------------------------------------------------
"""age = 29 
text = "Bonjour {} et j'ai {} ans".format("Jason",age) 
print(text)"""

"""number = 164.32641

print("{:.2f}".format(number))"""


"""
text = "Jason"
print("{:>15}".format(text))""" 

"""
text = "Jason"

print("{:10}/{}".format(text,"test"))"""


"""dic = {"name" : "Jason"}
print("{name}".format(**dic))"""

#-----------------------------------------------------------
# syntaxe "f-string"
#------------------------------------------------------------


"""
name = "Jason"

print(f"Je m'appelle {name}")"""


li = [1,2,3]

print(f"{li}")