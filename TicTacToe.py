from tkinter import *
from functools import partial

window = Tk()

def textchange1(num):
    if num==1:
        button1['text']= 'X'
    
    elif num==2:
        button2['text']= 'X'

    elif num==3:
        button3['text']= 'X'

    elif num==4:
        button4['text']= 'X'

    elif num==5:
        button5['text']= 'X'

    elif num==6:
        button6['text']= 'X'

    elif num==7:
        button7['text']= 'O'

    elif num==8:
        button8['text']= 'X'

    elif num==9:
        button9['text']= 'X'

button1 =  Button(window,bg="white",width=10,command=partial(textchange1,1))
button2 =  Button(window,bg="white",width=10,command=partial(textchange1,2))
button3 =  Button(window,bg="white",width=10,command=partial(textchange1,3))
button4 =  Button(window,bg="white",width=10,command=partial(textchange1,4))
button5 =  Button(window,bg="white",width=10,command=partial(textchange1,5))
button6 =  Button(window,bg="white",width=10,command=partial(textchange1,6))
button7 =  Button(window,bg="white",width=10,command=partial(textchange1,7))
button8 =  Button(window,bg="white",width=10,command=partial(textchange1,8))
button9 =  Button(window,bg="white",width=10,command=partial(textchange1,9))

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