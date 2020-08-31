from tkinter import Label,Entry,Frame,Button,Tk,LEFT,BOTH,messagebox,StringVar,Scrollbar,RIGHT,Y,Listbox,END
import tkinter as tk
from PIL import Image,ImageTk
import db
import random,datetime
from datetime import time
import adminPage
PartiesName=[]
AllDate=[0,0]
def TakeName(m):
    m.destroy()
    root=Tk()
    root.geometry("250x200")
    root.title("Create New Election")
    ElectionId=StringVar()
    ElectionName=StringVar()
    Label(root,text="Enter Election ID ",width="20",  font = "Times 14 bold").pack()
    Entry(root,textvariable=ElectionId,font="Times 14 bold",width=10).pack(expand = True, fill = BOTH)
    Label(root,text="").pack()
    Label(root,text="Enter Election Name ",width="20",  font = "Times 14 bold").pack()
    Entry(root,textvariable=ElectionName,font="Times 14 bold",width=10).pack(expand = True, fill = BOTH)
    Label(root,text="").pack()
    Button(root,text="Create Election",width="20", fg="black", activebackground = "white",font="Times 14 bold",command=lambda :Create_New(root,ElectionId,ElectionName)).pack()
    Label(root,text="").pack()
    Button(root,text="Cancel",width="20", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:back_bu(root)).pack()
    Label(root,text="").pack()
    
    root.mainloop()
def Create_New(m,ElectionId,ElectionName):
    if(len(ElectionName.get())==0):
        messagebox.showerror("Error","Election Name must Not empty!")
        return
    if(len(ElectionId.get())!=4):
        messagebox.showerror("Error","Election Id must be 4 in size!")
        return
    try:
        int(ElectionId.get())
    except:
        messagebox.showerror("Error","Election Id must be Numeric !")
        return
    if(db.Check_Election_id_Exist(int(ElectionId.get()))):
        messagebox.showerror("Error","This Election id Already exist, use another one!")
        return
    Create_New_EPage(m,ElectionId,ElectionName)
def Create_New_EPage(m,ElectionId,ElectionName):
    m.destroy()
    root=Tk()
    root.geometry("856x500")
    root.title(ElectionName.get()+" "+ElectionId.get())
    leftFrame=Frame(root)
    leftFrame.pack(side=LEFT)
    mFrame=Frame(root)
    mFrame.pack(side=LEFT)
    rightFrame=Frame(root)
    rightFrame.pack(side=LEFT)
    load=Image.open("index.png")
    render=ImageTk.PhotoImage(load)
    img=Label(leftFrame,image=render)
    img.pack()
    ElectionPartiesId=StringVar()
    ElectionPartiesName=StringVar()
    Label(mFrame,text="Enter Parties Details",width="21", fg="blue", font = "Times 20 bold").pack()
    Label(mFrame,text="").pack()
    Label(mFrame,text="Enter Parties ID ",width="20",  font = "Times 14 bold").pack()
    Entry(mFrame,textvariable=ElectionPartiesId,font="Times 14 bold",width=10).pack(expand = True, fill = BOTH)
    Label(mFrame,text="").pack()
    Label(mFrame,text="Enter Parties Name ",width="20",  font = "Times 14 bold").pack()
    Entry(mFrame,textvariable=ElectionPartiesName,font="Times 14 bold",width=10).pack(expand = True, fill = BOTH)
    Label(mFrame,text="").pack()
    Button(mFrame,text="Add Parties",width="20", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:addParties(ElectionPartiesId,ElectionPartiesName,listbox)).pack(expand = True, fill = BOTH)
    Label(mFrame,text="").pack()
    
    Button(mFrame,text="Take Starting/Ending Date",width="25", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:TakeStartEndDateM(root)).pack(expand = True, fill = BOTH)
    Label(mFrame,text="").pack()
    Button(mFrame,text="Cancel",width="20", fg="Red", activebackground = "white",font="Times 14 bold",command=lambda:popupCancel(root)).pack(expand = True, fill = BOTH)
    Label(mFrame,text="").pack()
    Label(rightFrame,text="",width="21", font = "Times 20 bold").pack()
    Label(rightFrame,text="").pack()
    Label(rightFrame,text="List of Parties: ",width="20",  font = "Times 14 bold").pack()
    Label(rightFrame,text="").pack()

    listFrame=Frame(rightFrame)
    scrollbar = Scrollbar(listFrame)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(listFrame)  
    listbox.pack(expand = True, fill = BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listFrame.pack(expand = True, fill = BOTH)

    Label(rightFrame,text="").pack()
    Button(rightFrame,text="Delete Selected Parties",width="25", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:deleteSP(listbox)).pack(expand = True, fill = BOTH)
    Label(rightFrame,text="").pack()
    Button(rightFrame,text="Create Election",width="20", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:CreateFinalMethod(root,ElectionId,ElectionName)).pack(expand = True, fill = BOTH)
    Label(rightFrame,text="").pack()
    root.mainloop()
def popupCancel(root):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text="Do you really want to cancel?", font="Times 14 bold")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Yes", command = lambda:[popup.destroy(),back_bu(root)])
    B1.pack(expand = True, fill = BOTH)
    B2 = Button(popup, text="No", command = popup.destroy)
    B2.pack(expand = True, fill = BOTH)
    popup.mainloop()
