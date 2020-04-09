import os
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import acer

# FILE_TYPES = [(label1, pattern1), (label2, pattern2), ...]
FILE_TYPES = [
            ('video Files', '.avi .mp4'),
            ('image Files', '.jpg .png .bmp'),
            ('All Files', '.*')
        ]

HOME = os.path.expanduser("~")

root = tk.Tk()
ivn = tk.StringVar()
path = tk.Entry(root,textvariable=str(ivn))

def open_file():
    pathstr = tk.filedialog.askopenfilename(parent=root,
                                         filetypes=FILE_TYPES,     # optional
                                         defaultextension='.py',   # optional
                                         #initialdir=HOME,          # optional
                                         initialfile='hello.py',   # optional
                                         title='Select your file') # optional    
    ivn.set(str(pathstr))
def ok_func():
    acer.func(ivn.get())
    #root.destroy()
	#print(ivn.get())

def cancel_func():
	root.destroy()

open_button = tk.Button(root, text="Open", command=open_file)
okBtn = tk.Button(root, text="OK", command=ok_func)
cancelBtn = tk.Button(root,text = "Cancel",command = cancel_func)

path.pack(ipadx=320,pady=5,padx=20)
open_button.pack(pady=5,padx=20,side = "right")

okBtn.pack(ipadx=10,pady=5,padx=20,side = "left")
cancelBtn.pack(ipadx=10,pady=5,padx=10,side = "left")
root.geometry('400x100')
tk.mainloop()