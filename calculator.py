from tkinter import *
window = Tk()
window.geometry("500x500")

e = Entry(window, width=64, borderwidth=5)
e.place(x=0,y=0)

def click(num):
    result= e.get()
    e.insert(0, str(result) + str(num))


b1= Button(window, text="1"  , width=12, height=5, command= lambda:click(1))
b2= Button(window, text="2"  , width=12, height=5, command= lambda:click(2))
b3= Button(window, text="3"  , width=12, height=5, command= lambda:click(3))
b4= Button(window, text="4"  , width=12, height=5, command= lambda:click(4))
b5= Button(window, text="5"  , width=12, height=5, command= lambda:click(5))
b6= Button(window, text="6"  , width=12, height=5, command= lambda:click(6))
b7= Button(window, text="7"  , width=12, height=5, command= lambda:click(7))
b8= Button(window, text="8"  , width=12, height=5, command= lambda:click(8))
b9= Button(window, text="9"  , width=12, height=5, command= lambda:click(9))
b0= Button(window, text="0"  , width=12, height=5, command= lambda:click(0))


b1.place(x=0   , y=50  )
b2.place(x=100 , y=50  )
b3.place(x=200 , y=50  )
b4.place(x=0   , y=150 )
b5.place(x=100 , y=150 )
b6.place(x=200 , y=150 )
b7.place(x=0   , y=250 )
b8.place(x=100 , y=250 )
b9.place(x=200 , y=250 )
b0.place(x=100 , y=350 )


def add():
    n1=e.get()
    global i
    global math
    math= "addition"
    i=int(n1)
    e.delete(0, END)

def sub():
    n1=e.get()
    global i
    global math
    math= "subtraction"
    i=int(n1)
    e.delete(0, END)

def mul():
    n1=e.get()
    global i
    global math
    math= "multiplication"
    i=int(n1)
    e.delete(0, END)

def div():
    n1=e.get()
    global i
    global math
    math= "addition"
    i=int(n1)
    e.delete(0, END)


def equal():
    n2=e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    if math == "subtraction":
        e.insert(0, i - int(n2))
    if math == "multiplication":
        e.insert(0, i * int(n2))
    if math == "division":
        e.insert(0, i / int(n2))


def clear():
    e.delete(0, END)


f1=Button(window,text="+", width=12, height=5, command= add)
f2=Button(window,text="-", width=12, height=5, command= sub)
f3=Button(window,text="*", width=12, height=5, command= mul)
f4=Button(window,text="/", width=12, height=5, command= div)
f5=Button(window,text="=", width=12, height=5, command= equal)
f6=Button(window,text="CE",width=12, height=5, command= clear)


f1.place(x=300, y=50  )
f2.place(x=300, y=150 )
f3.place(x=300, y=250 )
f4.place(x=300, y=350 )
f5.place(x=0  , y=350 )
f6.place(x=200, y=350 )

mainloop()