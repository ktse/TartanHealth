import http.client
import time

#Implemented sickTypeCounts per day 2:40

#already copied all the code 

students=set()
sickPerDay=[]
loginUser = None

class Student(object):
    def __init__(self,andrewID,location,sickness = None,when = None):
        self.loc = location
        self.sickness= sickness
        self.when = when
        self.andrewID = andrewID
        self.sickDays=[]
        
    def __repr__(self):
        return self.andrewID
        
    def __eq__(self, other):
        return isinstance(other,Student)and self.andrewID==other.andrewID

    def __hash__(self):
        return hash(self.andrewID)

    def getLoc(self):
        return self.loc
    
    def getWhen(self):
        if(len(self.sickDays)!=0):
            return self.sickDays[-1]
        
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
            self.sickDays.append((date, date)) #adds a new sick date.            
    
    def updateSickDays(self):
        if(len(sickDays)!=0 and self.sickness!=None):
            (x,y)=self.sickDays[-1]
            self.sickDays[-1]=(x,y+1)
            if(y-x>13):
                self.sickness=None

def updateSickness(student, sickness):
    if student != None:
        student.setSickness(sickness)

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
sickDorms["Hill"]=None
sickDorms["Donner"]=None
sickDorms["Morewood"]=None
sickDorms["Stever"]=None
sickDorms["Mudge"]=None
sickDorms["RezShir"]=None
sickDorms["Other"]=None

sickType=dict()
sickType["Cold"]=None
sickType["Fever"]=None
sickType["Flu"]=None
sickType["Other"]=None
sickType["Healthy"]=None

def clearData():
    global sickDorms
    global sickType
    global students
    global sickPerDay
    sickDorms=dict()
    sickDorms["Hill"]=None
    sickDorms["Donner"]=None
    sickDorms["Morewood"]=None
    sickDorms["Stever"]=None
    sickDorms["Mudge"]=None
    sickDorms["RezShir"]=None
    sickDorms["Other"]=None
    
    sickType=dict()
    sickType["Cold"]=None
    sickType["Fever"]=None
    sickType["Flu"]=None
    sickType["Other"]=None
    sickType["Healthy"]=None
    
    students = set()
    
    sickPerDay = []

def getDormPercentageData():
    result = []
    for key in sickDorms:
        if key != "Other":
            result.append((key,sickDorms[key]))
    return result

def getSickTypeData():
    result = []
    for key in sickType:
        result.appedn((key, sickType[key]))
    return result
    

    
def getPercentIncrease():
    if (len(sickPerDay)>1):
        (x1,y1)=sickPerDay[-2]
        (x2,y2)=sickPerDay[-1]
        return y2-y1
    return None
        
def updateSickTypesDay():
    for d in sickType:
        sickType[d].append(getSickTypeDay(d))
        
def updateSickDormsDay():
    for d in sickDorms:
        sickDorms[d].append(getDormCountDay(d))
    
def getMostRecentStudent():
    result = None
    for stud in students:
        if stud.getSickness() != None and (result == None or compareDate(result.getWhen(),stud.getWhen())>0):
            result = stud
    if result != None:
        students.remove(result)
    return result 
    
def getMostRecentStudentDorm(dorm):
    result = None
    for stud in students:
        if stud.getSicknes() != None and stud.getLoc() == dorm and\
           (result == None or compareDate(result.getWhen(), stud.getWhen())>0):
            result = stud
    if result != None:
        students.remove(result)
    return result
    
def topFiveSick():
    global students
    result = []
    numStudents = 5
    for i in range(numStudents):
        temp = getMostRecentStudent()
        if temp != None:
            result.append(temp)
    students.union(set(result))
    return result
    
def topFiveSickDorm(dorm):
    result = []
    numStudents = 5
    for i in range(numStudents):
        result.append(getMostRecentStudentDorm(dorm))
    students.add(set(result))
    return result

def getDate():
    now = time.strftime("%c")
    month = int(now[0:2])
    day = int(now[3:5])
    return (month, day)
    
def validate(andrewId):
    conn = http.client.HTTPConnection("apis.scottylabs.org")
    link = "/directory/v1/andrewID/" + andrewId
    conn.request("HEAD", link)
    res = conn.getresponse()
    if res.reason == "OK": return True
    elif res.reason == "Not Found": return False
    
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('HansChen', '7fbfulgo03')

def makeGraphTimeline(value):
    x=[]; y=[]
    for i in range(len(value)):
        x += [str(value[i][0][1])+"/"+str(value[i][0][2])]
        y += [value[i][1]]
    data = Data([
    Scatter(
        x = x,
        y = y,
        name='Number Of Sick People per Day',
        xsrc='HansChen:1:fef3e7',
        ysrc='HansChen:1:e6e549'
    )
])
    layout = Layout(
    title='Sick People Timeline',
    xaxis=XAxis(
        title='Date',
        titlefont=dict(
            color='#7f7f7f',
            family='Times New Roman',
            size=18
        )
    ),
    yaxis=YAxis(
        title='Number Of sick People',
        titlefont=dict(
            color='#7f7f7f',
            family='Times New Roman',
            size=18
        )
    )
)
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='my-graphs/my plot', auto_open=False)
    return plot_url

def makeBarChart(values):
    x = []
    y = []
    for key in values:
        if key == "Other": continue
        x += [key]
        y += [values[key]]
    
    data = Data([
    Bar(
        x=x,
        y=y,
        name='y',
        xsrc='HansChen:3:6eb5b4',
        ysrc='HansChen:3:df30da'
    )
])
    layout = Layout(
        title='Percentage of Sick people in Each Dorm',
        xaxis=XAxis(
            title='Dorm',
            titlefont=dict(
                color='#7f7f7f',
                family='Times New Roman',
                size=18
        )
    ),
        yaxis=YAxis(
        title='Percentage of Sick People',
        titlefont=dict(
            color='#7f7f7f',
            family='Times New Roman',
            size=18
        )
    )
)
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename = "my-graphs/my-plot1", auto_open=False)

def makePieChart(values):
    x = []
    y = []
    for sicktype in values:
        if sicktype == "Healthy": continue
        x += [sicktype]
        y += [values[sicktype]]
    
    fig = {
    'data': [{'labels': x,
              'values': y,
              'type': 'pie',
              'name': 'Percentage of Each Disease'}],
    'layout': {'title': 'Percentage of Each Disease'}
}
    url = py.plot(fig, filename='my-graphs/pie-chart', auto_open=False)

def makePieChart2(values):
    x = []; y = []; count= 0
    for sicktype in values:
        if sicktype == "Healthy": x += [sicktype]; y+= [values[sicktype]]
        else: count += values[sicktype]
    x += ["Sick"]; y+= [count]
    fig = {
    'data': [{'labels': x,
              'values': y,
              'type': 'pie',
              'name': 'Percentage of Sick People'}],
    'layout': {'title': 'Percentage of Sick People'}
}
    url = py.plot(fig, filename='my-graphs/pie-chart2', auto_open=False)

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def getContents():
    sickos = topFiveSick()
    result = ""
    if len(sickos) == 0: return ""
    for sicko in sickos:
        if len(sicko.sickDays) != 0:
            (x,y)=sicko.sickDays[-1]
            (a,b,c)=x
            result+=sicko.andrewID+" "+str(a)+","+str(b)+","+str(c)+"\n\n"
    return result


