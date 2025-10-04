# class Lapin:
#     def __init__(self,name,weigth):
#         self.name = name
#         self.weigth = weigth

#     def hello(self):
#         print("hello !:")



# lp = Lapin("coco",25)
# lp.hello()





# class Lapin:
#     def __init__(self,name,weigth):
#         self.name = name
#         self.weigth = weigth

#     def hello(self):
#         print("hello !:")
    
#     def __repr__(self):
#         return "Lapin {} de {}kg.".format(self.name,self.weigth)


# lp = Lapin("coco",25)
# print(lp)





class Lapin:
    def __init__(self,name,weigth):
        self.name = name
        self.weigth = weigth

    def hello(self):
        print("hello !:")
    
    def __repr__(self):
        return "Lapin {} de {}kg.".format(self.name,self.weigth)


lp = Lapin("coco",25)
lp2 = Lapin ("Titi",7)

if lp == lp2:
    print("Ce sont les mêmes")

else:
    print("Ces lapins sont différents")
