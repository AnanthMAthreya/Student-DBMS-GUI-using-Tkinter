#Type the USN in this format->'RVCE22B**XXX', where ** is the branch code and XXX is the roll number
from tkinter import *
from tkinter import ttk
import pandas as pd
w = Tk()
datalist=[]
USNlist=[]
def DestroyWidgets():
    for widget in w.winfo_children():
        widget.destroy()

def TeacherPage():
    DestroyWidgets()
    w.title('Database-Options')
    label1=Label(w,text="Welcome to the student DBMS.",fg='blue',
    font=('algerian',20)).place(x=450,y=0)
    label=Label(w,text="What do you want to do?",fg='blue',
    font=('algerian',20)).place(x=450,y=50)
    o1=Button(w,text="Enter student data",width=30,height=1,font=10,
    command=DataEntry1).place(x=100,y=100)
    o2=Button(w,text="View student table",width=30,height=1,font=10,
    command=viewWholeTable).place(x=800,y=100)
    o3=Button(w,text='View student marks',width=30,height=1,font=10,
    command=viewStudentMarks).place(x=450,y=200)
    w.mainloop()
    
def DataEntry1():
    DestroyWidgets()
    USNstr=StringVar()
    Namestr=StringVar()
    Marks1str=StringVar()
    Marks2str=StringVar()
    Marks3str=StringVar()
    Marks4str=StringVar()
    Marks5str=StringVar()
    Marks6str=StringVar()
    
    w.title('Data Entry')
    introLabel=Label(w,text='Data Entry',fg='blue',
    font=('algerian',20)).place(x=100,y=0)
    label1=Label(w,text="Enter student USN number",font=10).place(x=100,y=100)
    usnentry=Entry(w,textvariable=USNstr,width=20).place(x=350,y=100) 
    label2=Label(w,text='Enter student name',font=10).place(x=100,y=200)
    nameentry=Entry(w,textvariable=Namestr,width=40).place(x=350,y=200)
    label3=Label(w,text='Enter marks:-Subject 1',font=10).place(x=100,y=300)
    marksentry1=Entry(w,textvariable=Marks1str,width=10).place(x=350,y=300)
    label4=Label(w,text='Subject 2',font=10).place(x=400,y=300)
    marksentry=Entry(w,textvariable=Marks2str,width=10).place(x=500,y=300)
    label5=Label(w,text='Subject 3',font=10).place(x=600,y=300)
    marksentry=Entry(w,textvariable=Marks3str,width=10).place(x=700,y=300)
    label6=Label(w,text='Subject 4',font=10).place(x=220,y=400)
    marksentry1=Entry(w,textvariable=Marks4str,width=10).place(x=350,y=400)
    label7=Label(w,text='Subject 5',font=10).place(x=400,y=400)
    marksentry=Entry(w,textvariable=Marks5str,width=10).place(x=500,y=400)
    label8=Label(w,text='Subject 6',font=10).place(x=600,y=400)
    marksentry=Entry(w,textvariable=Marks6str,width=10).place(x=700,y=400)
    button1=Button(w,text='<-Back',width=20,height=1,font=10
    ,command=TeacherPage).place(x=100,y=500)
    button2=Button(w,text='View table',width=20,height=1,font=10,command=lambda
    :ifViewTable(USNstr.get(), Namestr.get(), Marks1str.get(),
    Marks2str.get(),Marks3str.get(),Marks4str.get(),Marks5str.get(),
    Marks6str.get())).place(x=761,y=500)
    
def getValues(x,y,m1,m2,m3,m4,m5,m6):
    if x!='' and y!='' and m1!='' and m2!='' and m3!='' and m2!='' and m5!='' and m6!='':
        if USNPatCheck(x):
            if x not in USNlist:
                details=[]
                details.append(x)
                details.append(y)
                addMarks(m1,details)
                addMarks(m2,details)
                addMarks(m3,details)
                addMarks(m4,details)
                addMarks(m5,details)
                addMarks(m6,details)
                datalist.append(details)
                USNlist.append(x)
 
def addMarks(x,y):
    try:
        x=int(x)
    except ValueError:
        pass
    y.append(x)
    

def ifViewTable(x,y,m1,m2,m3,m4,m5,m6):
    getValues(x,y,m1,m2,m3,m4,m5,m6)
    displayTable()
    button1=Button(w,text="<-Back",width=20,height=1,font=10,
    command=DataEntry1).place(x=0,y=500)
    button3=Button(w,text='Delete items',width=20,height=1,font=10,
    command=Deleteitems).place(x=875,y=500)
    
    
def ifViewTable1():
    displayTable()
    button1=Button(w,text="<-Back",width=20,height=5,
    command=DataEntry1).place(x=0,y=500)
    button3=Button(w,text='Delete items',width=20,height=5,
    command=Deleteitems).place(x=875,y=500)
    

