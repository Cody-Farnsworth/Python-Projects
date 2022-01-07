# Python Ver:   3.9.0
#
# Author:       Cody J. Farnsworth
#
# Purpose:      Student Tracker Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10



import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser

import WebPage_Main
import WebPage_gui



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        

def creat_file(self):
    var_text = self.txt_page.get()
    f = open("BasicHtml.html", "w")
    f.write("<html><body><h1> {} </h1></body></html>".format(var_text,))
    f.close()

def open_page(self):

    url=("BasicHtml.html")
    webbrowser.open_new(url)
    









if __name__ == "__main__":
    pass
