from tkinter import *
import os

a=Tk()

l1=Label(a,text="Item Name")
l2=Label(a,text="Item Desciption")
l3=Label(a,text="Model No")
l4=Label(a,text="Price")
l5=Label(a,text="Delivery time")

l1.grid(column=1,row=1)
l2.grid(column=1,row=2)
l3.grid(column=1,row=3)
l4.grid(column=1,row=4)
l5.grid(column=1,row=5)

s1=StringVar()
e1=Entry(a,textvariable=s1)
e1.grid(column=2,row=1)

s2=StringVar()
e2=Entry(a,textvariable=s2)
e2.grid(column=2,row=2)

s3=StringVar()
e3=Entry(a,textvariable=s3)
e3.grid(column=2,row=3) 

s4=StringVar()
e4=Entry(a,textvariable=s4)
e4.grid(column=2,row=4) 

s5=StringVar()
e5=Entry(a,textvariable=s5)
e5.grid(column=2,row=5)

count=0

def add():
    print('Add clicked')
    f=open("pythondb.txt","a+")
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    f.writelines(a+" "+b +" "+c+" "+d+" "+e+" "+"\n")
    f.close
    
def next():
    f=open("pythondb.txt",'r')
    global count
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
        l=l.split()
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    
    f.close()
    count=count+1
    
def previous():
    f=open("pythondb.txt",'r')
    global count
    i=count
    while(i>0):
        l=f.readline()
        i=i-1
        l=l.split()
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    f.close()
    count=count-1

    
def first():
    f=open("pythondb.txt",'r')
    global count
    i=count
    l=f.readline()
    i=i-i
    l=l.split()
    

   
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
   
    f.close()
    count=count-count
    
def last():
    f=open("pythondb.txt",'r')       
    a=sum(1 for i in open("pythondb.txt"))-1
    print("last record is:",a+1)
   
    l=f.readlines()[a]
    d=l.split()
    s1.set(d[0])
    s2.set(d[1])
    s3.set(d[2])
    s4.set(d[3])
    s5.set(d[4])
    f.close()

def delete():
     with open("pythondb.txt",'r') as f:
         d=f.readlines()
    
     new = []
     for line in d:
         data = line.strip().split()
         if len(data)!=0 and data[2] != e3.get(): new.append(line)
     with open("pythondb.txt",'w') as fp:
         for line in new:   
             fp.write(line)
 
def search():
    entryid=s3.get()
    print(entryid)
    f=open("pythondb.txt",'r')       
    l=f.readlines()
    for i in l:
        d=i.split()
        print(d)
        if(d[2]==entryid):
            
            s1.set(d[0])
            s2.set(d[1])
            s3.set(d[2])
            s4.set(d[3])
            s5.set(d[4])
    f.close()

    
def update():
    x1=e1.get()
    x2=e2.get()
    x3=e3.get()
    x4=e4.get()
    x5=e5.get()
    with open("pythondb.txt",'r') as f:
              d=f.readlines()   
    new=[]
    
    for line in d:
              data=line.strip().split()
              if len(data)!=0 and data[2]!=c3: new.append(line)
              else:
                  new.append(str(x1)+' '+str(x2)+' '+str(x3)+' '+str(x4)+' '+str(x5)+"\n")
    with open("pythondb.txt",'w') as fp:
              for line in new:
                  fp.write(line)
            
 
b1=Button(a, text= "First",command=first)
b1.grid(column=1, row=8,columnspan=2)

b2=Button(a, text= "Next",command=next)
b2.grid(column=2, row=8,columnspan=2)

b3=Button(a, text= "Previous",command=previous)
b3.grid(column=3, row=8)

b4=Button(a, text= "Last",command=last)
b4.grid(column=4, row=8)

b5=Button(a, text= "Add", command=add)
b5.grid(column=1, row=9,columnspan=2)

b6=Button(a, text= "Delete",command=delete)
b6.grid(column=2, row=9, columnspan=2)

b7=Button(a, text= "Search",command=search)
b7.grid(column=3, row=9)

b8=Button(a, text= "Update",command=update)
b8.grid(column=4, row=9)
a.mainloop()


