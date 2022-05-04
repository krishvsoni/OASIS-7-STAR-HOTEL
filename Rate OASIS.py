from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.wm_maxsize(455,233)
root.title("Rate OASIS 7 STAR")

def getrate():
    print(f" {myslider2.get()} ")
    tmsg.showinfo("RATED!", f"You have rated {myslider2.get()} points to us ")

    with open("k.txt","a") as f:
        f.write(f"CUSTOMER RATING : {myslider2.get()}\n")


Label(root, text="RATE US BETWEEN 0 to 10").pack()
myslider2 = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=5)


myslider2.pack()


Button(root, text="RATE", pady=10 , padx=10,bg='blue' , fg = 'white', command=getrate).pack()

root.mainloop()