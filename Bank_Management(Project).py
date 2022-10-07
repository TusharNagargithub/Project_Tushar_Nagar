
from tkinter import*
import tkinter.messagebox
from tkinter import messagebox
import mysql.connector
t=Tk()
t.geometry("2000x900")
t.title("HOME PAGE");
t.config(bg="LightBlue1")
lab1=Label(t,bg="yellow",fg="black",text="Welcome To The Home page of Bank Management System",font=("times new roman","35"))
lab1.place(x=200,y=50)
lab2=Label(t,bg="yellow",fg="black",text="Select your bank ",font=("times new roman","30"))
lab2.place(x=450,y=150)
con=mysql.connector.connect(user='root',password='',host='localhost',database='tushar')

def chk111():
    obj22=Tk()
    obj22.geometry("2000x900")
    obj22.title("CreateAccount")
    obj22.config(bg="DarkOrange1")
    lab41=Label(obj22,bg="yellow",fg="black",text="Please Fill your complete detail for Loan",font=("times new roman","40"))
    lab41.place(x=100,y=20)

    lab51=Label(obj22,bg="black",fg="white",text="Enter your first name",font=("times new roman","30"))
    lab51.place(x=160,y=150)
    a31=Entry(obj22,font=("times new roman","30"))
    a31.place(x=550,y=150)
                
    lab61=Label(obj22,bg="black",fg="white",text="Enter your last name",font=("times new roman","30"))
    lab61.place(x=160,y=210)
    a41=Entry(obj22,font=("times new roman","25"))
    a41.place(x=550,y=210)
                
    lab71=Label(obj22,bg="black",fg="white",text="Enter Pin Card Number",font=("times new roman","30"))
    lab71.place(x=160,y=270)
    a51=Entry(obj22,font=("times new roman","25"))
    a51.place(x=550,y=270)
                
    lab81=Label(obj22,bg="black",fg="white",text="Enter Customer_id ",font=("times new roman","30"))
    lab81.place(x=160,y=330)
    a61=Entry(obj22,font=("times new roman","25"))
    a61.place(x=550,y=330)
                
    lab91=Label(obj22,bg="black",fg="white",text="Enter Password ",font=("times new roman","30"))
    lab91.place(x=160,y=390)
    a71=Entry(obj22,font=("times new roman","30"))
    a71.place(x=550,y=390)

    r11=StringVar()
    lab161=Label(obj22,bg="black",fg="white",text="Select Gender",font=("times new roman","30"))
    lab161.place(x=160,y=450)
                
    rb1=Radiobutton(obj22,font=("times new roman","30"),bg="yellow",text="female",variable=r11,value="female")
    rb1.place(x=550,y=450)
    rb11=Radiobutton(obj22,font=("times new roman","30"),bg="yellow",text="Male",variable=r11,value="male")
    rb11.place(x=700,y=450)

    lab81=Label(obj22,bg="black",fg="white",text="Enter Loan Type ",font=("times new roman","30"))
    lab81.place(x=160,y=510)
    a61=Entry(obj22,font=("times new roman","30"))
    a61.place(x=550,y=510)

    lab82=Label(obj22,bg="black",fg="white",text="Enter your Adress ",font=("times new roman","30"))
    lab82.place(x=160,y=570)
    a62=Entry(obj22,font=("times new roman","30"))
    a62.place(x=550,y=570)

    lab83=Label(obj22,bg="black",fg="white",text="Enter Amount For Loan ",font=("times new roman","30"))
    lab83.place(x=160,y=630)
    lnamt=Entry(obj22,font=("times new roman","30"))
    lnamt.place(x=550,y=630)

