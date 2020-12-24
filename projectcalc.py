import tkinter
expression=""
def press(num):
    global expression
    expression+=str(num)

    strvar.set(expression)


expression=""
def clear():
    global expression
    expression=""
    strvar.set(expression)
expression=""
def equal():
    global expression
    apple = strvar.get()
    store=eval(apple)


    strvar.set(store)


calc=tkinter.Tk()

calc.title("CALCULATOR")
calc.geometry("700x800")
label=tkinter.Label(calc,text="WELCOME TO ABHI CALCULATOR'S WORLD ", bg="red",padx=100,pady=10 ,bd=10).pack(side="top",fill="x")
strvar=tkinter.StringVar()
strvar.set(0)

e1=tkinter.Entry(calc,textvariable=strvar,bd=5,font="Lucida 60 bold").pack(fill="x",ipady=10)

topframe=tkinter.Frame(calc,bd=20)
topframe.pack(side="top")
middleframe=tkinter.Frame(calc,bd=20)
middleframe.pack(side="top")
bottom1frame=tkinter.Frame(calc,bd=20)
bottom1frame.pack(side="top")
bottom2frame=tkinter.Frame(bottom1frame,bd=20)
bottom2frame.pack(side="bottom")
righttop=tkinter.Frame(topframe,bd=20)
righttop.pack(side="right")
rightmiddle=tkinter.Frame(middleframe,bd=20)
rightmiddle.pack(side="right")
rightbottom1=tkinter.Frame(bottom1frame,bd=20)
rightbottom1.pack(side="right")
rightbottom2=tkinter.Frame(bottom2frame,bd=20)
rightbottom2.pack(side="right")
btn1=tkinter.Button(topframe,text=1 ,bd=10,fg="black",bg="blue" ,padx=20 ,pady=10,activebackground="green",activeforeground="yellow" ,command=lambda:press(1)).pack(side="left")
btn2=tkinter.Button(topframe,text=2,bd=10 ,fg="black",bg="blue",padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow" ,command=lambda:press(2)).pack(side="left")
btn3=tkinter.Button(topframe,text=3,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow" ,command=lambda:press(3)).pack(side="left")
btn4=tkinter.Button(middleframe,text=4,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(4)).pack(side="left")
btn5=tkinter.Button(middleframe,text=5,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(5)).pack(side="left")
btn6=tkinter.Button(middleframe,text=6,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(6)).pack(side="left")
btn7=tkinter.Button(bottom1frame,text=7,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(7)).pack(side="left")
btn8=tkinter.Button(bottom1frame,text=8,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(8)).pack(side="left")
btn9=tkinter.Button(bottom1frame,text=9,bd=10 ,fg="black",bg="blue" ,padx=20 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(9)).pack(side="left")
btn0=tkinter.Button(bottom2frame,text=0,bd=10 ,fg="black",bg="blue" ,padx=60 ,pady=10 ,activebackground="green",activeforeground="yellow", command=lambda:press(0)).pack(side="left")
btnstart=tkinter.Button(righttop,text="CE",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=clear).pack(side="right")
btnplus=tkinter.Button(righttop,text="+",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=lambda:press("+")).pack(side="right")
btnminus=tkinter.Button(rightmiddle,text="-",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=lambda:press("-")).pack(side="right")
btnmultiply=tkinter.Button(rightmiddle,text="x",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=lambda:press("*")).pack(side="right")
btndivide=tkinter.Button(rightbottom1,text="/",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=lambda:press("/")).pack(side="right")
btnpercentage=tkinter.Button(rightbottom1,text="%",bd=10 ,fg="black",bg="yellow" ,padx=30 ,pady=10 ,activebackground="white",activeforeground="black", command=lambda:press("%")).pack(side="right")
btnequals=tkinter.Button(rightbottom2,text="=",bd=10 ,fg="black",bg="yellow" ,padx=60 ,pady=10 ,activebackground="white",activeforeground="black", command=equal).pack(side="right")
calc.mainloop()