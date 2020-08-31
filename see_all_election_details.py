from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import db
import random
import adminPage

def see_election(m):
    m.destroy()
    root=Tk()
    root.geometry("905x400")
    root.title("See All Election Details")

    leftFrame=Frame(root)
    leftFrame.pack(side=LEFT)

    midFrame=Frame(root)
    midFrame.pack(side=LEFT)

    lableMidFrame=Frame(root)
    lableMidFrame.pack(side=LEFT)
    startdate=StringVar()
    enddate=StringVar()
    Label(lableMidFrame,text="Starting Date:", font = "Times 10 bold").pack(expand = True, fill = BOTH)
    Label(lableMidFrame,text="").pack(expand = True, fill = BOTH)
    Label(lableMidFrame,textvariable=startdate, font = "Times 10 bold",width=30).pack(expand = True, fill = BOTH)
    Label(lableMidFrame,text="").pack(expand = True, fill = BOTH)
    Label(lableMidFrame,text="Endting Date:", font = "Times 10 bold").pack(expand = True, fill = BOTH)
    Label(lableMidFrame,text="").pack(expand = True, fill = BOTH)
    Label(lableMidFrame,textvariable=enddate, font = "Times 10 bold",width=30).pack(expand = True, fill = BOTH)

    rightFrame=Frame(root)
    rightFrame.pack(side=LEFT)

    Label(leftFrame,text="All Election Details:", fg="blue", font = "Times 17 bold").pack()
    Label(leftFrame,text="").pack()
    load=Image.open("index.png")
    render=ImageTk.PhotoImage(load)
    img=Label(leftFrame,image=render)
    img.image=render
    img.pack()

    Label(midFrame,text="Elections", font = "Times 15 bold").pack(expand = True, fill = BOTH)
    Label(midFrame,text="", font = "Times 15 bold").pack()
    Eframe=Frame(midFrame)
    Eframe.pack(expand = True,fill = BOTH)
    scrollbarE=Scrollbar(Eframe)
    listBoxElection=Listbox(Eframe,width=30,selectmode=BROWSE)
    listBoxElection.config(yscrollcommand=scrollbarE.set)
    scrollbarE.config(command=listBoxElection.yview)
    listBoxElection.pack(expand = True, fill = BOTH,side=LEFT)
    scrollbarE.pack(fill = BOTH,side=RIGHT)
    Label(midFrame,text="").pack()
    Button(midFrame,text="Back",font = "Times 10 bold",command=lambda:adminPage.adminPageStart(root)).pack(expand = True, fill = BOTH)
    db.loadElectionData(listBoxElection)

    Label(rightFrame,text="Candidates", font = "Times 15 bold").pack(expand = True, fill = BOTH)
    Label(rightFrame,text="", font = "Times 15 bold").pack()
    Cframe=Frame(rightFrame)
    Cframe.pack(expand = True,fill = BOTH)
    scrollbarC=Scrollbar(Cframe)
    listBoxCandidate=Listbox(Cframe,width=30)
    listBoxCandidate.config(yscrollcommand=scrollbarC.set)
    scrollbarC.config(command=listBoxCandidate.yview)
    listBoxCandidate.pack(expand = True, fill = BOTH,side=LEFT)
    listBoxCandidate.configure(exportselection=False)
    scrollbarC.pack(fill = BOTH,side=RIGHT)
    Label(rightFrame,text="").pack()
    Button(rightFrame,text="Cancel",fg="red",font = "Times 10 bold",command=lambda:root.destroy()).pack(expand = True, fill = BOTH)
    
    def selectedElection(event):
        try:
            listBoxCandidate.delete(0, tk.END)
            cur=listBoxElection.curselection()
            all_items = listBoxElection.get(0, tk.END)
            sel_list= [all_items[item] for item in cur]
            Eid=int(sel_list[0][0:5])
            db.getCandidate(Eid,listBoxCandidate,startdate,enddate)
        except:
            pass
    listBoxElection.bind('<<ListboxSelect>>', selectedElection)
    
    root.mainloop()
if __name__ == "__main__":
    m=Tk()
    see_election(m)
