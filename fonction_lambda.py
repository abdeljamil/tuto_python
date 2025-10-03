# Fonction lambda

#lambda [parametres] : [expression ]

# power = lambda n:n **n

# print(power(5))

#Power = lambda n:n ** n#Power = lambda n:n ** n##Power = lambda n:n ** n

#Print (power(4))

#power = lambda n:n**n

#Print (power(2))

#filter(<callback>, <Iterable>)





# def if_positive(n):
# 	return n >= 0
   
# result = filter (lambda n:n > 0, [-3,1,2,-22,136,-5])

# print (list(result))




# result = filter (lambda n : n >= 0,[-3,1,2,-22,136,-5])
# print(list(result))








# import tkinter


# def print_message():
# 	print("L'utilisateur a cliqué sur le bouton " )
# app = tkinter.Tk()

# app.title("Fonction lambda sur un bouton ")

# btn = tkinter.Button(app, text="Cliquez ici",command= print_message )

# btn. pack()
# app.mainloop()





import tkinter


def print_message(message):
    print(f"L'utilisateur a envoyé : {message}")

app = tkinter.Tk()

app.title("Fonction lambda sur un bouton")
app.geometry("300x200")

btn = tkinter.Button(app,text="Cliquez ici",command= lambda: print_message("bonjour"))

btn.pack()
app.mainloop()

