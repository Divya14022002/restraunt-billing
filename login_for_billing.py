from tkinter import *
import mysql.connector
from PIL import Image,ImageTk
from tkinter import messagebox
#import billing_new
class Signin():
    def Query(self):
         db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
         cursor=db.cursor()
         sql="insert into registered(username,passcode,Emailid,phoneNo)values('"+self.e1.get()+"','"+self.e2.get()+"','"+self.e3.get()+"','"+self.e4.get()+"')"
         cursor.execute(sql)
         db.commit()
         db.close()
         self.window.destroy()
         self.newroot.destroy()
    def Register(self):
        self.newroot=Toplevel(self.root)
        self.l1=Label(self.newroot,text="username:",font="times 18")
        self.l1.place(x=500,y=400)
        self.e1=Entry(self.newroot,width=25,font="times 10",relief=RIDGE,bd=5)
        self.e1.place(x=600,y=400)
        self.l2=Label(self.newroot,text="Password:",font="times 18")
        self.l2.place(x=500,y=500)
        self.e2=Entry(self.newroot,width=25,font="times 10",relief=RIDGE,bd=5)
        self.e2.place(x=620,y=500)
        b0=Button(self.newroot,width=10,text="Next",relief=RIDGE,bd=5,command=lambda:s.info())
        b0.place(x=700,y=600)
    def info(self):
            self.window=Toplevel(self.newroot)
            self.l3=Label(self.window,text="Email ID:",font="times 18")
            self.l3.place(x=500,y=400)
            self.e3=Entry(self.window,width=25,font="times 10",relief=RIDGE,bd=5)
            self.e3.place(x=600,y=400)
            self.l4=Label(self.window,text="Phone Number:",font="times 18")
            self.l4.place(x=500,y=500)
            self.e4=Entry(self.window,width=25,font="times 10",relief=RIDGE,bd=5)
            self.e4.place(x=670,y=500)
            b1=Button(self.window,width=10,text="finish",relief=RIDGE,bd=5,command=lambda:s.Query())
            b1.place(x=700,y=600)
    def submitact(self):
        user=e0.get()
        passc=e8.get()
        try:
           db=mysql.connector.connect(user='root',password='Yavatmal@12',host='127.0.0.1',database='restraunt')
           cursor=db.cursor()
           saveQuery="select * from registered where username=%s AND passcode=%s"
           cursor.execute(saveQuery,(user,passc))
           username=cursor.fetchone()
           if username:
               import billing_new
               db.close()
           else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            db.close()
        except mysql.connector.Error as err:
             messagebox.showerror("Database Error", f"An error occurred: {err}")
    
         #import billing_new
         #db.close()
        
        
root=Tk()
root.title("Billing")
img_old=Image.open('D:\Python class\GUI\\bill\\bg.png')
s=Signin()
img_resize=img_old.resize((2000,1024))
my_img=ImageTk.PhotoImage(img_resize)
l0=Label(root,image=my_img)
l0.pack()
l=Label(root,text='Welcome',font='Ariel 130 bold italic')
l.place(x=350,y=100)
l1=Label(root,text="User ID:",font="times 18")
l1.place(x=500,y=400)
e0=Entry(width=25,font="times 10",relief=RIDGE,bd=5)
e0.place(x=600,y=400)
l2=Label(root,text="Password:",font="times 18")
l2.place(x=500,y=500)
e8=Entry(width=25,font="times 10",relief=RIDGE,bd=5)
e8.place(x=620,y=500)
b=Button(root,width=15,text="Sign up",relief=RIDGE,bd=5,command=lambda:s.Register())
b.place(x=500,y=600)
b1=Button(root,width=15,text="Login",relief=RIDGE,bd=5,command=lambda:s.submitact())
b1.place(x=700,y=600)
mainloop()

