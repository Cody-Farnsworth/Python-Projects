# Python Ver:   3.9.0
#
# Author:       Cody J. Farnsworth
#
# Purpose:      Student Tracking Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

import WebPage_Main
import WebPage_func


def load_gui(self):

    self.lbl_click = tk.Label(self.master,text='Press the Button to make a web Page with your text!')
    self.lbl_click.grid(row=1,column=3,padx=(275,0),pady=(10,10),sticky=NW)
    self.lbl_click = tk.Label(self.master,text='Press the Button to Open the Page')
    self.lbl_click.grid(row=5,column=3,padx=(325,0),pady=(10,0),sticky=NW)

    self.txt_page = tk.Entry(self.master,text='')
    self.txt_page.grid(row=2,column=3,rowspan=1,columnspan=3,padx=(350,0),pady=(10,0),sticky=NW)

    self.btn_make = tk.Button(self.master,width=12,height=2,text='Make',command=lambda: WebPage_func.creat_file(self))
    self.btn_make.grid(row=4,column=3,padx=(365,0),pady=(45,10),sticky=NW)
    self.btn_make = tk.Button(self.master,width=12,height=2,text='Open',command=lambda: WebPage_func.open_page(self))
    self.btn_make.grid(row=6,column=3,padx=(365,0),pady=(45,10),sticky=NW)
                                                                




if __name__ == "__main__":
    pass
