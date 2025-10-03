# f = open("myfile.txt","a")

# f.write("hello")

# f.close()



# with open("myfile.txt","a") as f :
#     f.write("hello")


# Le fichier est  fermé

















# """
# Classe : qui va implementer deux méthodes :
#          __enter__()
#          __exit__()
# """

# import threading


# class FileLock:
#     def __init__(self,filename):
#         self.filename = filename
#         self.lock = threading.Lock()

#     def __enter__(self):
#         self.lock.acquire()
#         self.file = open(self.filename,'a')
#         return  self.file
    
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         self.file.close()
#         self.lock.release()

# with FileLock("myfile.txt") as f :
#     f.write("hello world")










from contextlib import ContextDecorator


class SomeContext(ContextDecorator):
    def __enter__(self):
        print("phrase de configuration des ressource.....")
        return self
    
    def __exit__(self,*exc):
        print("phrase de libération des ressources...")
        return False
    
@SomeContext()
def some_func():
    print("Ma function est appelée...")


with SomeContext():
    print("Je m'execute")
