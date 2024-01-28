from tkinter import *
import pymongo
from tkinter import ttk

def check():
    coll_name=com.get()
    if coll_name in s:
        coll=db.get_collection(coll_name)
        all=coll.find({},{"_id":0})
        for i in all:
            lbl_r=Label(root,text=i,font=("",18))
            lbl_r.pack()
root=Tk()
root.geometry("500x500")
client = pymongo.MongoClient("localhost", 27017)
db = client.get_database('poulstar')
print(db)
s=db.list_collection_names()
print(s)

lbl=Label(root,text="collections:",font=('',18),fg="blue")
com=ttk.Combobox(root,values=s,font=('',18))
btn=Button(root,text="show info",width=10,height=2,bg="blue",fg="white",command=check)
lbl.pack(pady=20)
com.pack()
btn.pack()
root.mainloop()
