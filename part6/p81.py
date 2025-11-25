from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("My Application")
root.option_add("*Font", "aerial 14 bold")

def submitForm():
    txt = txtName.get()
    display = Label(root,text="Hello " + txt)
    display.place(relx=0.05,rely=0.3)

def showForm():
    global label,txtName,btn,root
    label = Label(root,text="Name")
    label.place(relx=0.05,rely=0.05)
    txtName = Entry(root)
    txtName.place(relx=0.15,rely=0.05)
    btn = Button(root,text="Submit",command=submitForm)
    btn.place(relx=0.05,rely=0.15)
    root.mainloop()
showForm()