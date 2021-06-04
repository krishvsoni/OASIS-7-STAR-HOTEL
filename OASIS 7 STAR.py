from tkinter import *
hotel = Tk()
hotel.title("OASIS 7 STAR ")
hotel.geometry("780x650")
hotel.wm_minsize(780,650)
hotel.configure(bg='yellow')

def getvals():
    print("Sending To OASIS 7 STAR")
    print(f"{nameval.get() , genderval.get() ,  phoneval.get() ,emailval.get()}\n")

    with open("k.txt","a") as f:
        f.write(f"{nameval.get(), genderval.get(),   phoneval.get(), emailval.get()}\n")




Label(text="Welcome To OASIS 7 STAR HOTEL",font="comicsansms 18 bold",padx=30,fg="white",bg="black",pady=150    ).grid(row=0,column=3)


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
hotel.mainloop()
