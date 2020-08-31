from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from datetime import datetime
import db,vote,VoteMainPage
def userVotePage(m,user_id):
    m.destroy()
    root=Tk()
    root.geometry("755x380")
    root.title("Voting")
    Label(root,text="Election list:", fg="blue", font = "Times 17 bold").pack()
    Label(root,text="").pack()
    load=Image.open("index.png")
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render)
    img.image=render
    img.pack(side=LEFT)
    Button(root,text="Cancel",fg="red",width=40,command=lambda :[root.destroy(),VoteMainPage.start()]).pack(side=BOTTOM)

    listFrame=Frame(root)
    listFrame.pack(side=LEFT)
    Label(listFrame,text="Active Election:", font = "Times 15 bold").pack()
    Label(listFrame,text="").pack()
    li=Listbox(listFrame,width=30)
    li.pack(side = LEFT )
    scrollbar = Scrollbar(listFrame)
    scrollbar.pack( side = RIGHT,expand=True ,fill=BOTH)
    scrollbar.config( command = li.yview )
    li.config(yscrollcommand=scrollbar.set)


    listFrame2=Frame(root)
    listFrame2.pack(side=LEFT)
    Label(listFrame2,text="All Election:", font = "Times 15 bold").pack()
    Label(listFrame2,text="").pack()
    li2=Listbox(listFrame2,width=40)
    li2.pack(side = LEFT, expand=True )
    scrollbar = Scrollbar(listFrame2)
    scrollbar.pack( side = RIGHT,expand=True,fill=BOTH )
    scrollbar.config( command = li2.yview )
    li2.config(yscrollcommand=scrollbar.set,exportselection=False)
    l=db.UserloadElectionData(li)
    db.UserAllElectionTable(li2)
    li.bind('<Double-Button-1>', lambda x:selectedElection(root,li,l,user_id))
    root.mainloop()
def selectedElection(root,li,l,user_id):
        cur=li.curselection()
        print(l[cur[0]][0])
        if(db.isUserAlreadyVoted(int(l[cur[0]][0]),user_id)):
            messagebox.showerror("Error","User Already Voted!")
            return
        inputDialog = seeE(root,l,cur,li,user_id)
        root.wait_window(inputDialog.top)
        
class seeE:
    def __init__(self, parent,l,cur,li,user_id):
        top = self.top = tk.Toplevel(parent)
        self.l=l
        self.cur=cur
        self.myLabel = tk.Label(top, text="Do you want to start '"+str(self.l[self.cur[0]][1])+"' Election?")
        self.myLabel.pack()
        self.Label1 = tk.Label(top, text='')
        self.Label1.pack()
        self.yes = tk.Button(top, text='Yes',command=lambda :[self.top.destroy(),vote.voteP(parent,l,user_id)])
        self.yes.pack(expand = True, fill = BOTH)
        self.myLabel1 = tk.Label(top, text='')
        self.myLabel1.pack()
        self.no = tk.Button(top,text='No',command=lambda:self.top.destroy())
        self.no.pack(expand = True, fill = BOTH)
        self.FromLabel2 = tk.Label(top, text='')
        self.FromLabel2.pack()

if __name__ == "__main__":
    m=Tk()
    userVotePage(m,"11sd2gy6t7")
