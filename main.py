from tkinter import *
base = Tk()
base.geometry("500x500")
base.title("registration form")
base.maxsize(500,500)

lb1 = Label(base, text="Registration Form", width=40, font=("arial",12),fg="red")
lb1.place(x=50, y=70)

lb2 = Label(base, text="Enter First Name", width=10, font=("arial",12))
lb2.place(x=20, y=120)
en2 = Entry(base)
en2.place(x=200, y=120)

lb2 = Label(base, text="Enter Second Name", width=10, font=("arial",12))
lb2.place(x=20, y=160)
en2 = Entry(base)
en2.place(x=200, y=160)

lb3 = Label(base, text="Enter Email", width=10, font=("arial",12))
lb3.place(x=19, y=200)
en3 = Entry(base)
en3.place(x=200, y=200)

lb4 = Label(base, text="Contact Number", width=13,font=("arial",12))
lb4.place(x=19, y=240)
en4 = Entry(base)
en4.place(x=200, y=240)

lb5 = Label(base, text="Select Gender", width=15, font=("arial",12))
lb5.place(x=5, y=260)
vars = IntVar()
Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=180, y=260)
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=240,y=260)

lb6 = Label(base, text="Enter Password", width=13,font=("arial",12))
lb6.place(x=19, y=300)
en6 = Entry(base, show='*')
en6.place(x=200, y=300)

lb7 = Label(base, text="Re-Enter Password", width=15,font=("arial",12))
lb7.place(x=21, y=340)
en7 = Entry(base, show='*')
en7.place(x=200, y=340)

Button(base, text="Register", width=10).place(x=200,y=400)
base.mainloop()
