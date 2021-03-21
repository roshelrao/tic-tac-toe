from tkinter import *
from functools import partial

window = Tk()

clicked=True
count=0

def textchange1(num):
    global clicked, count
    if num['text']=="" and clicked==True:
        num['text']="X"
        clicked=False
        count = count+1

    elif num['text']=="" and clicked==False:
        num['text']="O"
        clicked=True
        count=count+1
    
button1 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button1))
button2 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button2))
button3 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button3))
button4 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button4))
button5 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button5))
button6 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button6))
button7 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button7))
button8 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button8))
button9 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button9))

button1.grid(row=0,column=0, sticky="w", padx=3,pady=2)
button2.grid(row=0,column=1, sticky="w", padx=3,pady=2)
button3.grid(row=0,column=2, sticky="w", padx=3,pady=2)
button4.grid(row=1,column=0, sticky="w", padx=3,pady=2)
button5.grid(row=1,column=1, sticky="w", padx=3,pady=2)
button6.grid(row=1,column=2, sticky="w", padx=3,pady=2)
button7.grid(row=3,column=0, sticky="w", padx=3,pady=2)
button8.grid(row=3,column=1, sticky="w", padx=3,pady=2)
button9.grid(row=3,column=2, sticky="w", padx=3,pady=2)

window.mainloop()