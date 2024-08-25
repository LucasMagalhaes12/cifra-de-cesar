from tkinter import Tk
from aplicationGUI import Application
from cesarEncryption import *

root = Tk()
root.title("CifraPy")
root.geometry("400x480")
root.resizable(0, 0)

Application(root)
root.mainloop()

