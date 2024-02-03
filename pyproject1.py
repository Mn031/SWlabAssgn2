import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

tfile = "save.txt"
def reads(a):
    global tfile
    try:
        f = open(tfile,'r')
        while True:
            r = f.readline()
            if(len(r)== 0):
                break
            else:
                q = r.split(",")
                if (q[0] == 'T'):
                    a.append(teacher(q[1],q[2],q[3],q[4],q[5]))
                elif(q[0] == 'UG'):
                    a.append(UG_student(q[1],q[2],q[3],q[4],q[5],q[6][0:-1]))
                elif(q[0] == 'PG'):
                    a.append(PG_student(q[1],q[2],q[3],q[4],q[5],q[6][0:-1]))
        f.close()
    except IOError:
        f = open(tfile,'w')
        f.close() 
def saves(a):
    global tfile
    f = open(tfile,'w')
    for i in a:
        if(i.type == 'T'):
            t = i.type + ',' + i.userID + ',' + i.password  + ',' +  i.emp_id + ',' + i.name + ',' + i.dept + '\n'
            f.write(t)
        elif(i.type == 'PG'):
            t = i.type + ',' + i.userID + ',' + i.password  + ',' +  i.name + ',' + i.roll_no + ',' + i.year + ',' + i.dept + '\n'
            f.write(t)
        elif(i.type == 'UG'):
            t = i.type + ',' + i.userID + ',' + i.password  + ',' +  i.name + ',' + i.roll_no + ',' + i.year + ',' + i.dept + '\n'
            f.write(t)
    f.flush()
    f.close()
class person():
    def __init__(self,userID,password):
        self.userID = userID
        self.password = password
class teacher(person):
    def __init__(self, userID, password,emp_id,name,dept):
        super().__init__(userID, password)
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.type = 'T'
class student(person):
    def __init__(self, userID, password):
        super().__init__(userID, password)
class UG_student(student):
    def __init__(self, userID, password,name,roll_no,year,dept):
        super().__init__(userID, password)
        self.roll_no = roll_no
        self.year = year
        self.name = name
        self.dept = dept
        self.type = "UG"
class PG_student(student):
    def __init__(self, userID, password,name,roll_no,year,dept):
        super().__init__(userID, password)
        self.roll_no = roll_no
        self.year = year
        self.name = name
        self.dept = dept
        self.type = "PG"
counter = 3
def namec(name):
    if (name.isalpha() == True):
        return 1
    else:
        return 0
def empty(t):
    if(t == ""):
        return 1
    else:
        return 0
def number(num):
    if(num.isnumeric() == True):
        return 1
    else:
        return 0
def lowercase(password):
    count = 0
    for i in password:
        if (ord(i)>= 97 and ord(i)<= 122):
            count= count+ 1
    return count
def uppercase(password):
    count = 0
    for i in password:
        if (ord(i)>= 65 and ord(i)<= 90):
            count= count+ 1
    return count
def symbol(password):
    count = 0
    j = ['!','@','#','$','%','&','*']
    for i in password:
        if i in j:
            count= count+ 1
    return count
def digit(password):
    count = 0
    for i in password:
        if (ord(i)>= 48 and ord(i)<= 57):
            count= count+ 1
    return count
def usercheck(email,a):
    for i in a:
        if(email == i.userID):
            return 1
def home(a,r,f):
    f.destroy()
    main(a,r)
def userid(email,a,e):
    t1 = email.rfind('@iitkgp.ac.in')
    l = len(email)
    if ( t1 <= 0):
        e.delete(0,len(email))
        messagebox.showerror("Error", "Write the username in the given format")
    elif(usercheck(email,a)== 1):
        e.delete(0,len(email))
        messagebox.showerror("Error", "UserId already exists")
    else:
        return email
