from tkinter import Label,Entry,Frame,Button,Tk,LEFT,BOTH,messagebox,Listbox,Scrollbar,RIGHT,BOTTOM,StringVar,BROWSE,Radiobutton,IntVar,W
from PIL import Image,ImageTk
import tkinter as tk
import db
import random
import adminPage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

def see_After(m):
    m.destroy()
    root=Tk()
    root.geometry("555x400")
    root.title("See All Election Details")

    leftFrame=Frame(root)
    leftFrame.pack(side=LEFT)

    midFrame=Frame(root)
    midFrame.pack(side=LEFT)

    rightFrame=Frame(root)
    rightFrame.pack(side=LEFT)

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
    db.loadAfterElectionData(listBoxElection)
    all_items = listBoxElection.get(0, tk.END)
    print(all_items)
    listBoxElection.bind('<Double-Button-1>', lambda x:selectedElection(root,listBoxElection,all_items))

    root.mainloop()
def selectedElection(root,listBoxElection,all_items):
    try:
        cur=listBoxElection.curselection()
        sel_list= [all_items[item] for item in cur]
        Eid=int(sel_list[0][0:5])
        print(Eid)
        ShowResult(root,Eid)
    except:
        pass
def ShowResult(m,eid):
    m.destroy()
    root=Tk()
    root.title("Result")
    root.geometry("500x400")

    lframe=Frame(root)
    lframe.pack(side=LEFT)
    load=Image.open("index.png")
    render=ImageTk.PhotoImage(load)
    img=Label(lframe,image=render)
    img.image=render
    img.pack(side=LEFT)
    
    cFrame=Frame(root)
    cFrame.pack(side=LEFT)
    Label(cFrame,text="Panno:",font = "Times 17 bold").pack()
    Label(cFrame,text="").pack()

    listFrame=Frame(cFrame)
    listFrame.pack()
    scrollbarE=Scrollbar(listFrame)
    listBoxPanno=Listbox(listFrame,width=30,selectmode=BROWSE)
    listBoxPanno.config(yscrollcommand=scrollbarE.set)
    scrollbarE.config(command=listBoxPanno.yview)
    listBoxPanno.pack(expand = True, fill = BOTH,side=LEFT)
    scrollbarE.pack(fill = BOTH,side=RIGHT)
    db.getAllPanno(listBoxPanno)
    listBoxPanno.bind('<Double-Button-1>', lambda x:Panno_c(root,eid,listBoxPanno))
    Label(cFrame,text="").pack()
    Button(cFrame,text="Back",font = "Times 10 bold",command=lambda :see_After(root) ).pack(expand = True, fill = BOTH)
    root.mainloop()
def Panno_c(root,eid,listBoxPanno):
    cur=listBoxPanno.curselection()
    all_items = listBoxPanno.get(0, tk.END)
    sel_list= [all_items[item] for item in cur]
    pan_no=int(sel_list[0][0:4])
    print(pan_no)
    root.geometry("950x500")
    rFrame=Frame(root)
    rFrame.pack(side=LEFT)
    print(eid)

    canvas1 = tk.Canvas(rFrame, width = 400, height = 400)

    figure = Figure(figsize=(4,3), dpi=100) 
    subplot = figure.add_subplot(111) 
    PartiesName,candidateID,NoOfVotes,explode1=db.plot(eid,pan_no)
     
    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)
    wedges, texts, autotexts = subplot.pie(NoOfVotes, autopct=lambda pct: func(pct, NoOfVotes),
                                  textprops=dict(color="w"))

    subplot.legend(wedges, PartiesName,
            title="Ingredients",
            loc="upper left",
            bbox_to_anchor=(-0.1, 1, 0, 0.21))
    subplot.axis('equal')
    pie2 = FigureCanvasTkAgg(figure, rFrame)
    pie2.get_tk_widget().pack()
    canvas1.create_window(100, 100, window=figure)
    canvas1.pack(side=LEFT)
if __name__ == "__main__":
    m=Tk()
    see_After(m)

