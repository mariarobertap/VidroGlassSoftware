from tkinter import *               
from tkinter import ttk


class PageTwo(Frame):


    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.title_font = controller.title_font
        self.background = controller.backgoung
        self.db = controller.db
        label = Label(self, text="Clientes",
                     font=controller.title_font,
                     background=controller.backgoung,
                     foreground="white")
        label.pack(side="top", fill="x", pady=40)

        self.config(bg=controller.backgoung)
        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4"), show='headings')

        self.tree.column("#1", anchor=CENTER)

        self.tree.heading("#1", text="ID Clietene")

        self.tree.column("#2", anchor=CENTER)

        self.tree.heading("#2", text="Nome Cliente")

        self.tree.column("#3", anchor=CENTER)

        self.tree.heading("#3", text="Endereco")

        self.tree.column("#4", anchor=CENTER)

        self.tree.heading("#4", text="Estado")

        self.tree.pack()

        self.backImage = PhotoImage(file="..\\images\\back.png")
        self.deleteImage = PhotoImage(file="..\\images\\trash.png")
        self.alterImage = PhotoImage(file="..\\images\\pencil.png")
        button1 = Button(self,
                         text="Excluir",
                         font=("Comic Sans", 15),
                         width=220,
                         height=50,
                         fg="white",
                         bg="grey",
                         image=self.deleteImage,
                         compound=LEFT,
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda: self.selectItem()
                         )
        button2 = Button(self,
                         text="Alterar",
                         font=("Comic Sans", 15),
                         width=220,
                         height=50,
                         fg="white",
                         bg="grey",
                         image=self.alterImage,
                         compound=LEFT,
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda: self.alterClient()
                         )

        button3 = Button(self,
                         text="Voltar",
                         font=("Comic Sans", 15),
                         width=220,
                         height=50,
                         fg="white",
                         bg="grey",
                         image=self.backImage,
                         compound=LEFT,         
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda:  controller.show_frame("StartPage")
                         )

        button1.pack()
        button1.place(relx=0.24, rely=0.5)
        button2.pack()
        button2.place(relx=0.43, rely=0.5)
        button3.pack()
        button3.place(relx=0.61, rely=0.5)

        self.showinTable(controller);
        
    
    def showinTable(self, controller):
        
        rows = self.db.getItem() 


        for item in self.tree.get_children():
             self.tree.delete(item)

        for row in rows:
            print(row) 
            self.tree.insert("", END, values=row)    


    def selectItem(self):
        curItem = self.tree.focus()

        if(len(curItem) >= 0):
            
               myselectedValue = self.tree.item(curItem)
               print(myselectedValue)
               id = myselectedValue['values'][0]
               name = myselectedValue['values'][1]
               print("====SELECTED CLIENTE ID ["+str(id)+"]==========")
               print("====SELECTED CLIENTE ["+name+"]==========")

               return myselectedValue
        else:
            return 0
    

    def packEntrys(self,PackList):
        for entry in PackList:
            entry.pack()

    def alterClient(self):

        selectedValues = self.selectItem()

        if(selectedValues == 0):
            print("Nothing was selected")
        
       
        name = selectedValues['values'][1]


        app = Tk()


        border_cadastro = Frame(app,
                                highlightbackground="blue",
                                highlightthickness=4,
                                width=500,
                                height=400,
                                bd= 0)

     
        app.entryCidade = Entry(border_cadastro)
        app.entryNome = Entry(border_cadastro, )
        app.entryRua = Entry(border_cadastro)
        app.entryTelefone = Entry(border_cadastro)
        app.clicked = StringVar()
        app.clicked.set("PR")

        app.entryNome.insert(END, name)
   

  
        app.label = Label(app,
                      text="Cadastrar Cliente",
                      font=self.title_font,
                      bg=self.background,
                      fg = "white")



        app.drop = OptionMenu(border_cadastro, app.clicked, "PR", "SP", "RJ", "RS", "SC", "Outro")
        app.button = Button(app,
                         text="VOLTAR",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="#3f71d4",
                         activebackground="#084dd4",
                         activeforeground="white")
                   

        
        app.buttonSumit = Button(border_cadastro,
                         text="SUBMIT",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="green",
                         activebackground="green",
                         activeforeground="white"
                         )



        labelNomeCliente = Label(border_cadastro, text = "Nome cliente:", fg="white", background=self.background)
        labelTelefone = Label(border_cadastro, text = "Telefone:", fg="white", background=self.background, )
        labelRua = Label(border_cadastro, text = "Rua:", fg="white", background=self.background)
        labelEstado = Label(border_cadastro, text = "Estado", fg="white", background=self.background)
        labelCidade = Label(border_cadastro, text = "Cidade", fg="white", background=self.background)

  


        #entry.place(x=150, y=60)


        border_cadastro.pack_propagate(0)

        app.entryCidade.insert(END, 'Campo Mourão')
        border_cadastro.config(bg=self.background)

        packList = [labelNomeCliente,app.entryNome,
                    labelTelefone,app.entryTelefone,
                    labelCidade, app.entryCidade,
                    labelRua,app.entryRua,
                    app.label, border_cadastro, app.button,
                    labelEstado, app.drop,
                    app.buttonSumit]

        self.packEntrys(packList)
 
        app.eval('tk::PlaceWindow %s center' % app.winfo_toplevel())
        app.mainloop()


           
