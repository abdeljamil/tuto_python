# import sys


# pyversion = sys.version_info


# if pyversion.major < 3:
#     print()




# import sys

# pyversion = sys.version_info


# if pyversion.minor < 15 :
#     print("Erreur")





# import sys

# print(sys.executable)





# import sys

# print(sys.getdefaultencoding())




# import sys

# print(sys.path)



# import sys

# for p in sys.path:
#     print(p)




# import sys

# print(sys.platform)






# import sys

# """
#     win 32  : Windows
#     linux   :GNU/Linux
#     darwin  :MacOS
#     cygwin  :Cygwin
# """
# if sys.platform == "linux":
#     print("Nous somme sur GNU/Linux")





# import sys

# if # unproblème :
#     #Message..
#     sys.exit()




  

# import sys

# args = sys.argv

# for arg in args:
#     print(arg)

# print(len(sys.argv) - 1)





# import sys

# args = sys.argv


# print(args[1])





# import os

# try:
#     print(os.getcwd())
# except Error as err:
#     print(err)




# import os

# try:
#     print(os.getcwd())
#     os.chdir("C:/User/jachampagne")
#     print(os.getcwd())
# except Error as err:
#     print(err)





# import os

# try:
#     print(os.listdir())
# except Error as err:
#     print(err)






# import os

# try:
#     for (path,directories,file) in os.walk("."):
#         print(directories)
# except Error as err:
#     print(err)






# import os

# try:
#     for (path,directories,file) in os.walk(".", top=False):
#         print(directories)
# except Error as err:
#     print(err)






# import os

# try:
#     for (path,directories,file) in os.walk(".", top=True):
#         print(directories)
# except Error as err:
#     print(err)






  
# import os

# try:
#     os.mkdir('test',777) # sur linux
# except OSError as err:
#     print(err)






# import os

# try:
#     os.mkdir('test') # sur windowns
# except OSError as err:
#     print(err)






# import os

# try:
#     os.rename('rapport','report')
# except OSError as error:
#     print(error)








# import os

# try:
#     os.remove('test')
# except OSError as error:
#     print(error)









# import os

# try:
#     os.removedirs('test/prog/projets/lua')
# except OSError as error:
#     print(error)






# import os

# print(os.path.exists('test.txt'))





# import os

# print(os.path.realpath('test.txt'))










# import os

# base = 'C:\\Usser\\jachampagne'

# filename = 'prog.py'

# complete_path = os.path.join(base,filename)

# print(complete_path)







# import os

# p = "C:\\User\\jacampagne\\Desktop\\FV\\python\\truc.png"

# print(os.path.split(p))










# import os

# p = "C:\\User\\jacampagne\\Desktop\\FV\\python\\truc.png"

# tpl = os.path.split(p)

# print(tpl[1])






# import os

# good_path= "C:\\User\\jacampagne\\Desktop\\FV\\python\\truc.png"
# user_input_path= "C:\\User\\jacampagne\\Desktop\\FV\\python\\truc.png"

# print(os.path.samefile(good_path,user_input_path))







# import os

# print(os.path.isdir('opérateur_systémes.py'))








# import os

# print(os.path.isfile('opérateur_systémes.py'))






# import os

# print(os.path.islink('opérateur_systémes.py'))






# import os

# file_stats = os.stat('attribus_privés.py')

# print(file_stats)








# import os

# file_stats = os.stat('attribus_privés.py')

# print(f"la taille du fichier:{file_stats.st_size}")




# import os

# file_stats = os.stat('attribus_privés.py')

# print(f"la taille du fichier:{file_stats.st_atime}")



import os

file_stats = os.stat('attribus_privés.py')

print(f"Création du:{file_stats.st_atime}")