from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('1000x626+100+50')
root.title('Talking Dictionary')
root.resizable(False, False)


BgImage = PhotoImage(file='bg.png')

bgLabel = Label(root, image=BgImage)
bgLabel.place(x=0, y=0)

EnterWordLabel = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), foreground='red3', background='white')
EnterWordLabel.place(x=530, y=20)

EnterWordEntry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief="GROOVE", justify=CENTER)
EnterWordEntry.place(x=510, y=80)

root.mainloop()

