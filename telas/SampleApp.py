from tkinter import *               
from tkinter import font  
from PageOne import PageOne
from PageTwo import PageTwo
from DefaultPage import StartPage
from Database import Database
from invoiceGenerator import start


class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = font.Font(family='Helvetica', size=40, weight="bold", slant="italic")
       
        self.backgoung = "#cfcbca"
        self.db = Database()
        self.state('zoomed')
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        self.container = container
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        self.createDefaultButtons()
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if(page_name == "PageTwo"):
            frame.showinTable(self)

    def cleanAndShowFrame(self, page_name):
        frame = self.frames[page_name]
        for widgets in frame.winfo_children():
            widgets.destroy()
        frame = PageTwo(self.container, self)
        frame.mainloop()

    def createDefaultButtons(self):
        self.config(bg=self.backgoung)
        self.buttonActiveColor =   "#0E7173"
        self.buttonInactiveColor = "#737574"
        self.render = PhotoImage(file="..\\images\\userImage2.png")
        self.invoice = PhotoImage(file="..\\images\\invoice.png")
        self.produto = PhotoImage(file="..\\images\\produto.png")
        self.border_menu = Frame(self,
                            highlightthickness=4,
                            width=240,
                            height=1000,
                            background="grey",
                            bd= 0)

        self.border_top = Frame(self,
                            highlightthickness=4,
                            width=2000,
                            height=100,
                            background="#303133",
                            bd= 0)

        self.ButtonCadastrarCliente = Button(self,
                         text="Cadastrar Cliente",
                         font=("Comic Sans", 15),
                         width=225,
                         height=100,
                         fg="white",
                         bg=self.buttonInactiveColor,
                         image=self.render,
                         compound=LEFT,
                         command=lambda: self.show_frame("PageOne")
                         )

        self.ButtonCadastrarProduto = Button(self, text="Cadastrar Produto",
                            font=("Comic Sans", 15),
                            width=225,
                            height=100,
                            fg="white",
                            bg=self.buttonInactiveColor,
                            image=self.produto,
                            compound=LEFT,
                            command=lambda: self.show_frame("PageTwo"))

      
        self.ButtonListarClientes = Button(self, text="Listar Clientes",
                            font=("Comic Sans", 15),
                            fg="white",
                            image=self.render,
                            compound=LEFT,
                            width=225,
                            height=100,
                            bg=self.buttonInactiveColor,
                            command=lambda: self.show_frame("PageTwo"))

        self.ButtonGerarNota = Button(self, text="     Gerar nota",
                            font=("Comic Sans", 15),
                            width=225,
                            height=100,
                            fg="white",
                            bg=self.buttonInactiveColor,
                            image=self.invoice,
                            compound=LEFT,
                            command=lambda: start())

        self.label = Label(self,
                text="VIDROGLASS",
                font=self.title_font,
                bg="#303133",
                fg="white")

    def showDefaultButtons(self, page):
        page.controller = self
        page.config(bg=self.backgoung)
        page.buttonActiveColor =   "#0E7173"
        page.buttonInactiveColor = "#737574"
        


        
 
        page.controller.border_menu.place(x=0, y=0)
        page.controller.border_top.place(x=0,y=0)
    
        page.controller.ButtonListarClientes.place(x=2, y=100)
        page.controller.ButtonGerarNota.place(x=2, y=235)
        page.controller.ButtonCadastrarCliente.place(x=2, y=370)
        page.controller.ButtonCadastrarProduto.place(x=2, y=505)

        page.controller.ButtonCadastrarCliente.bind("<Enter>", page.on_enter)
        page.controller.ButtonCadastrarCliente.bind("<Leave>", page.on_leave)
        page.controller.ButtonListarClientes.bind("<Enter>", page.on_enter)
        page.controller.ButtonListarClientes.bind("<Leave>", page.on_leave)
        page.controller.ButtonGerarNota.bind("<Enter>", page.on_enter)
        page.controller.ButtonGerarNota.bind("<Leave>", page.on_leave)
        page.controller.ButtonCadastrarProduto.bind("<Enter>", page.on_enter)
        page.controller.ButtonCadastrarProduto.bind("<Leave>", page.on_leave)
        page.controller.label.place(relx=.5, rely=.05, anchor="center")

if __name__ == "__main__":
    app = SampleApp()

    app.mainloop()