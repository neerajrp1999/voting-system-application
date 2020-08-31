from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import userVoting,db,adminPage,VCardActivation,userForgetPwd

def start():
    top = Tk()  
    top.geometry("400x450") 
    top.title("Main Page") 
    frame = Frame(top)  
    frame.pack()  
      
    Bottomframe = Frame(top)  
    Bottomframe.pack()  
     
    
    load = Image.open("index.png")
    render = ImageTk.PhotoImage(load)
    img = Label(frame, image=render)
    img.image = render
    img.pack( expand = True, fill = BOTH)
 
      
    Label(Bottomframe, text="Voting Cart No",width="20",  font = "Times 15 bold").pack()
    votingCardNo = StringVar()
    Entry(Bottomframe, textvariable=votingCardNo,font = "Verdana 10 bold").pack(expand = True, fill = BOTH)
    Label(Bottomframe,text="").pack()
    Label(Bottomframe,text="Password",width="10", font = "Times 15 bold").pack()  
    password = StringVar()
    Entry(Bottomframe, textvariable=password, show='*',font = "Verdana 10 bold").pack(expand = True, fill = BOTH)  
    Label(Bottomframe,text="").pack()
    btn4 = Button(Bottomframe, text="Login", fg="black", activebackground = "white",font = "Times 15 bold",command=lambda:login_bu(votingCardNo,password,top))  
    btn4.pack(expand = True, fill = BOTH)  
    forgetPwd=Label(Bottomframe,text="Forget Password",fg="blue", activebackground = "white",font = "Times 15 bold")  
    forgetPwd.pack(expand = True, fill = BOTH) 
    forgetPwd.bind("<Button-1>",lambda x:forget_pwd(top))
    Label(Bottomframe,text="").pack()
    btn5 = Button(Bottomframe, text="Active Account", fg="black", activebackground = "white",font = "Times 15 bold",command=lambda:register_bu(top))  
    btn5.pack(expand = True, fill = BOTH) 
    #messagebox.showinfo("Alert Message", "This is just a alert message!")
    top.mainloop()

def login_bu(votingCardNo,password,root):
    votingCardNoS,passwordS=votingCardNo.get().strip(),password.get().strip()
    if (len(votingCardNoS)!=10):
        messagebox.showinfo("Error", "Voter Card char is 10!")
        return
    if(len(passwordS)!=6):
        messagebox.showinfo("Error", "password lenght is 6!")
        return
    if(db.isAdmin(votingCardNoS)):
        if(passwordS!=db.giveAdminPassword(votingCardNoS)):
            messagebox.showerror("Error","Invalid Password!")
            return
        adminPage.adminPageStart(root)

    else:
        if not(db.isVoterAccountAlreadyActivated(votingCardNoS)):
            messagebox.showerror("Error","This Voting Card No is Not Activated, Activate First!")
            return
        if (passwordS!=db.userPassword(votingCardNoS)):
            messagebox.showerror("Error","User Password Is Invalid!")
            return
        userVoting.userVotePage(root,votingCardNoS)
def register_bu(root):
    VCardActivation.startR(root)
def forget_pwd(top):
    userForgetPwd.startReset(top)
   
if __name__ == "__main__":
    start()
