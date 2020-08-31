from tkinter import Label,Entry,Frame,Button,Tk,LEFT,BOTH,messagebox
from PIL import Image,ImageTk
import tkinter as tk
import db,random
import VoteMainPage,Create_New_Election,see_all_election_details,AfterElectionDetail
def con(l):
	l.config(text="sending  in progress...")
	l.update()
def adminPageStart(m):
	m.destroy()
	root=Tk()
	root.geometry("650x400")
	root.title("Admin Main Page") 
	leftFrame=Frame(root)
	leftFrame.pack(side=LEFT)
	rightFrame=Frame(root)
	rightFrame.pack()
	load=Image.open("index.png")
	render=ImageTk.PhotoImage(load)
	img=Label(leftFrame,image=render)
	img.image=render
	img.pack()
	
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Admin Main Page",width="25", fg="blue", font = "Times 20 bold").pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="Create New Election",width="25",fg="black", activebackground = "white",font="Times 14 bold",command=lambda:Create_New_Election.TakeName(root)).pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="Delete Election",fg="black", activebackground = "white",width="25",font="Times 14 bold",command=lambda:deleteElection(root)).pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="See All Election Details",fg="black", activebackground = "white",width="25",font="Times 14 bold",command=lambda:see_all_election_details.see_election(root)).pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="See After Election Details",fg="black", activebackground = "white",width="25",font="Times 14 bold",command=lambda : AfterElectionDetail.see_After(root)).pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="Back",width="25", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:back_bu(root)).pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="Cancel",width="25", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:root.destroy()).pack()
	root.mainloop()
def back_bu(root):
	root.destroy()
	VoteMainPage.start()

def deleteElection(root):
    inputDialog = deleteElectionClass(root)
    root.wait_window(inputDialog.top)

class deleteElectionClass:
	def __init__(self,parent):
		top=self.top=tk.Toplevel(parent)
		self.label=tk.Label(top,text="Enter Election id to delete:")
		self.label.pack()
		self.label1=tk.Label(top,text="")
		self.label1.pack()
		self.id=tk.Entry(top)
		self.id.pack(expand=True,fill=BOTH)
		self.label1=tk.Label(top,text="")
		self.label1.pack()
		self.deleteB=tk.Button(top,text="Delete",command=lambda:self.send())
		self.deleteB.pack()
		self.label1=tk.Label(top,text="")
		self.label1.pack()
		self.cancelB=tk.Button(top,text="Cancel",command=lambda:self.top.destroy())
		self.cancelB.pack()
	def send(self):
		self.idS=self.id.get()
		if(len(self.idS)!=4):
			messagebox.showerror("Error","Election id lenght must be 4!")
			return
		try:
			self.idi =int(self.idS)
		except:
			messagebox.showerror("Error","Election id must be numberic!")
			return
		if not(db.Check_Election_id_Exist(self.idi)):
			messagebox.showerror("Error","Election id does not exist!")
			return
		if not(db.deleteElectiondb(self.idi)):
			messagebox.showerror("Error","DB Error!")
			return
		messagebox.showinfo("Done","Election deletion completed.")
		self.top.destroy()

if __name__ == "__main__":
    m=Tk()
    adminPageStart(m)