from tkinter import *
import pymongo
from tkinter import ttk

root=Tk()
root.geometry("500x500")

treev = ttk.Treeview(root, selectmode ='browse')

treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'
treev.column("1", width = 90, anchor ='center')
treev.column("2", width = 90, anchor ='center')
treev.column("3", width = 90, anchor ='center')

treev.heading("1", text ="Name")
treev.heading("2", text ="Last name")
treev.heading("3", text ="Age")

client=pymongo.MongoClient("localhost", 27017)
db=client.get_database("poulstar")
coll=db.get_collection("teacher")
all_data=coll.find({},{"_id":0})
for i in all_data:
    treev.insert("", 'end', text ="L1",values =(i['name'],i['lastname'], i['age']))

treev.pack()
root.mainloop()
