import tkinter

import game


def open():
    game.run()

app = tkinter.Tk()

app.title("Mon app tkinter")

app.geometry("300x100")

lb = tkinter.Label(app,text="Cliquer sur le bouton....").pack()

bt = tkinter.Button(app,text="Hack tkinter",command=open).pack()

app.mainloop
