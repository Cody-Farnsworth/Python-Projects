
import sqlite3

import os


#This creates the starting table that has a ID integer and one column named
#file name that starts off our table
def Start_app():
    conn = sqlite3.connect('project.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_project ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT \
            )")
        conn.commit()
    conn.close()
    get_files()
    display()
    
#This next section grabs all the files that end in .txt from the OS
#Then it imports them into the tables in SQL
def get_files():

    fileList = ('information.docx', 'Hello.txt', 'myImage.png',
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    conn = sqlite3.connect('project.db')
    with conn:
        cur = conn.cursor()

        for i in fileList:
            if i.endswith('.txt'):
                cur.execute("INSERT INTO tbl_project(file_name) VALUES(?)",(i,))
        conn.commit()
    conn.close()


#This final section grabs the info out of SQL and displays them.
def display():
    
    conn = sqlite3.connect('project.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT file_name FROM tbl_project")
        varPerson = cur.fetchall()
        for item in varPerson:
            msg = "{}".format(item)
            print(msg)
    



if __name__ == "__main__":
    Start_app()
