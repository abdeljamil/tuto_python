import tkinter

# app = tkinter.Tk()

# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.pack()
# app.mainloop()






# def func (event):
#     print("La touche [A] a été pressée")

# app =  tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)
# entry_w.bind('<KeyPress-a>',func)


# entry_w.pack()
# app.mainloop()






# def func(event):
#     print("La touche [A] a été pressée")


# app = tkinter.TK()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)
# entry_w.bind('<Button-1>',func)
# entry_w.bind('<Button-2>',func)
# entry_w.bind('<Button-3>',func)

# entry_w.pack()
# app.mainloop()







# def func(event):
#     print("La touche [A] a été pressée")


# app = tkinter.TK()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)
# entry_w.bind('<Button-1>',func)
# entry_w.bind('<KP_minus>',func)
# entry_w.bind('<KP_Enter>',func)

# entry_w.pack()
# app.mainloop()







# def func(event):
#     print("La touche [A] a été pressée")


# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)
# entry_w.bind('<Control-Alt-a>',func)

# entry_w.pack()
# app.mainloop() 








# def func(event):
#     print("La touche [A] a été  pressée")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind('<Double-a>',func)

# entry_w.pack()
# app.mainloop()







# def func(event):
#     print("Ok")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind('<Double-Button-1>',func)

# entry_w.pack()
# app.mainloop()







# def func(event):
#     print("Ok")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind('<Key>',func)

# entry_w.pack()
# app.mainloop()





# def func(event):
#     print("Ok")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind('<Button>',func)

# entry_w.pack()
# app.mainloop()













# def func(event):
#     print("Ok")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind_class('Entry','<Double-Button-1',func)

# entry_w.pack()
# app.mainloop()







# def func(event):
#     print("Ok")

# app = tkinter.Tk()
# app.geometry('320x240')

# entry_w = tkinter.Entry(app)

# entry_w.bind_all('Entry','<Double-Button-1',func)

# entry_w.pack()
# app.mainloop()








# def openwindown():
#     top =  tkinter.Toplevel()
#     label_w = tkinter.Label(top,text= 'Bonjour')
#     label_w.pack()


# app = tkinter.Tk()

# app.geometry('320x240')

# button_w = tkinter.Button(app,text='Ouvrir une fênetre',command= openwindown)


# button_w.pack()
# app.mainloop()





# def func(event):
#     print("La fênetre a été fermée")

# def openwindown():
#     top =  tkinter.Toplevel()
#     label_w = tkinter.Label(top,text= 'Bonjour')
#     label_w.bind('<Destroy>',func)
#     label_w.pack()


# app = tkinter.Tk()

# app.geometry('320x240')

# button_w = tkinter.Button(app,text='Ouvrir une fênetre',command= openwindown)


# button_w.pack()
# app.mainloop()













# """
# x, y, x_root, y_root
# width, heigth 
# state 
# Keysym,Keycode

# """


# def func(event):
#     print("{}/{}".format(event.Keysym,event.keyCode))
#     event.widget.destroy()
#     print("Fênetre fermée")


# def openwindown():
#     top =  tkinter.Toplevel()
#     label_w = tkinter.Label(top,text= 'Bonjour')
#     label_w.bind('<Escape>',func)
#     label_w.pack()


# app = tkinter.Tk()

# app.geometry('320x240')

# button_w = tkinter.Button(app,text='Ouvrir une fênetre',command= openwindown)

# button_w.pack()
# app.mainloop()



def func(event):
    print("Un clic s'est produit ")

app = tkinter.Tk()

app.geometry('320x240')

label = tkinter.Label(app,text='Hello world !!')


app.event_add('<<click>>','<Button-1>','<Button-2>','<Button-3>')

app.bind('<<click>>',func)

label.pack()
app.mainloop()