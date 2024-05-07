from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("text files","*.txt")))
print (root.filename)