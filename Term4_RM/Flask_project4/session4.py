from tkinter import *
from tkinter import messagebox as msb,ttk
from threading import Thread
from data import *
import smtplib,ssl
import webbrowser

SENDER="soheila.pouldrive1@gmail.com"
PASSWORD="jlqa hkzo dzrk mkdc"
SMTP_SERVER="smtp.gmail.com"
PORT=465

BG="#333333"
FG="orange"
BG2="#444444"
FG2="yellow"

root=Tk()
root.geometry("1200x550+50+50")
root.config(bg=BG)

#________ALL FRAMES____________
frame_top=Frame(root,bg=BG)
frame_middle=Frame(root,bg=BG)
frame_middle2=Frame(root,bg=BG)
frame_bottom=Frame(root,bg=BG)

frame_top.pack(pady=10)
frame_middle.pack(pady=10)
frame_middle2.pack(pady=10)
frame_bottom.pack(pady=10)
#__________END FRAMES________

l_welcome=Label(frame_top,text="welcome to New York Times".upper(),bg=BG,fg=FG,font=('times',22))
l_welcome.pack()

l_search=Label(frame_middle,text="what are you looking for?",bg=BG,fg=FG,font=('times',22))
l_search.grid(row=1,column=1,columnspan=2)

btn_update=Button(frame_middle,text="click here to get the latest update",bg=BG,fg=FG,font=("times",22),command=update)
btn_update.grid(row=2,column=1,columnspan=2,pady=10)

e_search=Entry(frame_middle,bg=BG,fg=FG,insertbackground=FG,font=("times",22),bd=4)
e_search.grid(row=3,column=1)
e_search.bind("<Return>",search)

btn_search=Button(frame_middle,text="search",bg=FG,fg=BG,font=("times",22),command=search)
btn_search.grid(row=3,column=2)

l_bdl_click=Label(frame_middle,text="Double click on a row to open the link in browser",bg=BG,fg=FG,font=("times",14))
l_bdl_click.grid(row=4,column=1,pady=5)


root.mainloop()