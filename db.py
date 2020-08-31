import MySQLdb
from tkinter import *

db_connection= MySQLdb.connect (host="127.0.0.1",user="root",passwd="pwd@123",db="VotingDB") 

 
def CardNoIsRight(cardno):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT ID FROM Voters WHERE ID = '%s' ; "%(cardno))
    m = cursor.fetchall()
    if(len(m)>=1):
        return True
    else:
        return False
def GetEmailByCardNo(cardno):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT emailid from Voters where ID='%s';"% (cardno)) 
    m = cursor.fetchone()
    return m[0]+""
def ActivateNewVoter(cardnoS,passwordS):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT * FROM Voters WHERE ID = '%s' ; "%(cardnoS))
    m = cursor.fetchone()
    cursor.execute("insert into ActivatedVoters(ID,VoterName,state,city,village,panno,emailid,tahsil,password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(cardnoS,m[1]+"",m[2]+"",m[3]+"",m[4]+"",str(m[5])+"",m[6]+"",m[7]+"",passwordS))
    db_connection.commit()
def isVoterAccountAlreadyActivated(cardnoS):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT ID FROM ActivatedVoters WHERE ID = '%s' ; "%(cardnoS))
    m = cursor.fetchall()
    if(len(m)>=1):
        return True
    else:
        return False
def ResetPwdActiveVoter(cardnoS,passwordS):
    cursor=db_connection.cursor() 
    cursor.execute("update ActivatedVoters set password = '%s' where ID = '%s' ;"%(passwordS,cardnoS))
    db_connection.commit()
def giveAdminPassword(votingCardNoS):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT adminpassword FROM adminLogin WHERE adminname = '%s' ; "%(votingCardNoS))
    m = cursor.fetchone()
    return m[0]+""
def userPassword(votingCardNoS):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT password FROM ActivatedVoters WHERE ID = '%s' ; "%(votingCardNoS))
    m = cursor.fetchone()
    return m[0]+""
def isAdmin(votingCardNoS):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT adminpassword FROM adminLogin WHERE adminname = '%s' ; "%(votingCardNoS))
    m = cursor.fetchall()
    if(len(m)>=1):
        return True
    else:
        return False
def CreateNewElection(AllDate,PartiesName,EID,EN):
    cursor=db_connection.cursor() 
    cursor.execute("insert into election values('%s','%s','%s','%s') ; "%(EID,EN,AllDate[0].strftime('%Y-%m-%d %H:%M:%S'),AllDate[1].strftime('%Y-%m-%d %H:%M:%S')))
    db_connection.commit()
    for candidate in PartiesName:
        cursor.execute("insert into candidate values('%s','%s','%s');"%(int(candidate[0]),candidate[1],EID))
        db_connection.commit()
    cursor.execute("alter table ActivatedVoters add column %s smallint(1) NOT NULL DEFAULT '%s';"%("isVoted"+str(EID),0))
    db_connection.commit()
    cursor.execute("alter table ActivatedVoters add column %s smallint(4) NOT NULL DEFAULT '%s';"%("VoteWhome"+str(EID),0000))
    db_connection.commit()
def Check_Election_id_Exist(ElectionId):
    cursor=db_connection.cursor() 
    cursor.execute("SELECT election_id FROM election WHERE election_id = '%s' ; "%(ElectionId))
    m = cursor.fetchall()
    if(len(m)>=1):
        return True
    else:
        return False

def deleteElectiondb(idi):
    try:
        cursor=db_connection.cursor()
        cursor.execute("DELETE FROM candidate WHERE election_id='%s';"%(idi))
        db_connection.commit()
        cursor.execute("DELETE FROM election WHERE election_id='%s';"%(idi))
        db_connection.commit()
        cursor.execute("alter table ActivatedVoters drop column %s ;"%("isVoted"+str(idi)))
        db_connection.commit()
        cursor.execute("alter table ActivatedVoters drop column %s ;"%("VoteWhome"+str(idi)))
        db_connection.commit()
        return True
    except:
        return False
    
def loadElectionData(listBoxElection):
    cursor=db_connection.cursor()
    cursor.execute("select * from election;")
    data=cursor.fetchall()
    for i in data:
        listBoxElection.insert(END,str(i[0])+" | "+str(i[1]))
def getCandidate(Eid,listBoxCandidate,startdate,enddate):
    cursor=db_connection.cursor()
    cursor.execute("select * from candidate where election_id='%s';"%(Eid))
    data=cursor.fetchall()
    for i in data:
        listBoxCandidate.insert(END,str(i[0])+" | "+str(i[1]))
    cursor.execute("select start_date,end_date from election where election_id='%s';"%(Eid))
    data=cursor.fetchone()
    startdate.set(str(data[0]))
    enddate.set(str(data[1]))
def UserloadElectionData(li):
    l=[]
    cursor=db_connection.cursor()
    cursor.execute("select * from election where start_date<(select now()) and end_date>(select now());")
    data=cursor.fetchall()
    for i in data:
        l.append(i)
        li.insert(END,"  "+str(i[1]))
    return l
def UserAllElectionTable(li):
    cursor=db_connection.cursor()
    cursor.execute("select * from election;")
    data=cursor.fetchall()
    for i in data:
        li.insert(END," "+str(i[1])+" | start date: "+str(i[2]))

def getAllCandidateById(id):
    li=[]
    cursor=db_connection.cursor()
    cursor.execute("select * from candidate where election_id='%s';"%(id))
    data=cursor.fetchall()
    for i in data:
        li.append(i)
    return li

def isUserAlreadyVoted(eid,user_id):
    cursor=db_connection.cursor() 
    cursor.execute("select %s from ActivatedVoters where ID = '%s';"%("isVoted"+str(eid),user_id))
    data=cursor.fetchone()
    print(data)
    if(data[0]==1):
        return True
    return False
def loadAfterElectionData(listBoxElection):
    cursor=db_connection.cursor()
    cursor.execute("select * from election where end_date < (select now());")
    data=cursor.fetchall()
    for i in data:
        listBoxElection.insert(END,str(i[0])+" | "+str(i[1]))
def makeVote(user_id,c_id,e_id):
    cursor=db_connection.cursor() 
    cursor.execute("update ActivatedVoters set %s ='%s' where ID = '%s';"%("isVoted"+str(e_id),1,user_id))
    db_connection.commit()
    cursor.execute("update ActivatedVoters set %s ='%s' where ID = '%s';"%("VoteWhome"+str(e_id),c_id,user_id))
    db_connection.commit()
def getAllPanno(listBoxPanno):
    cursor=db_connection.cursor()
    cursor.execute("SELECT DISTINCT  panno from ActivatedVoters;")
    data=cursor.fetchall()
    for i in data:
        listBoxPanno.insert(END,str(i[0]))
def plot(eid,pan_no):
    candidateName=[]
    candidateID=[]
    noVote=[]
    explode=[]
    cursor=db_connection.cursor()
    cursor.execute("SELECT candidate_name,candidate_id from candidate where election_id='%s';"%(eid))
    data=cursor.fetchall()
    for i in data:
        candidateName.append(i[0])
        candidateID.append(int(i[1]))
    for j in candidateID:
        cursor.execute("select count(*) from ActivatedVoters where %s ='%s' and panno='%s';"%("VoteWhome"+str(eid),int(j),int(pan_no)))
        d=cursor.fetchone()
        noVote.append(d[0])
    index=noVote.index(max(noVote))
    for i in range(0,len(noVote)):
        if i==index:
            explode.append(0.1)
        else:
            explode.append(0)
    return candidateName,candidateID,noVote,explode
    