def passwordc(password,passw):
    if(uppercase(password) == 0):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "Atleast one uppercase character should be there in the password")
    elif(lowercase(password) == 0):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "Atleast one lowercase character should be there in the password")
    elif(symbol(password) == 0):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "Atleast one symbol should be there in the password")
    elif (len(password) < 8 or len(password) > 12):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "The password should be between 8 to 12 characters")
    elif (' ' in password):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "There should be no spaces in the password")
    elif(digit(password) == 0):
        passw.delete(0,len(password))
        messagebox.showerror("Error", "Atleast one digit should be there in the password")
    else:
        return password
def createup(e,passw,a,r,f):
    j = userid(e.get(),a,e)
    q = passwordc(passw.get(),passw)
    if(j is not None and q is not None):
        a.append(person(j,q))
        teach_stud(r,a,f)
def teach_c(a,r,f,e,e1,e2,j):
    if(empty(e.get()) == 1 or empty(e1.get()) == 1 or empty(e2.get()) == 1):
        messagebox.showerror("Error","No field can be left empty")
        return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
        return
    if (number(e1.get()) == 0 or len(e1.get())!= 3):
        e1.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only the correct roll no")
        return
    for i in a:
        if(i.userID != j.userID and i.type == 'T' and i.emp_id == e1.get()):
            e1.delete(0,len(e1.get()))
            messagebox.showerror("Error","roll no already exists")
            return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
    else:
        teach_add(a,r,f,e,e1,e2)
def teach(a,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title('Teacher')
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    label2 = tk.Label(f,text= 'Enter your emp_id in the form XXX')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    label4 =tk.Label(f,text= 'Enter your department')
    label4.pack()
    combo1 = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo1.pack()
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : teach_c(a,r,f,e,e1,combo1,a[-1]))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :teach_stud(r,a,f))
    button3.pack()
def teach_add(a,r,f,e,e1,e2):
    a[-1] = teacher(a[-1].userID,a[-1].password,e1.get(),e.get(),e2.get())
    f.destroy()
    main(a,r)
def stud(a,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title('student')
    label = tk.Label(f,text= 'Are you a')
    label.pack()
    button1= tk.Button(f,text= 'UG Student',width = 25,command= lambda : UGstud(a,r,f))
    button1.pack()
    button2 = tk.Button(f,text='PG Student',width = 25,command= lambda: PGstud(a,r,f))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :teach_stud(r,a,f))
    button3.pack()
def UGstud_c(a,r,f,e,e1,e2,e3,j):
    if(empty(e.get()) == 1 or empty(e1.get()) == 1 or empty(e2.get()) == 1 or empty(e3.get()) == 1):
        messagebox.showerror("Error","No field can be left empty")
        return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
        return
    if (number(e1.get()) == 0 or len(e1.get())!= 5):
        e1.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only the correct roll no")
        return
    for i in a:
        if((i.userID !=j.userID) and (i.type in ['UG','PG'] ) and i.roll_no == e1.get()):
            e1.delete(0,len(e1.get()))
            messagebox.showerror("Error","roll no already exists")
            return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
    else:
        UGstud_add(a,r,f,e,e1,e2,e3)
def UGstud_add(a,r,f,e,e1,e2,e3):
    a[-1] = UG_student(a[-1].userID,a[-1].password,e.get(),e1.get(),e2.get(),e3.get())
    f.destroy()
    main(a,r)
def UGstud(a,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title("UG Student")
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    label2 = tk.Label(f,text= 'Enter your roll_no in the form XXXXX')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    label3 = tk.Label(f,text= 'Enter your year')
    label3.pack()
    combo = ttk.Combobox(f,values=["First year","Second year","Third year","Fourth year","Fifth year"])
    combo.pack()
    label4 =tk.Label(f,text= 'Enter your department')
    label4.pack()
    combo1 = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo1.pack()
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : UGstud_c(a,r,f,e,e1,combo,combo1,a[-1]))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :stud(a,r,f))
    button3.pack()
