from tkinter import *               
from tkinter import ttk


class PageTwo(Frame):


    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.db = controller.db
        label = Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: self.showinTable())
        button.pack()
        self.config(bg=controller.backgoung)
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3"), show='headings')

        self.tree.column("#1", anchor=CENTER)

        self.tree.heading("#1", text="Nome Cliente")

        self.tree.column("#2", anchor=CENTER)

        self.tree.heading("#2", text="Telefone")

        self.tree.column("#3", anchor=CENTER)

        self.tree.heading("#3", text="Endereco")

        self.tree.pack()

        self.showinTable()


    def showinTable(self):
        rows = self.db.getItem() 


        for item in self.tree.get_children():
             self.tree.delete(item)

        for row in rows:
            print(row) 
            self.tree.insert("", END, values=row)    