def login():
    obj=Tk()
    obj.geometry("2000x900")
    obj.config(bg="PaleGreen1")
    obj.title(" LOGIN")
    lab=Label(obj,bg="yellow",fg="black",text="Please Enter Your Email'id And Password",font=("times new roman","35"))
    lab.place(x=150,y=50)
    lab3=Label(obj,bg="black",fg="white",text="Enter Your Email'id",font=("times new roman","25"))
    lab3.place(x=250,y=200)
    a1=Entry(obj,font=("times new roman","25"))
    a1.place(x=550,y=200)
    lab4=Label(obj,bg="black",fg="white",text="Enter Your Password",font=("times new roman","25"))
    lab4.place(x=250,y=300)
    a2=Entry(obj,font=("times new roman","25"))
    a2.place(x=550,y=300)

    def mylogin():
        if (a1.get()=="Tushar@gmail.com" and a2.get()=="123"):
            obj1=Tk()
            obj1.geometry("2000x900")
            obj1.config(bg="orchid1")

            def createAccount():
                obj2=Tk()
                obj2.geometry("2000x900")
                obj2.title("CreateAccount")
                obj2.config(bg="DarkOrange1")
                lab4=Label(obj2,bg="yellow",fg="black",text="Please enter your complete detail for creating your Account",font=("times new roman","40"))
                lab4.place(x=100,y=20)

                lab5=Label(obj2,bg="black",fg="white",text="Enter your first name",font=("times new roman","30"))
                lab5.place(x=160,y=150)
                a3=Entry(obj2,font=("times new roman","30"))
                a3.place(x=550,y=150)
                
                lab6=Label(obj2,bg="black",fg="white",text="Enter your last name",font=("times new roman","30"))
                lab6.place(x=160,y=210)
                a4=Entry(obj2,font=("times new roman","25"))
                a4.place(x=550,y=210)
                
                lab7=Label(obj2,bg="black",fg="white",text="Enter Pin Card Number",font=("times new roman","30"))
                lab7.place(x=160,y=270)
                a5=Entry(obj2,font=("times new roman","25"))
                a5.place(x=550,y=270)
                
                lab8=Label(obj2,bg="black",fg="white",text="Enter Customer_id ",font=("times new roman","30"))
                lab8.place(x=160,y=330)
                a6=Entry(obj2,font=("times new roman","25"))
                a6.place(x=550,y=330)
                
                lab9=Label(obj2,bg="black",fg="white",text="Enter Password ",font=("times new roman","30"))
                lab9.place(x=160,y=390)
                a7=Entry(obj2,font=("times new roman","30"))
                a7.place(x=550,y=390)

                r1=StringVar()
                lab16=Label(obj2,bg="black",fg="white",text="Select Gender",font=("times new roman","30"))
                lab16.place(x=160,y=450)
                
                rb=Radiobutton(obj2,font=("times new roman","30"),bg="yellow",text="female",variable=r1,value="female")
                rb.place(x=550,y=450)
                rb1=Radiobutton(obj2,font=("times new roman","30"),bg="yellow",text="Male",variable=r1,value="male")
                rb1.place(x=700,y=450)

                def mysql():
                    
                    name=a3.get()+" "+a4.get()
                    customer=a6.get()
                    password=a7.get()
                    
                    cur=con.cursor();
                    cur.execute("insert into studenttable values(%s,%s,%s)",(name,customer,password))
                    con.commit()
                    cur.close()
                    objj=Tk()
                    objj.geometry("2000x900")
                    objj.config(bg="PaleGreen1")
                    lab16=Label(objj,bg="yellow",fg="black",text="Congrats!...Your Account has been Created",font=("times new roman","45"))
                    lab16.place(x=80,y=250)
                    bt13=Button(objj,bg="red",fg="white",text="Click here",font=("times new roman","45"),command=login_bank)
                    bt13.place(x=500,y=450)
                    
                bt1=Button(obj2,bg="red",fg="white",text="Submit mysql",font=("times new roman","35"),command=mysql)
                bt1.place(x=160,y=550)
                
            

            def operationdatabase():
                obj3=Tk()
                obj3.geometry("900x800")
                obj3.title("CreateAccount")
                obj3.config(bg="DarkOrange1")
                lab14=Label(obj3,bg="blue",fg="white",text="Please enter your complete detail for creating your Account",font=("times new roman","25"))
                lab14.place(x=50,y=20)

                lab15=Label(obj3,bg="black",fg="white",text="Enter your name",font=("times new roman","25"))
                lab15.place(x=80,y=100)
                a13=Entry(obj3,font=("times new roman","25"))
                a13.place(x=400,y=100)
                lab16=Label(obj3,bg="black",fg="white",text="Enter your customer_id ",font=("times new roman","25"))
                lab16.place(x=80,y=150)
                a14=Entry(obj3,font=("times new roman","25"))
                a14.place(x=400,y=150)
                lab17=Label(obj3,bg="black",fg="white",text="Enter password ",font=("times new roman","25"))
                lab17.place(x=80,y=200)
                a15=Entry(obj3,font=("times new roman","25"))
                a15.place(x=400,y=200)
            
            lab3=Label(obj1,bg="yellow",fg="black",text="Your Email'id is Verified.................",font=("times new roman","55"))
            lab3.place(x=250,y=50)
            
                
            def login_bank():
                objj=Tk()
                objj.geometry("2000x900")
                objj.config(bg="PaleGreen1")
                objj.title(" LOGIN")
                lb=Label(objj,bg="yellow",fg="black",text="Please Enter Your Username And Password",font=("times new roman","35"))
                lb.place(x=150,y=50)
                lb3=Label(objj,bg="black",fg="white",text="Enter Your Name     ",font=("times new roman","25"))
                lb3.place(x=250,y=200)
                a11=Entry(objj,font=("times new roman","25"))
                a11.place(x=600,y=200)
                lb4=Label(objj,bg="black",fg="white",text="Enter Your Customer'Id",font=("times new roman","25"))
                lb4.place(x=250,y=300)
                a12=Entry(objj,font=("times new roman","25"))
                a12.place(x=600,y=300)

                def chk11():
                    objct12=Tk()
                    objct12.geometry("2000x900")
                    objct12.config(bg="PaleGreen1")
                    objct12.title("Account detail")
                    cur=con.cursor()
                    #######
                    customer=a12.get()
                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer,))
                    data=cur.fetchone()

                    if not data:
                        lb41=Label(objct12,bg="black",fg="white",text="These Customer may not be present",font=("times new roman","65"))
                        lb41.place(x=250,y=400)
                    else:
                        n=data[0]
                        c=data[1]
                        a=data[2]
                        lb4111=Label(objct12,bg="yellow",fg="black",text="Customer Bank Account detail",font=("times new roman","35"))
                        lb4111.place(x=60,y=80)
                        lb411=Label(objct12,bg="black",fg="white",text="Name of Customer",font=("times new roman","25"))
                        lb411.place(x=100,y=200)
                        lb412=Label(objct12,bg="black",fg="white",text=n,font=("times new roman","25"))
                        lb412.place(x=400,y=200)
                        lb413=Label(objct12,bg="black",fg="white",text="Customer account no.",font=("times new roman","25"))
                        lb413.place(x=100,y=300)
                        lb414=Label(objct12,bg="black",fg="white",text=c,font=("times new roman","25"))
                        lb414.place(x=400,y=300)
                        lb415=Label(objct12,bg="black",fg="white",text="Customer Amount",font=("times new roman","25"))
                        lb415.place(x=100,y=400)
                        lb416=Label(objct12,bg="black",fg="white",text=a,font=("times new roman","25"))
                        lb416.place(x=400,y=400)
                            
                    
                
                def chk1():
                    objct1=Tk()
                    objct1.geometry("2000x900")
                    objct1.config(bg="PaleGreen1")
                    objct1.title("OK")
                    lb=Label(objct1,bg="yellow",fg="black",text="Enter here Customer'id and amount for Transfer",font=("times new roman","35"))
                    lb.place(x=150,y=50)

                    lab71=Label(objct1,bg="black",fg="white",text="Enter Customer_id To...  ",font=("times new roman","30"))
                    lab71.place(x=160,y=270)
                    a51=Entry(objct1,font=("times new roman","25"))
                    a51.place(x=600,y=270)

                    lab72=Label(objct1,bg="black",fg="white",text="Enter Customer_id To...  ",font=("times new roman","30"))
                    lab72.place(x=160,y=270)
                    a51=Entry(objct1,font=("times new roman","25"))
                    a51.place(x=600,y=270)
             
                    lab81=Label(objct1,bg="black",fg="white",text="Enter amount for send... ",font=("times new roman","30"))
                    lab81.place(x=160,y=330)
                    a61=Entry(objct1,font=("times new roman","25"))
                    a61.place(x=600,y=330)

                    def chck21():
                        cur=con.cursor()
                        customer=a51.get()##Receiver
                        customer_owner=a12.get()##Sender
                        #customer="123"
                        cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer,))
                        data=cur.fetchone()

                        cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer_owner,))
                        datas=cur.fetchone()

                        if not data:
                            lb41=Label(objct1,bg="black",fg="white",text="These Customer may not be present",font=("times new roman","65"))
                            lb41.place(x=250,y=400)
                        else:
                            k=data[2]##receiver amount
                            #m=int(a61.get())

                            l=datas[2]##sender amount
                            n=int(a61.get())##send amount
                            
                            objk=Tk()
                            objk.geometry("2000x900")
                            objk.config(bg="PaleGreen1")
                            objk.title("Finally WebPage")
                            lab81=Label(objk,bg="yellow",fg="black",text="Click here to Transfer the Amount",font=("times new roman","65"))
                            lab81.place(x=100,y=80)
                            def chck31():
                                lab81=Label(objk,bg="yellow",fg="black",text="Your Transfer the Amount is Successfull",font=("times new roman","35"))
                                lab81.place(x=250,y=450)
                                

                            bt12=Button(objk,bg="red",fg="white",text="transfer Amount",font=("times new roman","45"),command=chck31)
                            bt12.place(x=500,y=250)
                            
                            if l>=n:
                                cur=con.cursor()
                                amount=str(k+n)
                                amount1=str(l-n)
                                #cur.execute("update studenttable set Balance=%s where name=%s ",(amount,name))

                                cur.execute("update studenttable set Balance=%s where customer_id=%s ",(amount,a51.get()))
                                #con.commit()
                                cur.execute("update studenttable set Balance=%s where customer_id=%s ",(amount1,a12.get()))
                                con.commit()
                                #lab811=Label(objk,bg="yellow",fg="black",text="OK Successfull...........",font=("times new roman","65"))
                                #lab811.place(x=500,y=500)
                            else:
                                lab811=Label(objk,bg="PaleGreen1",fg="PaleGreen1",text="______________________________________________________",font=("times new roman","65"))
                                lab811.place(x=100,y=80)
                                lab8121=Label(objk,bg="yellow",fg="black",text="Your have not those enter amount in you account ..........",font=("times new roman","50"))
                                lab8121.place(x=50,y=254)

                            #def chck31():
                                #lab81=Label(objk,bg="yellow",fg="black",text="Hello",font=("times new roman","30"))
                                #lab81.place(x=160,y=700)
                                

                            #bt12=Button(objk,bg="red",fg="white",text="transfer Amount",font=("times new roman","45"),command=chck31)
                            #bt12.place(x=500,y=250)
                            
                            
                            
                            
                            

                    bt12=Button(objct1,bg="red",fg="white",text="Transfer",font=("times new roman","30"),command=chck21)
                    bt12.place(x=550,y=420)
                    
                    
                def check1():
                    
                    cur=con.cursor()
                    customer=a12.get()
                    #customer="123"
                    cur.execute("SELECT * FROM studenttable where customer_id=%s",(customer,))

                    data=cur.fetchone()
                    
                    if not data:
                        lb41=Label(objj,bg="red",fg="white",text="May Wrong username or customer'id",font=("times new roman","55"))
                        lb41.place(x=200,y=600)
                    else:
                        #.........................................
                        objct=Tk()
                        objct.geometry("2000x900")
                        objct.config(bg="PaleGreen1")
                        objct.title("Successfully Registered      ")
                        lbk=Label(objct,bg="yellow",fg="black",text="You Have Successfully Verified your Name and Customer_ID",font=("times new roman","40"))
                        lbk.place(x=50,y=100)
                        lbk1=Label(objct,bg="skyblue",fg="black",text="Please click here for Transfer data",font=("times new roman","30"))
                        lbk1.place(x=120,y=250)
                        bt11=Button(objct,bg="red",fg="white",text="Transfer",font=("times new roman","20"),command=chk1)
                        bt11.place(x=700,y=250)

                        lbk2=Label(objct,bg="skyblue",fg="black",text="Please click here for Account detail",font=("times new roman","30"))
                        lbk2.place(x=120,y=350)
                        bt12=Button(objct,bg="red",fg="white",text="Account",font=("times new roman","20"),command=chk11)
                        bt12.place(x=700,y=350)

                        lbk3=Label(objct,bg="skyblue",fg="black",text="Fill Application Form for Loan",font=("times new roman","30"))
                        lbk3.place(x=120,y=450)
                        bt13=Button(objct,bg="red",fg="white",text="Loan",font=("times new roman","20"),command=chk111)
                        bt13.place(x=700,y=450)
                        
                btn11=Button(objj,bg="blue",fg="white",text="Login",font=("times new roman","30"),command=check1)
                btn11.place(x=350,y=450)
                
                
                

            lb3=Label(obj1,bg="yellow",fg="black",text="If You Have Already your Bank Account",font=("times new roman","25"))
            lb3.place(x=350,y=300)
            btn=Button(obj1,bg="red",fg="white",text="Clicke Here",font=("times new roman","30"),command=login_bank)
            btn.place(x=350,y=350)

            lb4=Label(obj1,bg="yellow",fg="black",text="If You Want to Create Bank Account",font=("times new roman","25"))
            lb4.place(x=350,y=480)
            btn12=Button(obj1,bg="red",fg="white",text="Clicke Here",font=("times new roman","30"),command=createAccount)
            btn12.place(x=350,y=530)
        else:
            objl=Tk()
            objl.geometry("2000x900")
            objl.config(bg="PaleGreen1")
            lab3=Label(objl,bg="yellow",fg="black",text="Please Try Again You Password or username is Wrong",font=("times new roman","45"))
            lab3.place(x=150,y=50)
            objl.config(bg="red2")
            #def log():
                
                #lab3.destroy()
               # btn.destroy()
            btn=Button(objl,bg="green",fg="white",text="Click here to try again",font=("times new roman","35"),command=login)
            btn.place(x=550,y=350)
     
    btn1=Button(obj,bg="red",fg="white",text="Login",font=("times new roman","30"),command=mylogin)
    btn1.place(x=350,y=450)

btn=Button(t,bg="blue",fg="white",text="      SBI     ",font=("times new roman","25"),command=login)
btn.place(x=500,y=250)

btn=Button(t,bg="blue4",fg="white",text="     HDFC   ",font=("times new roman","25"),command=login)
btn.place(x=500,y=350)


btn=Button(t,bg="red",fg="white",text="     AXIS     ",font=("times new roman","25"),command=login)
btn.place(x=500,y=450)




