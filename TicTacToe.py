from tkinter import *
from functools import partial

window = Tk()

clicked=True
count=0

board = ["","","","","","","","",""]

def textchange1(btn,index):
    global clicked, count
    if btn['text']=="" and clicked==True:
        btn['text']="X"
        board[index]="X"
        clicked=False
        count = count+1

    elif btn['text']=="" and clicked==False:
        btn['text']="O"
        board[index]="O"
        clicked=True
        count=count+1
    print(board)
    
button1 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button1,0))
button2 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button2,1))
button3 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button3,2))
button4 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button4,3))
button5 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button5,4))
button6 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button6,5))
button7 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button7,6))
button8 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button8,7))
button9 =  Button(window,bg="white",width=10,text="",command=lambda:textchange1(button9,8))

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