def deleteSP(listbox):
    s=listbox.curselection()
    if s is ():
        messagebox.showerror("Error","First Select Any Parties!")
        return
    listbox.delete(s)
    del PartiesName[s[0]]
    pass
def addParties(ElectionPartiesId,ElectionPartiesName,listbox):
    ElectionPartiesIdS=ElectionPartiesId.get()
    ElectionPartiesNameS=ElectionPartiesName.get()
    if(len(ElectionPartiesNameS)==0):
        messagebox.showerror("Error","Election Parties Name must Not empty!")
        return
    if(len(ElectionPartiesIdS)!=4):
        messagebox.showerror("Error","Election Id must be 4 in size!")
        return
    try:
        int(ElectionPartiesIdS)
    except:
        messagebox.showerror("Error","Election Parties Id must be Numeric !")
        return
    for i in PartiesName:
        if i[0]==int(ElectionPartiesIdS):
            messagebox.showerror("Error","This ID Already Exist")
            return
    listbox.insert(END,ElectionPartiesIdS+"  |  "+ElectionPartiesNameS)
    PartiesName.append([int(ElectionPartiesIdS),ElectionPartiesNameS])
    pass
def TakeStartEndDateM(root):
    inputDialog = TakeStartEndDate(root)
    root.wait_window(inputDialog.top)
    try:
        AllDate[0]= inputDialog.dateStart
        AllDate[1]= inputDialog.dateEnd
        print(AllDate)
    except:
        messagebox.showerror("Error","Add Both dates otherwise you can't create a new Election process!")
class TakeStartEndDate:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Enter Date in DD:MM:YYYY:hh:mm:ss format')
        self.myLabel.pack()
        self.Label1 = tk.Label(top, text='')
        self.Label1.pack()
        self.From = tk.Label(top, text='From')
        self.From.pack()
        self.myLabel1 = tk.Label(top, text='')
        self.myLabel1.pack()
        self.FromEntryBox = tk.Entry(top)
        self.FromEntryBox.pack(expand = True, fill = BOTH)
        self.FromLabel2 = tk.Label(top, text='')
        self.FromLabel2.pack()
        self.To = tk.Label(top, text='To')
        self.To.pack()
        self.myLabel3= tk.Label(top, text='')
        self.myLabel3.pack()
        self.ToEntryBox = tk.Entry(top)
        self.ToEntryBox.pack(expand = True, fill = BOTH)
        self.myLabel4= tk.Label(top, text='')
        self.myLabel4.pack()
        self.SubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.SubmitButton.pack()

    def send(self):
        self.dateS = self.FromEntryBox.get()
        self.dateE = self.ToEntryBox.get()
        self.dateSs=self.dateS.split(":")
        self.dateEs=self.dateE.split(":")
        try:
            self.x = datetime.datetime(int(self.dateSs[2]),int(self.dateSs[1]),int(self.dateSs[0]),int(self.dateSs[3]),int(self.dateSs[4]),int(self.dateSs[5]))
            self.y = datetime.datetime(int(self.dateEs[2]),int(self.dateEs[1]),int(self.dateEs[0]),int(self.dateEs[3]),int(self.dateEs[4]),int(self.dateEs[5]))
        except:
            messagebox.showerror("Invalid","Invalid date and time")
            return
        now = datetime.datetime.now()
        if(now>=self.x or now>=self.y):
            messagebox.showerror("Date Error","Election will be start in future not now!")
            return
        if(self.x>=self.y):
            messagebox.showerror("Date Error","Election End date must greater than starting date!")
            return
        self.x_10=self.x+datetime.timedelta(minutes = 10)
        if(self.y<=self.x_10):
            messagebox.showerror("Date Error","Election will not End in 10 minutes, make longer")
            return
        self.dateStart=self.x
        self.dateEnd=self.y
        self.top.destroy()
def back_bu(root):
    PartiesName.clear()
    adminPage.adminPageStart(root)
def CreateFinalMethod(root,ElectionId,ElectionName):
    if(len(PartiesName)<=1):
        messagebox.showerror("Error","Atleast Need two candidet for election!")
        return
    if(AllDate[0]==0 or AllDate[1]==0):
        messagebox.showerror("Error","Enter the date first!")
        return
    EID,EN=int(ElectionId.get()),ElectionName.get()
    db.CreateNewElection(AllDate,PartiesName,EID,EN)
    messagebox.showinfo("Done","New Election has been created!")
    PartiesName.clear()
    back_bu(root)
if __name__ == "__main__":
    m=Tk()
    TakeName(m)