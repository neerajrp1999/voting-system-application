import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import db
import VoteMainPage,userVoting
def voteP(m,li,user_id):
    m.destroy()
    root=Tk()
    root.title("Vote")
    root.geometry("500x500")
    load=Image.open("index.png")
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render)
    img.image=render
    img.pack(side=LEFT)
    
    cFrame=Frame(root)
    cFrame.pack(side=LEFT)
    Label(cFrame,text="Candidates",font = "Times 17 bold").pack()
    Label(cFrame,text="").pack()
    var = IntVar()
    id1=int(li[0][0])
    all1=db.getAllCandidateById(id1)
    for i in all1:
        Radiobutton(cFrame, text=i[1], variable=var, value=i[0],font = "Times 15 bold").pack( anchor = W )
    Label(cFrame,text="").pack()
    Button(cFrame,text="Vote",command=lambda : votePreMethod(root,var,user_id,id1),font = "Times 15 bold").pack()
    Button(cFrame,text="Cancel",fg="red",command=lambda :[userVoting.userVotePage(root,user_id)]).pack()
    root.mainloop()
def votePreMethod(root,var,user_id,id1):
    c_id=int(var.get())
    print(user_id,c_id)
    inputDialog = VoteClass(root,user_id,c_id,id1)
    root.wait_window(inputDialog.top)
class VoteClass:
    def __init__(self, parent,user_id,c_id,id1):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text="Are you sure?")
        self.myLabel.pack()
        self.Label1 = tk.Label(top, text='')
        self.Label1.pack()
        self.yes = tk.Button(top, text='Yes',command=lambda :[self.top.destroy(),votePostMethod(parent,user_id,c_id,id1)])
        self.yes.pack(expand = True, fill = BOTH)
        self.myLabel1 = tk.Label(top, text='')
        self.myLabel1.pack()
        self.no = tk.Button(top,text='No',command=lambda:self.top.destroy())
        self.no.pack(expand = True, fill = BOTH)
        self.FromLabel2 = tk.Label(top, text='')
        self.FromLabel2.pack()
def votePostMethod(parent,user_id,c_id,id1):
    db.makeVote(user_id,c_id,id1)
    messagebox.showinfo("Done","Vote Done")
    userVoting.userVotePage(parent,user_id)

if __name__ == "__main__":
    d=[(8904, 'test3'),(8909, 'test3'),(8900, 'test3'),(8902, 'test3')]
    m=Tk()
    voteP(m,d,"11sd2gy6t7")