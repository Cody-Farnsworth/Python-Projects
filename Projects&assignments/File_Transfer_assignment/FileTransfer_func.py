# Python Ver:   3.9.0
#
# Author:       Cody J. Farnsworth
#
# Purpose:      File Transfer Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10



import os,time
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import shutil
import datetime as dt

import FileTransfer_main
import FileTransfer_gui



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

def File_transfer(self):
    source = self.src_entry.get()
    destination = self.des_entry.get()
    files = os.listdir(source)
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    for i in files:
        mtime= os.path.getmtime(source+'/'+i)
        modtime = dt.datetime.fromtimestamp(mtime)
        if modtime > ago:
            shutil.move(source+'/'+i, destination)
    
def Choose_source(self):
    src = filedialog.askdirectory()
    self.src_entry.insert(0, src)

def Choose_des(self):
    des = filedialog.askdirectory()
    self.des_entry.insert(0, des)








if __name__ == "__main__":
    pass

