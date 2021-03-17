from tkinter import *

window = Tk()

button1 =  Button(window,bg="white",width=10)
button2 =  Button(window,bg="white",width=10)
button3 =  Button(window,bg="white",width=10)
button4 =  Button(window,bg="white",width=10)
button5 =  Button(window,bg="white",width=10)
button6 =  Button(window,bg="white",width=10)
button7 =  Button(window,bg="white",width=10)
button8 =  Button(window,bg="white",width=10)
button9 =  Button(window,bg="white",width=10)

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