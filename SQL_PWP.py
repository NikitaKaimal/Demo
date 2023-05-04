import mysql.connector
con=mysql.connector.connect(host='localhost',password='2127',user='root')

if con.is_connected():
    print("Connection created...")

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+MySql")

id = Label(root,text='Enter ID',font=('bold',10))
id.place(x=20,y=30)

name = Label(root,text='Enter Name',font=('bold',10))
name.place(x=20,y=60)
 
phone = Label(root,text='Enter Phone',font=('bold',10))
phone.place(x=20,y=90)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_phone=Entry()
e_phone.place(x=150,y=90)

insert = Button(root,text="insert",font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=140)

delete = Button(root,text="delete",font=("italic",10),bg="white",command=delete)
insert.place(x=70,y=140)

update = Button(root,text="update",font=("italic",10),bg="white",command=update)
insert.place(x=130,y=140)

get = Button(root,text="get",font=("italic",10),bg="white",command=get)
insert.place(x=190,y=140)
