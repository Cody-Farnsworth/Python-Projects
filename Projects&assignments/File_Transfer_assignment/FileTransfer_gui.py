# Python Ver:   3.9.0
#
# Author:       Cody J. Farnsworth
#
# Purpose:      File Transfer Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

# importing our other modules 
# so we can have access to them
import FileTransfer_main
import FileTransfer_func



def load_gui(self):
  
    self.lbl_source = tk.Label(self.master,text='Source Path:')
    self.lbl_source.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_des = tk.Label(self.master,text='Destination Path:')
    self.lbl_des.grid(row=0,column=2,padx=(27,0),pady=(10,0),sticky=N+W)

    self.src_entry = tk.Entry (self.master)    
    self.src_entry.grid(row=1,column=0,columnspan=2,padx=(10,0),pady=(0,0),sticky=N+E+S+W)
    self.des_entry = tk.Entry (self.master)    
    self.des_entry.grid(row=1,column=2,columnspan=2,padx=(10,0),pady=(0,0),sticky=N+E+S+W)


    self.btn_source = tk.Button(self.master,width=12,height=2,text='Choose Source',command=lambda: FileTransfer_func.Choose_source(self))
    self.btn_source.grid(row=8,column=0,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_des = tk.Button(self.master,width=15,height=2,text='Choose Destination',command=lambda: FileTransfer_func.Choose_des(self))
    self.btn_des.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: FileTransfer_func.File_transfer(self))
    self.btn_update.grid(row=8,column=2,padx=(20,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: FileTransfer_func.ask_quit(self))
    self.btn_close.grid(row=8,column=3,columnspan=1,padx=(10,0),pady=(45,10),sticky=E)

    



    



if __name__ == "__main__":
    pass