def PGstud_c(a,r,f,e,e1,e2,e3,j):
    if(empty(e.get()) == 1 or empty(e1.get()) == 1 or empty(e2.get()) == 1 or empty(e3.get()) == 1):
        messagebox.showerror("Error","No field can be left empty")
        return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
        return
    if (number(e1.get()) == 0 or len(e1.get())!= 5):
        e1.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only the correct roll no")
        return
    for i in a:
        if((i.userID != j.userID) and (i.type in ['UG','PG'] ) and i.roll_no == e1.get()):
            e1.delete(0,len(e1.get()))
            messagebox.showerror("Error","roll no already exists")
            return
    if (namec(e.get()) == 0):
        e.delete(0,len(e.get()))
        messagebox.showerror("Error","Enter only alphabetic names")
    else:
        PGstud_add(a,r,f,e,e1,e2,e3)
def PGstud_add(a,r,f,e,e1,e2,e3):
    a[-1] = PG_student(a[-1].userID,a[-1].password,e.get(),e1.get(),e2.get(),e3.get())
    f.destroy()
    main(a,r)
def PGstud(a,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title("UG Student")
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    label2 = tk.Label(f,text= 'Enter your roll_no in the from XXXXX')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    label3 = tk.Label(f,text= 'Enter your year')
    label3.pack()
    combo = ttk.Combobox(f,values=["First year","Second year"])
    combo.pack()
    label4 =tk.Label(f,text= 'Enter your department')
    label4.pack()
    combo1 = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo1.pack()
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : PGstud_c(a,r,f,e,e1,combo,combo1,a[-1]))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :stud(a,r,f))
    button3.pack()
def teach_stud(r,a,f):
    f.destroy()
    p = Frame(r)
    p.pack()
    label = tk.Label(p,text= 'Are you a')
    label.pack()
    button1= tk.Button(p,text= 'Teacher',width = 25,command= lambda : teach(a,r,p))
    button1.pack()
    button2 = tk.Button(p,text='Student',width = 25,command = lambda : stud(a,r,p))
    button2.pack()
def signup(a,f,r):
    f.destroy()
    f= Frame(r)
    f.pack()
    label = tk.Label(f,text = 'Enter your desired username in ***@iitkgp.ac.in format')
    label.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    label1 = tk.Label(f,text = 'Enter the password')
    label1.pack()
    passw = tk.Entry(f,width = 50,borderwidth= 5,show = "*")
    passw.pack()
    r.title('Sign Up')
    button = tk.Button(f, text='Enter', width=25,command= lambda:createup(e,passw,a,r,f))
    button.pack()
    button1 = tk.Button(f,text = 'Home',width = 25,fg = 'green',command = lambda :home(a,r,f) )
    button1.pack()


def updatePG(a,i,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title("PG Student Update")
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    e.insert(0,i.name)
    label2 = tk.Label(f,text= 'Enter your roll_no')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    e1.insert(0,i.roll_no)
    label3 = tk.Label(f,text= 'Enter your year')
    label3.pack()
    combo = ttk.Combobox(f,values=["First year","Second year"])
    combo.pack()
    combo.insert(0,i.year)
    label4 =tk.Label(f,text= 'Enter your department')
    label4.pack()
    combo1 = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo1.pack()
    combo1.insert(0,i.dept)
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : PGstud_c(a,r,f,e,e1,combo,combo1,i))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :showPG(a,i,r,f))
    button3.pack()
def showPG(a,i,r,f):
    f.destroy()
    f = LabelFrame(r,text = "PG Student")
    f.pack()
    r.title("PG Student")
    label2 = Label(f,text= "Userid: {}".format(i.userID))
    label2.pack()
    label3 = Label(f,text= "Name: {}".format(i.name))
    label3.pack()
    label4 = Label(f,text= "Roll_no: {}".format(i.roll_no))
    label4.pack()
    label5 = Label(f,text= "year {}".format(i.year))
    label5.pack()
    label6 = Label(f,text= "department {}".format(i.dept))
    label6.pack()
    button = tk.Button(f, text='Update', width=25,command=lambda : updatePG(a,i,r,f))
    button.pack()
    button1 = tk.Button(f,text = 'Home',width = 25,fg = 'green',command = lambda :home(a,r,f) )
    button1.pack()
    button2 = tk.Button(f,text = 'Delete',width = 25,command=lambda : delete(a,i,r,f) )
    button2.pack()
