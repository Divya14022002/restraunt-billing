from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
     
class Bill():
  def q(self):
     db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
     cursor=db.cursor()
     sql="select*from itemcater where active1=True"
     cursor.execute(sql)
     records=cursor.fetchall()
  def dis(self):
        val=0
        self.T=Text(window,height=0,width=10,font="times 18")
        for row in l.get_children():
          val=val+l.item(row)["values"][3]
        self.T.place(x=630,y=320)
        self.T.insert('end',val)
  def dis1(self):
        val=0
        self.T1=Text(window,height=0,width=10,font="times 18")
        for row in l.get_children():
          val=val+l.item(row)["values"][4]
        r="Total:"+str(val)
        self.T1.place(x=830,y=320)
        self.T1.insert('end',r)
  def update(self):
          qt=0
          for rl in self.l.get_children():
             if self.l.item(rl)["values"][1]==self.menu.get():
                         qt+=int(qty.get())
                         a1=self.r*int(qt)
             self.l.set(rl,"#4",qt)
             self.l.set(rl,"#5",a1)
  def confirm(self):
     db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
     cursor=db.cursor()
     sql="select*from itemcater where active1=True"
     cursor.execute(sql)
     records=cursor.fetchall()
     for record in records:
        if record[1]==menu.get():
            self.r=record[2]
     qt=int(qty.get())
     a=self.r*int(qt)
     for rl in l.get_children():
        if l.item(rl)["values"][1]==menu.get():
                         r=qt+qt
                         a1=self.r*int(qt)
    
     global iid
     iid=iid+1
     l.insert('','end',values=(iid,menu.get(),self.r,qt,a))
     #z.update()
     qty.delete(0,'end')
     menu.set("select an item")
  def Data(self):
       z.conn()
       v=""
       for r in l.get_children():
            v=v+","+(l.item(r)["values"][1])

       val=0
       for row in l.get_children():
            val=val+l.item(row)["values"][4]
       uv=v
       rt=val
       sql="insert into customers(customer_name,customer_number,Items,Total)values('"+n.get()+"','"+n1.get()+"','"+uv+"','"+str(rt)+"')"
       cursor.execute(sql)
  def Bn(self):
    z.conn()
    sql="Select Bill_no from customers where customer_name='"+self.n.get()+"'"
    cursor.execute(sql)
  def Total(self):
     
      z.Data()
      val=0
      for row in l.get_children():
         val=val+l.item(row)["values"][4]
      self.frame=Frame(window,width=500,height=390,highlightbackground="white",highlightthickness=2)
      self.frame.place(x=1000,y=400)
      l0=Label(self.frame,text="----------------------------------------------------")
      l0.grid(row=1,column=0)
      l1=Label(self.frame,text="customer name:"+n.get(),font="times 10")
      l1.grid(row=2,column=0)
      l2=Label(self.frame,text="customer number:"+n1.get(),font="times 10")
      l2.grid(row=3,column=0)
      l3=Label(self.frame,text="---------------------------------------------------------")
      l3.grid(row=4,column=0)
      v=""
      for row in l.get_children():
         v=v+"\n"+l.item(row)["values"][1]
         l4=Label(self.frame,text=v,font="times 10")
         l4.grid(row=4,column=0)
      def item():
         v=""
         for r in l.get_children():
             v=v+"\n"+str(l.item(r)["values"][4])
             l5=Label(self.frame,text=v,font="times 10")
             l5.grid(row=4,column=1)
      item()
      l6=Label(self.frame,text="-------------------------------------------")
      l6.grid(row=11,column=0)
      label=Label(self.frame,text="Your total bill is:"+str(val),font="arial 10 bold ")
      label.grid(row=12,column=0)
      z.dis()
      z.dis1()
      db.commit()
      #db.close()
      #l4=Label(self.frame,text="Bill_no:"+str(z.Bn()),font="times 10")
      #l4.grid(row=0,column=0)
      
      
      
        
  def Reset(self):
      (self.T).destroy()
      (self.T1).destroy()
      (self.frame).destroy()
      n.delete(0,'end')
      n1.delete(0,'end')
      for row in l.get_children():
                 l.delete(row)
      mainp()
      
      
      
      
                

