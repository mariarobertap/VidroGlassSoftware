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

    def printEntryLog(self, cidade):
        print(cidade.get())

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
   

        self.config(bg=controller.backgoung)
        self.controller = controller
        label = Label(self,
                      text="Cadastrar Cliente",
                      font=controller.title_font,
                      bg=controller.backgoung,
                      fg = "white")
        entryCidade = Entry(border_cadastro)
        button = Button(self,
                         text="VOLTAR",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="#3f71d4",
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda: self.clearFrame(border_cadastro, controller))

        
        buttonSumit = Button(border_cadastro,
                         text="SUBMIT",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="green",
                         activebackground="green",
                         activeforeground="white",
                         command= lambda: self.printEntryLog( entryCidade)
                         )



        labelNomeCliente = Label(border_cadastro, text = "Nome cliente:", fg="white", background=controller.backgoung)
        labelTelefone = Label(border_cadastro, text = "Telefone:", fg="white", background=controller.backgoung, )
        labelRua = Label(border_cadastro, text = "Rua:", fg="white", background=controller.backgoung)
        labelEstado = Label(border_cadastro, text = "Estado", fg="white", background=controller.backgoung)
        labelCidade = Label(border_cadastro, text = "Cidade", fg="white", background=controller.backgoung)

        entryNome = Entry(border_cadastro)
        entryRua = Entry(border_cadastro)
        entryEstado = Entry(border_cadastro)


        entryTelefone = Entry(border_cadastro)


        #entry.place(x=150, y=60)
        clicked = StringVar()
        clicked.set("PR")


        drop = OptionMenu(border_cadastro, clicked, "PR", "SP", "RJ", "RS", "SC", "Outro")

        border_cadastro.pack_propagate(0)

        entryCidade.insert(END, 'Campo Mourão')
        border_cadastro.config(bg=controller.backgoung)

        packList = [labelNomeCliente,entryNome,
                    labelTelefone,entryTelefone,
                    labelCidade, entryCidade,
                    labelRua,entryRua,
                    label, border_cadastro, button,
                    labelEstado, drop,
                    buttonSumit]

        self.packEntrys(packList)




            
        