def updateUG(a,i,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title("UG Student Update")
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    e.insert(0,i.name)
    label2 = tk.Label(f,text= 'Enter your roll_no')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    e1.insert(0,i.roll_no)
    label3 = tk.Label(f,text= 'Enter your year')
    label3.pack()
    combo = ttk.Combobox(f,values=["First year","Second year","Third year","Fourth year","Fifth year"])
    combo.pack()
    combo.insert(0,i.year)
    label4 =tk.Label(f,text= 'Enter your department')
    label4.pack()
    combo1 = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo1.pack()
    combo1.insert(0,i.dept)
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : UGstud_c(a,r,f,e,e1,combo,combo1,i))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :showUG(a,i,r,f))
    button3.pack()
def showUG(a,i,r,f):
    f.destroy()
    f = LabelFrame(r,text = "UG Student")
    f.pack()
    r.title("UG Student")
    label2 = Label(f,text= "Userid: {}".format(i.userID))
    label2.pack()
    label3 = Label(f,text= "Name: {}".format(i.name))
    label3.pack()
    label4 = Label(f,text= "Roll_no: {}".format(i.roll_no))
    label4.pack()
    label5 = Label(f,text= "year {}".format(i.year))
    label5.pack()
    label6 = Label(f,text= "department {}".format(i.dept))
    label6.pack()
    button = tk.Button(f, text='Update', width=25,command=lambda : updateUG(a,i,r,f))
    button.pack()
    button1 = tk.Button(f,text = 'Home',width = 25,fg = 'green',command = lambda :home(a,r,f) )
    button1.pack()
    button2 = tk.Button(f,text = 'Delete',width = 25,command=lambda : delete(a,i,r,f) )
    button2.pack()
def updateT(a,i,r,f):
    f.destroy()
    f = Frame(r)
    f.pack()
    r.title("Teacher Update")
    label1 = tk.Label(f,text = 'Enter your name')
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    e.insert(0,i.name)
    label2 = tk.Label(f,text= 'Enter your emp_id')
    label2.pack()
    e1 = tk.Entry(f,width = 50,borderwidth= 5)
    e1.pack()
    e1.insert(0,i.emp_id)
    label3 =tk.Label(f,text= 'Enter your department')
    label3.pack()
    combo = ttk.Combobox(f,values=['Aerospace Engineering', 'Agricultural and Food Engineering', 'Architecture and Regional Planning', 'Chemical Engineering', 'Civil Engineering', 'Computer Science and Engineering', 'Electrical Engineering', 'Electronics and Electrical Communication Engineering', 'Geology and Geophysics', 'Industrial Engineering and Management', 'Mechanical Engineering', 'Metallurgical and Materials Engineering', 'Mining Engineering', 'Ocean Engineering and Naval Architecture', 'School of Planning and Architecture', 'Chemistry', 'Mathematics', 'Physics', 'Centre for Education Technology', 'Economics', 'English', 'History', 'Humanities and Social Sciences', 'Industrial Design', 'Languages', 'Management Studies', 'Philosophy', 'Psychology', 'Sociology', 'Centre for Ocean, River, Atmosphere and Land Sciences (CORAL)', 'Rajendra Mishra School of Engineering Entrepreneurship (RMSEE)', 'School of Medical Science and Technology (SMST)', 'School of Policy and Governance (SPG)'])
    combo.pack()
    combo.insert(0,i.dept)
    button2 = tk.Button(f,text='Enter',width = 25,command = lambda : teach_c(a,r,f,e,e1,combo,i))
    button2.pack()
    button3 = tk.Button(f,text= "previous",fg = 'blue',width = 25,command = lambda :showT(a,i,r,f))
    button3.pack()