class new_window(Bill):
 def conn(self):
     db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
     cursor=db.cursor()
 def Opennew(self):
    self.newWindow=Toplevel(window)
    self.newWindow.title("Updating items")
    self.newWindow.configure(bg='Grey')
    self.Item=Label(self.newWindow,text="Item to be added:",font="arial 13 bold")
    self.Item.place(x=320,y=150)
    self.n=Entry(self.newWindow,width=25,font="times 10",relief=RIDGE,bd=5)
    self.n.place(x=550,y=150)
    self.Price=Label(self.newWindow,text="Price:",font="arial 13 bold")
    self.Price.place(x=750,y=150)
    self.n1=Entry(self.newWindow,width=25,font="times 13",relief=RIDGE,bd=5)
    self.n1.place(x=890,y=150)
    self.Item1=Label(self.newWindow,text="Item to be deleted:",font="arial 13 bold")
    self.Item1.place(x=320,y=350)
    self.n0=Entry(self.newWindow,width=25,font="times 13",relief=RIDGE,bd=5)
    self.n0.place(x=550,y=350)
    self.bt1=Button(self.newWindow,text="OK",height=1,width=6,relief=RIDGE,bd=5,command=lambda:z.ins())
    self.bt1.place(x=450,y=200)
    self.bt2=Button(self.newWindow,text="Delete",height=1,width=6,relief=RIDGE,bd=5,command=lambda:z.Delete())
    self.bt2.place(x=450,y=400)
 def ins(self):
      z.conn()
      sql="insert into itemcater(discription,rate,active1)values('"+(self.n).get()+"','"+(self.n1).get()+"',True)"
      cursor.execute(sql)
      (n).delete(0,'end')
      (n1).delete(0,'end')
      db.commit()
      db.close()  
 def Delete(self):
      z.conn()
      sql="update itemcater set active1=False where discription='"+(self.n0).get()+"'"
      cursor.execute(sql)
      (self.n0).delete(0,'end')
      db.commit()
      db.close()


window =Tk()
iid=0
z=new_window()
window.title("Billing")
menu = StringVar()
window.configure(bg='Grey')
l = ttk.Treeview(window, columns=("c1", "c2", "c3",
                 "c4", "c5"), show="headings",selectmode='browse', height=9)
scrollbar=ttk.Scrollbar(window,orient='vertical',command=l.yview)
scrollbar.place(x=0,y=150)
l.configure(xscrollcommand=scrollbar.set)
l.heading('#1', text="sr.no")
l.heading('#2', text="particulars")
l.column('#3', anchor=W)
l.heading('#3', text="Rate")
l.column('#4', anchor=W)
l.heading('#4', text="Qty")
l.column('#5', anchor=W)
l.heading('#5', text="Amount")
label1 = Label(window, text="Items:", font="times 13 bold")
label1.place(x=1100, y=150)
menu.set("select an item")
db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
cursor=db.cursor()
sql="select*from itemcater where active1=True"
cursor.execute(sql)
records=cursor.fetchall()
s=[]
for record in records:
        s.append(record[1])
drop=OptionMenu(window, menu,*s)
drop.place(x=1170, y=150)
label2 = Label(window, text="Quantity:", font="times 13 bold")
label2.place(x=1350, y=150)
qty = Entry(window,width=4,relief=RIDGE,bg='lightgrey',bd=5)
qty.place(x=1430, y=150)
b=Button(window,text="Confirm",height=2,width=6,relief=RIDGE,bd=5,command=lambda:z.confirm())
b.place(x=1100,y=200)
b1=Button(window,text="Total",font="arial 18 bold",height=1,bd=5,width=6,relief=RIDGE,command=lambda:z.Total())
b1.place(x=312,y=380)
b2=Button(window,text="Reset",font="arial 18 bold",height=1,width=6,bd=5,relief=RIDGE,command=lambda:z.Reset())
b2.place(x=512,y=380)
btn=Button(window,text="update Items",font="arial 10 bold",relief=RIDGE,command=lambda:z.Opennew())
btn.place(x=20,y=10)
name=Label(window,text="Customer name:",font="times 13 bold")
name.place(x=20,y=50)
n=Entry(window,width=25,font="times 10",relief=RIDGE,bd=5)
n.place(x=150,y=50)
number=Label(window,text="Customer number:",font="times 13 bold")
number.place(x=350,y=50)
n1=Entry(window,width=25,font="times 10",relief=RIDGE,bd=5)
n1.place(x=500,y=50)        
l.place(x=20,y=100)
mainloop()
      
            
