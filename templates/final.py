import httplib
import time

#Implemented sickTypeCounts per day 2:40

students=set()
sickPerDay=[]
loginUser = None

class Student(object):
    def __init__(self,andrewID,location,sickness,when):
        self.loc = location
        self.sickness= sickness
        self.when = when
        self.andrewID = andrewID
        self.sickDays=[]
        
    def __repr__(self):
        return self.andrewID
        
    def __eq__(self, other):
        return isinstance(other,student)and self.andrewID==other.andrewID
    
    def getLoc(self):
        return self.loc
    
    def getWhen(self):
        return self.when
        
    def getAndrewID(self):
        return self.andrewID
    
    def getSickness(self):
        return self.sickness
       
    def getsickDays(self):
        return self.sickDays
        
    def setLoc(self, loc): self.loc = loc
    
    def setWhen(self, when) : self.when = when
    
    def setSickness(self, sickness): 
        self.sickness = sickness
        if sickness != None:
            date = getDate()
            self.sickDays.add((date, date)) #adds a new sick date.            
    
    def updateSickDays(self):
        if(len(sickDays)!=0 and self.sickness!=None):
            (x,y)=self.sickDays[-1]
            self.sickDays[-1]=(x,y+1)
            if(y-x>13):
                self.sickness=None

#Compares which date is earlier.
#If date1 is earlier than date2, it returns negative number.
#If date1 is later than date2, it returns a positive number.
#If date1 is equal to date2, it returns 0
def compareDate(date1, date2):
    (year1, month1, day1) = date1
    (year2, month2, day2) = date2
    yeardif = year1-year2
    monthdif = month1-month2
    daydif = day1-day2
    if yeardif != 0: return yeardif
    if monthdif != 0: return monthdif
    return daydif
    
#basic log in process of student.
#If a student exists in students set,
#return True. Else return False
def login(andrewID):
    for stud in students:
        if(andrewID==stud.andrewID):
            global loginUser
            loginUser = stud
            return True
    return False

def registerNewUser(andrewID, location):
    if(validate(andrewID)):
        enterData(andrewID,location)
        return True
    return False

def enterData(andrewID,location):
    stud = Student(andrewID,location,None,None)
    students.add(stud)
    global loginUser
    loginUser = stud

def refreshDaily():
    sickcount=0
    for stud in students:
        if (stud.sickness!=None):
            self.updateSickDays()
            sickcount+=1
    sickPerDay.append((getDate(),sickcount))
    
def getDormCountDay(dorm):
    sickcount = 0
    for stud in students:
        if(stud.sickness!=None and stud.loc==dorm):
            sickcount+=1
    return (getDate(),sickcount)

def getSickTypeDay(sickness):
    sickcount = 0
    for stud in students:
        if(stud.sickness==sickness):
            sickcount+=1
        elif(sickness=="Healthy" and self.sickness==None):
            sickcount+=1
    return (getDate(),sickcount) 
    
#This goes on website side
sickDorms=dict()
sickDorms["Hill"]=[]
sickDorms["Donner"]=[]
sickDorms["Morewood"]=[]
sickDorms["Stever"]=[]
sickDorms["Mudge"]=[]
sickDorms["RezShir"]=[]
sickDorms["Other"]=[]

sickType=dict()
sickType["Cold"]=[]
sickType["Fever"]=[]
sickType["Flu"]=[]
sickType["Other"]=[]
sickType["Healthy"]=[]

def updateSickTypesDay():
    for d in sickType:
        sickType[d].append(getSickTypeDay(d))
        
def updateSickDormsDay():
    for d in sickDorms:
        sickDorms[d].append(getDormCountDay(d))
    
def getMostRecentStudent():
    result = None
    for stud in students:
        if result == None or compareDate(result.getWhen(),stud.getWhen())>0:
            result = stud
    students.remove(result)
    return result 
    
def topFiveSick(dorm = None):
    result = []
    numStudents = 5
    for i in range(numStudents):
        result.append(getMostRecentStudent())
    students.add(set(result))
    return result


def getDate():
    now = time.strftime("%c")
    month = int(now[0:2])
    day = int(now[3:5])
    return (month, day)
    
def validate(andrewId):
    conn = httplib.HTTPConnection("apis.scottylabs.org")
    link = "/directory/v1/andrewID/" + andrewId
    conn.request("HEAD", link)
    res = conn.getresponse()
    if res.reason == "OK": return True
    elif res.reason == "Not Found": return False
