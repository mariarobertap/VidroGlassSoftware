from tkinter import *
from tkinter import font 

window = Tk()
window.geometry("600x600")

window.title("VidroGlass")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

window.config(background="#203d3f")

label1 = Label(window, text="This is a label in my Window",
                     font=('Arial', 20, 'bold'),
                     background="#203d3f",
                     foreground='white',
                     #relief=RAISED,
                     #bd=10,
                     #padx=50,
                     #pady=50,
                     #image=icon,
                     #compound='bottom'
                     )
label1.pack()


label = Label(window, text="Produto",
                     font=('Arial', 40, 'bold'),
                     background="black",
                     foreground='#5cfcff',
                     #relief=RAISED,
                     #bd=10,
                     #padx=50,
                     #pady=50,
                     #image=icon,
                     #compound='bottom'
                     )
#label.pack()
#label.place(x=0, y=0)


def buttonclick():
    len = entry.get().__len__()
    if(len <= 0):
        print("Campo vazio!")
        return
    print("click :p")
    button.config(state=DISABLED)
    entry.config(state=DISABLED)
    print(entry.get())
    
def delete():
    entry.delete(0, END)


labelbutton = Label(window, text="This is a button in my window",
                     font=('Arial', 20, 'bold'),
                     background="#203d3f",
                     foreground='white',
                     #relief=RAISED,
                     #bd=10,
                     #padx=50,
                     #pady=50,
                     #image=icon,
                     #compound='bottom'
                     )
labelbutton.pack()


button = Button(window,
                text="Submit",
                command=buttonclick,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground="#00FF00"
                #state=ACTIVE,
                #image=icon,
                #compound='bottom'
                )

#button.place(x=0, y=300)
button.pack()

labeldelete = Label(window, text="This is a delete button in my window",
                     font=('Arial', 20, 'bold'),
                     background="#203d3f",
                     foreground='white',
                     #relief=RAISED,
                     #bd=10,
                     #padx=50,
                     #pady=50,
                     #image=icon,
                     #compound='bottom'
                     )
labeldelete.pack()


button_delete = Button(window,
                text="Delete",
                command=delete,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground="#00FF00"
                #state=ACTIVE,
                #image=icon,
                #compound='bottom'
                )
button_delete.pack()
#button_delete.place(x=0, y=80)

labeletry = Label(window, text="This is a entryfield in my window",
                     font=('Arial', 20, 'bold'),
                     background="#203d3f",
                     foreground='white',
                     #relief=RAISED,
                     #bd=10,
                     #padx=50,
                     #pady=50,
                     #image=icon,
                     #compound='bottom'
                     )
labeletry.pack()

entry = Entry(window,
              show="*")
#entry.place(x=150, y=60)
entry.pack()


window.mainloop()
