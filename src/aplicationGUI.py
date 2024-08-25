from tkinter import *
from tkinter import ttk

class Application():
    def __init__(self, master=None):
        self.defaultFont = ("Arial", "10")
        self.header = Frame(master)
        self.header["pady"] = 25
        self.header.pack()

        self.body = Frame(master)
        self.body["pady"] = 0
        self.body.pack()

        self.boxContainer = Frame(master)
        self.boxContainer["pady"] = 15
        self.boxContainer.pack()

        self.title = Label(self.header, text="Cifra de Cesar")
        self.title["font"] = ("comic sans", "30", "bold")
        self.title.pack()

        self.textInput = Text(self.body, width=34, height=7, wrap=WORD, font=('Arial', '12', 'bold'))#, fg='white', bg='gray')
        self.textInput.pack(side=TOP)
        self.textOutput = Text(self.body, width=34, height=7, wrap=WORD, font=('Arial', '12', 'bold'))#, fg='white', bg='gray')
        self.textOutput.pack(side=BOTTOM, pady=10)

        self.cbSetAction = ttk.Combobox(self.boxContainer, values=("Criptografar", "Descriptografar"), width=13)
        self.cbSetAction.set("Deseja")
        self.cbSetAction.pack(side=LEFT, padx=10)

        self.cbSetNCaracter = ttk.Combobox(self.boxContainer, values=tuple(range(0, 27)), width=5)
        self.cbSetNCaracter.set("Passo")
        self.cbSetNCaracter.pack(side=LEFT, padx=5)

        self.btExecute = Button(self.boxContainer, text="Executar")
        self.btExecute.pack(side=RIGHT, padx=5)