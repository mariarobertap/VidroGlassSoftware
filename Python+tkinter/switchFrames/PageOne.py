from tkinter import *               

class PageOne(Frame):


    def clearFrame(self, frame, controller):
        # destroy all widgets from frame
      
        controller.show_frame("StartPage")

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def SubmitInformations(self):

        if(len(self.entryNome.get()) <= 0 ):
            self.entryNome.config(bg = 'red')
            return
        else:
            self.db.insertInto(self.entryNome.get(), self.entryCidade.get(), self.clicked.get(), self.entryRua.get(), self.entryTelefone.get())
            print("------------------------------"
                "\nCliente cadastrado:" +self.entryNome.get()+
                "\nCidade:" + self.entryCidade.get() + 
                "\nEstado: "+self.clicked.get()+
                "\nRua: "+self.entryRua.get()+
                "\nTelefone: "+self.entryTelefone.get()+
                "\n------------------------------")


        self.entryNome.delete(0, 'end')
        self.entryRua.delete(0, 'end')
        self.entryTelefone.delete(0, 'end')
        self.entryNome.config(bg = 'white')
  

    def packEntrys(self,PackList):
        for entry in PackList:
            entry.pack()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        border_cadastro = Frame(self,
                                highlightbackground="blue",
                                highlightthickness=4,
                                width=500,
                                height=400,
                                bd= 0)

        self.db = controller.db
        self.entryCidade = Entry(border_cadastro)
        self.entryNome = Entry(border_cadastro)
        self.entryRua = Entry(border_cadastro)
        self.entryTelefone = Entry(border_cadastro)
        self.clicked = StringVar()
        self.clicked.set("PR")

   

        self.config(bg=controller.backgoung)
        self.controller = controller
        self.label = Label(self,
                      text="Cadastrar Cliente",
                      font=controller.title_font,
                      bg=controller.backgoung,
                      fg = "white")



        self.drop = OptionMenu(border_cadastro, self.clicked, "PR", "SP", "RJ", "RS", "SC", "Outro")
        self.button = Button(self,
                         text="VOLTAR",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="#3f71d4",
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda: self.clearFrame(border_cadastro, controller))

        
        self.buttonSumit = Button(border_cadastro,
                         text="SUBMIT",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="green",
                         activebackground="green",
                         activeforeground="white",
                         command= lambda: self.SubmitInformations()
                         )



        labelNomeCliente = Label(border_cadastro, text = "Nome cliente:", fg="white", background=controller.backgoung)
        labelTelefone = Label(border_cadastro, text = "Telefone:", fg="white", background=controller.backgoung, )
        labelRua = Label(border_cadastro, text = "Rua:", fg="white", background=controller.backgoung)
        labelEstado = Label(border_cadastro, text = "Estado", fg="white", background=controller.backgoung)
        labelCidade = Label(border_cadastro, text = "Cidade", fg="white", background=controller.backgoung)

  


        #entry.place(x=150, y=60)


        border_cadastro.pack_propagate(0)

        self.entryCidade.insert(END, 'Campo Mourão')
        border_cadastro.config(bg=controller.backgoung)

        packList = [labelNomeCliente,self.entryNome,
                    labelTelefone,self.entryTelefone,
                    labelCidade, self.entryCidade,
                    labelRua,self.entryRua,
                    self.label, border_cadastro, self.button,
                    labelEstado, self.drop,
                    self.buttonSumit]

        self.packEntrys(packList)




            
        

