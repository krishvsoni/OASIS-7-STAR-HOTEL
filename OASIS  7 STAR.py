from tkinter import *
import tkinter.messagebox as tmsg


hotel = Tk()
hotel.title("OASIS 7 STAR ")
hotel.geometry("780x650")
hotel.wm_maxsize(780,650)
hotel.configure(bg='light green')

def getvals():
    print("Sending To OASIS 7 STAR")
    print(f"{nameval.get() , genderval.get() ,  phoneval.get() ,emailval.get()}\n")

    with open("k.txt","a") as f:
        f.write(f"{nameval.get(), genderval.get(),   phoneval.get(), emailval.get()}\n")

def myfunc():
    print("LABEL")


def rate():
    print("Rate us")
    value = tmsg.askquestion("?", "STAYING HERE.. Was your experience Great?")
    if value == "yes":
        msg = "Great. Rate us on PlayStore"
    else:
        msg = "Please let us know what went wrong , will sure work for it .."
    tmsg.showinfo("Experience", msg)

def help():
    print("WE ARE HERE TO HELP YOU")
    tmsg.showinfo("Help", "For HELP please contact us on help@oasis7star.com")

Label(text="Welcome To OASIS 7 STAR HOTEL",font="comicsansms 18 bold",padx=30,fg="blue",bg="light blue",pady=50    ).grid(row=0,column=3)


name = Label(hotel, text="NAME :")
gender =Label(hotel, text="GENDER :")
phone = Label(hotel, text="PHONE :")
email = Label(hotel, text="EMAIL :")

name.grid(row=  6 , column = 1,pady=10 )
gender.grid(row=  7 , column = 1,pady=10  )
phone.grid(row=  8, column =  1 ,pady=10)
email.grid(row=  9 , column =  1,pady=10 )



nameval=StringVar()
genderval=StringVar()
phoneval=StringVar()
emailval=StringVar()
#tc = Intvar()

nE = Entry(hotel,textvariable=nameval)
gE = Entry(hotel,textvariable=genderval)
pE = Entry(hotel,textvariable=phoneval)
eE = Entry(hotel,textvariable=emailval)

nE.grid(row= 6 , column =  2)
gE.grid(row= 7 , column =  2)
pE.grid(row=  8, column =  2)
eE.grid(row=  9, column = 2 )


tc=Checkbutton(text="I Had Read All Terms & Conditions ..")
tc.grid(row=14,column=3)

button  = Button(hotel,text="SUMBIT",command=getvals)
button.grid(row=16,column=3)

mainmenu = Menu(hotel)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
hotel.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
hotel.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label = "Help", command=help)
m3.add_command(label = "Rate us", command=rate)

mainmenu.add_cascade(label="Help", menu=m3)
hotel.config(menu=mainmenu)


hotel.mainloop()