def delete(a,i,r,f):
    f.destroy()
    a.remove(i)
    del i
    main(a,r)
def showT(a,i,r,f):
    f.destroy()
    f = LabelFrame(r,text = "Teacher")
    f.pack()
    r.title("Teacher")
    label2 = Label(f,text= "Userid: {}".format(i.userID))
    label2.pack()
    label3 = Label(f,text= "Name: {}".format(i.name))
    label3.pack()
    label4 = Label(f,text= "Emp_ID {}".format(i.emp_id))
    label4.pack()
    label5 = Label(f,text= "department {}".format(i.dept))
    label5.pack()
    button = tk.Button(f, text='Update', width=25,command=lambda : updateT(a,i,r,f))
    button.pack()
    button1 = tk.Button(f,text = 'Home',width = 25,fg = 'green',command = lambda :home(a,r,f) )
    button1.pack()
    button2 = tk.Button(f,text = 'Delete',width = 25,command=lambda : delete(a,i,r,f) )
    button2.pack()
def show(a,i,r,f):
    if(i.type == 'T'):
        showT(a,i,r,f)
    elif(i.type == 'UG'):
        showUG(a,i,r,f)
    elif(i.type== 'PG'):
        showPG(a,i,r,f)
def passcheck(a,i,passw,r,f):
    global counter
    if(i.password!=passw.get()):
        passw.delete(0,len(passw.get()))
        counter= counter -1
        messagebox.showerror("Error", "Wrong password\n No of attempts remaining {}".format(counter))
        if(counter == 0):
            delete(a,i,r,f)
        return
    else:
        counter = 3
        show(a,i,r,f)
def usericheck(a,e,passw,r,f):
    for i in a:
        if(e.get()==i.userID):
            passcheck(a,i,passw,r,f)
            break
    else:
        e.delete(0,len(e.get()))
        passw.delete(0,len(passw.get()))
        messagebox.showerror("Error", "Username doesn't exist")            
def signin(a,f,r):
    f.destroy()
    f= Frame(r)
    f.pack()
    r.title("signin")
    label1 = Label(f,text= "Enter your username")
    label1.pack()
    e = tk.Entry(f,width = 50,borderwidth= 5)
    e.pack()
    label2 = tk.Label(f,text = 'Enter the password')
    label2.pack()
    passw = tk.Entry(f,width = 50,borderwidth= 5,show = "*")
    passw.pack()
    button = tk.Button(f, text='Enter', width=25,command= lambda:usericheck(a,e,passw,r,f))
    button.pack()
    button1 = tk.Button(f,text = 'Home',width = 25,fg = 'green',command = lambda :home(a,r,f) )
    button1.pack()

def start(a,r):
    reads(a)
    main(a,r)
def quit(a,r):
    saves(a)
    r.quit()
def main(a,r):
    f = Frame(r)
    f.pack()
    main_label = tk.Label(f,text="Hello What do u want to do",font = ('bold',10))
    main_label.pack()
    button1 = tk.Button(f,text = "Sign up",width = 25,borderwidth=5,padx=5,pady=5,command= lambda : signup(a,f,r))
    button1.pack()
    button2 = tk.Button(f,text = "Sign in",width = 25,borderwidth=5,padx=5,pady=5,command= lambda : signin(a,f,r))
    button2.pack()
    button3 = tk.Button(f,text = "Exit",width = 25,borderwidth=5,padx=5,pady=5,fg='red',command = lambda: quit(a,r))
    button3.pack()


r = tk.Tk()
r.geometry('500x500')
r.title('Welcome')
a = list()
start(a,r)
r.mainloop()