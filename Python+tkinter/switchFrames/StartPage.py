from tkinter import *
from tkinter import font               
from Database import Database

class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.backgoung)
        label = Label(self, text="VIDROGLASS", font=controller.title_font, bg=controller.backgoung, fg="white")
        label.pack(side="top", fill="both", pady=5)
        
        button1 = Button(self,
                         text="Cadastrar Cliente",
                         font=("Comic Sans", 15),
                         width=20,
                         height=2,
                         fg="white",
                         bg="#3f71d4",
                         activebackground="#084dd4",
                         activeforeground="white",
                         command=lambda: controller.show_frame("PageOne")
                         )

        button2 = Button(self, text="Cadastrar Produto",
                            font=("Comic Sans", 15),
                            width=20,
                            height=2,
                            fg="white",
                            bg="#3f71d4",
                            activebackground="#084dd4",
                            activeforeground="white",
                            command=lambda: controller.show_frame("PageTwo"))


        button3 = Button(self, text="Listar Clientes",
                            font=("Comic Sans", 15),
                            width=20,
                            height=2,
                            fg="white",
                            bg="#3f71d4",
                            activebackground="#084dd4",
                            activeforeground="white",
                            command=lambda: controller.show_frame("PageTwo"))

        button4 = Button(self, text="Gerar orçamento/Pedido",
                            font=("Comic Sans", 15),
                            width=20,
                            height=2,
                            fg="white",
                            bg="#3f71d4",
                            activebackground="#084dd4",
                            activeforeground="white",
                            command=lambda: controller.show_frame("PageTwo"))

        button4.pack()                
        button3.pack()                    
        button1.pack()
        button2.pack()
