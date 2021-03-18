from tkinter import *

window = Tk()

def textchange1():
    button1['text']= 'X'

def textchange2():
    button2['text']= 'O'

def textchange3():
    button3['text']= 'O'

def textchange4():
    button4['text']= 'O'

def textchange5():
    button5['text']= 'O'

def textchange6():
    button6['text']= 'O'

def textchange7():
    button7['text']= 'O'

def textchange8():
    button8['text']= 'O'

def textchange9():
    button9['text']= 'O'

button1 =  Button(window,bg="white",width=10,command=textchange1)
button2 =  Button(window,bg="white",width=10,command=textchange2)
button3 =  Button(window,bg="white",width=10,command=textchange3)
button4 =  Button(window,bg="white",width=10,command=textchange4)
button5 =  Button(window,bg="white",width=10,command=textchange5)
button6 =  Button(window,bg="white",width=10,command=textchange6)
button7 =  Button(window,bg="white",width=10,command=textchange7)
button8 =  Button(window,bg="white",width=10,command=textchange8)
button9 =  Button(window,bg="white",width=10,command=textchange9)

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