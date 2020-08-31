from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import db
import random
import VoteMainPage
otp_ran=random.randint(1000,9999)
countTime=0
def startR(m):
	m.destroy()
	root=Tk()
	root.geometry("550x500")
	root.title("Account Activation Page") 
	leftFrame=Frame(root)
	leftFrame.pack(side=LEFT)
	rightFrame=Frame(root)
	rightFrame.pack()
	load=Image.open("index.png")
	render=ImageTk.PhotoImage(load)
	img=Label(leftFrame,image=render)
	img.image=render
	img.pack()
	
	cardno=StringVar()
	otp=StringVar()
	password=StringVar()
	Repassword=StringVar()
	time=StringVar()
	time.set("Time Left:")
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Activate Account",width="20", fg="blue", font = "Times 20 bold").pack()
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Voting Cart no",width="20",  font = "Times 14 bold").pack()
	Entry(rightFrame,textvariable=cardno,font="Times 14 bold",width=10).pack(expand = True, fill = BOTH)
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Enter Password",width="20",font="Times 14 bold").pack()
	Entry(rightFrame,textvariable=password,font="Times 14 bold",show="*").pack(expand = True, fill = BOTH)
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Re-enter Password",width="20",font="Times 14 bold").pack()
	Entry(rightFrame,textvariable=Repassword,font="Times 14 bold",show="*").pack(expand = True, fill = BOTH)
	Label(rightFrame,text="").pack()
	otpB=Button(rightFrame,text="Send OTP",width="20",fg="black", activebackground = "white",font="Times 14 bold",command=lambda:sendOTPB(cardno,time,root,ActB,otpB))
	otpB.pack()
	Label(rightFrame,text="").pack()
	Label(rightFrame,textvariable=time,text="",width="20",font="Times 14 bold").pack()
	Label(rightFrame,text="").pack()
	Label(rightFrame,text="Enter OTP",width="20",font="Times 14 bold").pack()
	Entry(rightFrame,textvariable=otp,font="Times 14 bold").pack(expand = True, fill = BOTH)
	Label(rightFrame,text="").pack()
	ActB=Button(rightFrame,text="Activate Account",fg="black", activebackground = "white",width="20",font="Times 14 bold",command=lambda:ActivateB(root,cardno,otp,password,Repassword,time))
	ActB.pack()
	Label(rightFrame,text="").pack()
	Button(rightFrame,text="Back",width="20", fg="black", activebackground = "white",font="Times 14 bold",command=lambda:back_bu(root)).pack()

	root.mainloop()
def back_bu(root):
	countTime=0
	root.destroy()
	VoteMainPage.start()
def countdown(count,time,root,ActB,otpB):
	mins,secs =divmod(count,60)
	time.set("Time Left:"+str(mins)+":"+str(secs))
	if(count>0):
		countTime=count-1
		root.after(1000,countdown,count-1,time,root,ActB,otpB)
	else:
		otpB["state"]=NORMAL
		otpB['text']="Re-Send OTP"
		ActB["text"]="Times up!!"
		ActB["state"]=DISABLED
def sendOTPB(cardno,time,root,ActB,otpB):
	cardnoS=str(cardno.get())
	cardnoS=cardnoS.strip()
	if(db.CardNoIsRight(cardnoS)):
		receiver_email = db.GetEmailByCardNo(cardnoS)
		sendOTP(receiver_email.strip(),otp_ran,time,root,ActB,otpB)
	else:
		messagebox.showinfo("Error", "Voter Card No is wrong!")
		return
def sendOTP(receiver_email,otp_ran,time,root,ActB,otpB):
	try:
		sender_email = "example@gmail.com" #Enter your gmail id
		password = "example" #Enter your gmail id password and go turn on your "app less secure"
		message = MIMEMultipart("alternative")
		message["Subject"] = "Voter Card Activation Validation"
		message["From"] = sender_email
		message["To"] = receiver_email
		text = """\
		Hi there,
		Your Voter Card Activation Validation OTP is:"""+str(otp_ran)+"""\
		Don't share this otp with anyone else.
		"""
		html = """\
		<html>
		<body>
			<p>Hi there,<br>
			Your Voter Card Activation Validation OTP is:<br>"""+str(otp_ran)+"""\
			Don't share this otp with anyone else.
			</p>
		</body>
		</html>
		"""
		part1 = MIMEText(text, "plain")
		part2 = MIMEText(html, "html")
		message.attach(part1)
		message.attach(part2)
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(
				sender_email, receiver_email, message.as_string()
			)
		otpB["state"]=DISABLED
		countTime=180
		countdown(countTime,time,root,ActB,otpB)
	except:
		messagebox.showinfo("Error", "Sending OTP Failed!")
	return
def ActivateB(root,cardno,otp,password,Repassword,time):
	cardnoS=cardno.get().strip()
	otpS=otp.get().strip()
	passwordS=password.get().strip()
	RepasswordS=Repassword.get().strip()
	if(len(cardnoS)!=10):
		messagebox.showerror("Error", "Voter Card char is not 10!")
		return
	if(db.isVoterAccountAlreadyActivated(cardnoS)):
		messagebox.showerror("Error","This Voter card id Account Already Activated")
		return
	if(len(passwordS)!=6):
		messagebox.showerror("Error", "password lenght is not 6!")
		return
	if(len(RepasswordS)!=6):
		messagebox.showerror("Error", "Re-password lenght is not 6!")
		return
	if(passwordS!=RepasswordS):
		messagebox.showerror("Error", "password & Repassword is not same!")
		return
	if(len(otpS)!=4):
		messagebox.showerror("Error", "Otp lenght is not 4!")
		return
	otpSInt=int(otpS)
	if(otpSInt!=otp_ran):
		messagebox.showerror("Error","Wrong Otp!")
		return
	db.ActivateNewVoter(cardnoS,passwordS)
	messagebox.showinfo("Done","Account Activated!")
	back_bu(root)
	