def displayTable():
    DestroyWidgets()
    datalist.sort()
    label1=Label(w,text="Student Table",fg='blue',
    font=('algerian',20)).place(x=450,y=0)
    table=ttk.Treeview(w)
    table['columns']=('1','2','3','4','5','6','7','8')
    for column in table['columns']:
        if column=='2':
            table.column(column,width=200)
        else:
            table.column(column,width=100)
    table.heading('1',text='Student USN')
    table.heading('2',text='Name')
    table.heading('3',text='Subject 1 marks')
    table.heading('4',text='Subject 2 marks')
    table.heading('5',text='Subject 3 marks')
    table.heading('6',text='Subject 4 marks')
    table.heading('7',text='Subject 5 marks')
    table.heading('8',text='Subject 6 marks')
    for i,row in enumerate(datalist):
        table.insert('',i,values=row)
    table.place(x=0,y=100)
     
def Deleteitems():
    for widget in w.winfo_children():
        widget.destroy()
    delitem=StringVar()
    heading=Label(w,text='Delete items',fg='blue',
    font=('algerian',20)).place(x=100,y=0)
    label1=Label(w,text='Enter the Usn to delete',font=10).place(x=100,y=100)
    entry1=Entry(w,textvariable=delitem,width=20).place(x=350,y=100)
    button1=Button(w,text='<-Back',width=20,height=1,font=10,
    command=ifViewTable1).place(x=100,y=200)
    button2=Button(w,text='Delete',width=20,height=1,font=10,
    command=lambda:Deletebutton(delitem.get())).place(x=400,y=200)
    w.mainloop()

def Deletebutton(item):
    status=False
    for i in datalist:
        if i[0]==item:
            datalist.remove(i)
            status=True
    displayTable()
    if status==True:
        label1=Label(w,text='Details deleted',font=10).place(x=500,y=400)
    else:
        label2=Label(w,text='USN not found',font=10).place(x=500,y=400)
    button1=Button(w,text='Add data',width=20,height=1,font=10,
    command=DataEntry1).place(x=0,y=500)
    button2=Button(w,text='Delete data',width=20,height=1,font=10,
    command=Deleteitems).place(x=875,y=500)
    
def viewWholeTable():
    for i in datalist:
        i.append(sum(i[2:]))
        i.append(sum(i[2:-1])/3)
    DestroyWidgets()
    datalist.sort()
    label1=Label(w,text="Student Table",fg='blue',
    font=('algerian',20)).place(x=450,y=0)
    table=ttk.Treeview(w)
    table['columns']=('1','2','3','4','5','6','7','8','9','10')
    for column in table['columns']:
        if column=='2':
            table.column(column,width=200)
        elif column=='9':
            table.column(column,width=50)
        else:
            table.column(column,width=100)
    table.heading('1',text='Student USN')
    table.heading('2',text='Name')
    table.heading('3',text='Subject 1 marks')
    table.heading('4',text='Subject 2 marks')
    table.heading('5',text='Subject 3 marks')
    table.heading('6',text='Subject 4 marks')
    table.heading('7',text='Subject 5 marks')
    table.heading('8',text='Subject 6 marks')
    table.heading('9',text='Total')
    table.heading('10',text='Percentage')
    button1=Button(w,text='<-Back',width=20,height=1,font=10,
    command=TeacherPage).place(x=0,y=500)
    for i,row in enumerate(datalist):
        table.insert('',i,values=row)
    table.place(x=0,y=100)
    
def viewStudentMarks():
    DestroyWidgets()
    heading=Label(w,text='View Student Data',fg='blue',
    font=('algerian',20)).place(x=450,y=0)
    backbutton=Button(w,text='<-Back',width=20,height=1,font=10,
    command=TeacherPage).place(x=0,y=0)
    USNstr=StringVar()
    label1=Label(w,text="Enter student USN number",font=10).place(x=100,y=100)
    usnentry=Entry(w,textvariable=USNstr,width=20).place(x=350,y=100)
    subbutton=Button(w,text='View details',width=20,height=1,
    font=10,command=lambda:printData(USNstr.get())).place(x=0,y=200)
    
def printData(x):
    for i in datalist:
        i.append(sum(i[2:]))
        i.append(sum(i[2:-1])/3)
    pos=-1
    for i in datalist:
        if i[0]==x:
            pos=datalist.index(i)
    if pos>=0:
        table=ttk.Treeview(w)
        table['columns']=('1','2','3','4','5','6','7','8','9','10')
        for column in table['columns']:
            if column=='2':
                table.column(column,width=200)
            elif column=='9':
                table.column(column,width=50)
            else:
                table.column(column,width=100)
        table.heading('1',text='Student USN')
        table.heading('2',text='Name')
        table.heading('3',text='Subject 1 marks')
        table.heading('4',text='Subject 2 marks')
        table.heading('5',text='Subject 3 marks')
        table.heading('6',text='Subject 4 marks')
        table.heading('7',text='Subject 5 marks')
        table.heading('8',text='Subject 6 marks')
        table.heading('9',text='Total')
        table.heading('10',text='Percentage')
        table.insert('',1,values=datalist[pos])
        table.place(x=0,y=300)
    else:
        for child in w.winfo_children():
            if isinstance(child,ttk.Treeview):
                child.destroy()
        label=Label(w,text='USN not found',font=10).place(x=100,y=300)

def USNPatCheck(x):
    if x[:4].isupper() and x[4:6].isdigit() and x[6:9].isupper() and x[9:].isdigit():
        return True
    else:
        return False
    
    

    
TeacherPage()
