import pymysql
vvvv=input("Please enter your SQL server username:")
uuuu=input("Please enter your SQL server password:")
conn=pymysql.connect(host="localhost",user=vvvv,password=uuuu,database="PROJECT")
cursor=conn.cursor()
print("--------------------------------------------------------------------------------")
print("Program Begins")
print("Hi there!!") 
cursor.execute("SELECT * FROM LOGIN ;")
L=[]
M=list(cursor.fetchall())
def abcd():
      koi=input("Please enter username:")
      zab=44
      ccccc=1
      while zab==44:
          for x in M:
                     if koi==x[1]:
                         while ccccc==1:
                             zz=input("Please enter password:")
                             if zz==x[2]:
                                 print("Welcome",x[1])
                                 print("You have logined as ",x[3])
                                 global aah
                                 aah=x[3]
                                 ccccc=2
                                 
                             else:
                                 print("Wrong password.Please try again!")
          zab=2                      
      if ccccc==1:
          print("No such username exists")
          yyyy=input("Press 1 to try again\nPress 2 to exit")
          if yyyy==2:
              conn.close()
          else:
              koi=yyyy
              abcd()
abcd()
        
    
def cust():
      cursor.execute("SELECT * FROM Customer ;")
      M=cursor.fetchall()
      for x in M:
           print(list(x))
      poi="INSERT INTO CUSTOMER(Cust_Id,Cust_Name,Age_18_Above,Cust_Mobile,Cust_Email,Identification_Document) VALUES(%s,%s,%s,%s,%s,%s)"
      VA=input("Cust_Id:")
      VAL=input("Cust_Name:")
      valu=input("Age_18_Above:")
      vv=input("Cust_Mobile:")
      vvv=input("Cust_Email:")
      vvvv=input("Identification_Document:")
      value=(VA,VAL,valu,vv,vvv,vvvv)
      
     
      cursor.execute(poi,value)
      conn.commit()
      print("Added")
def owner():
   while True:
       print("What operation do you want to perform\n Press 1 View employee details\n Press 2 Delete an employee record\n Press 3 Add Employee\n Press 4 Add Customer\n Press 5 Delete Customer\n Press 6 View Customer details\n Press 7 For booking\n Press 8 Generate bill\n Press 9 Add Room\nPress 10 Delete Room")
       pl=int(input("-->"))
       if pl==1:
           cursor.execute("SELECT * FROM Employee ;")
           M=cursor.fetchall()
           for x in M:
                print(list(x))
       if pl==2:
           cursor.execute("SELECT * FROM Employee ;")
           M=cursor.fetchall()
           for x in M:
                print("[",x[1],"]",end="\n")
         
           poi=input("Employee name:")
           h="DELETE FROM EMPLOYEE WHERE E_NAME=%s"
           adr=(poi,)
           
           cursor.execute(h,adr)
           print("Deleted")
       if pl==3:
           poi="INSERT INTO EMPLOYEE(E_Id,E_NAME,SALARY) VALUES(%s,%s,%s)"
           VA=input("E_Id:")
           VAL=input("E_NAME:")
           valu=input("Salary:")
           value=(VA,VAL,valu)
           cursor.execute(poi,value)
           conn.commit()
           print("Added")
       if pl==4:
                 cursor.execute("SELECT * FROM Customer ;")
                 M=cursor.fetchall()
                 for x in M:
                       print(list(x))
                 poi="INSERT INTO CUSTOMER(Cust_Id,Cust_Name,Age_18_Above,Cust_Mobile,Cust_Email,Identification_Document) VALUES(%s,%s,%s,%s,%s,%s)"
                 VA=input("Cust_Id:")
                 VAL=input("Cust_Name:")
                 valu=input("Age_18_Above:")
                 vv=input("Cust_Mobile:")
                 vvv=input("Cust_Email:")
                 vvvv=input("Identification_Document:")
                 value=(VA,VAL,valu,vv,vvv,vvvv)
                 
                 cursor.execute(poi,value)
                 conn.commit()
                 print("Added")
       if pl==5:
           cursor.execute("SELECT * FROM Customer ;")
           M=cursor.fetchall()
           for x in M:
                print("[",x[1],"]","[",x[0],"]",end="\n")
         
           poi=input("Customer name:")
           ccopo=input("Customer_Id:")
           h="DELETE FROM Customer WHERE Cust_Name=%s AND Cust_Id=%s"
           adr=(poi,ccopo)
           
           cursor.execute(h,adr)
           print("Deleted")
           conn.commit()
       if pl==6:
           cursor.execute("SELECT * FROM Customer ;")
           M=cursor.fetchall()
           for x in M:
                print(list(x))
       if pl==7:
             ppppp=input("Have you been here before?(Can we find your previous record?):(y/n)-->")
             if ppppp.upper()=="N":
                  cursor.execute("SELECT * FROM Customer ;")
                  M=cursor.fetchall()
                  for x in M:
                       print(list(x))
                  poi="INSERT INTO CUSTOMER(Cust_Id,Cust_Name,Age_18_Above,Cust_Mobile,Cust_Email,Identification_Document) VALUES(%s,%s,%s,%s,%s,%s)"
                  VA=input("Cust_Id:")
                  VAL=input("Cust_Name:")
                  valu=input("Age_18_Above:")
                  vv=input("Cust_Mobile:")
                  vvv=input("Cust_Email:")
                  vvvv=input("Identification_Document:")
                  value=(VA,VAL,valu,vv,vvv,vvvv)
                  
                 
                  cursor.execute(poi,value)
                  conn.commit()
                  print("Added")
                   

                  cz=1
                  while cz==1:
                        napss=input("Start_Date(Write in YYYY-MM-DD Format)")
                        napsss=input("End Date(Write in YYYY-MM-DD Format)")
                        if napss<napsss:
                              cz=2
                              break
                        else:
                              print("The dates youn have entered are not logically possible.Please try again!")


                  
                  print("                             BOOKING TABLE")

                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))

                  napssss=input("Booking Id")
                  print("                             ROOM TABLE")
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                        print(list(nan))     
                  naps=input("Room Id:")
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,napssss)
                  OOM=cursor.fetchall()
                  for nanI in OOM:
                        print(nani)

                  baby=(naps,napss,napsss,napssss,VA)
                  xxx="INSERT INTO Booking VALUES(%s,%s,%s,%s,%s)";
                   
                  cursor.execute(xxx,baby)
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                       print(list(nani))
                  conn.commit()
                  print("Booking done!")
                   
             

             if ppppp.upper()=="Y":
                  cz=1
                  while cz==1:
                        napss=input("Start_Date(Write in YYYY-MM-DD Format)")
                        napsss=input("End Date(Write in YYYY-MM-DD Format)")
                        if napss<napsss:
                              cz=2
                              break
                        else:
                              print("The dates youn have entered are not logically possible.Please try again!")
                  print("                             BOOKING TABLE")

                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))

                  napssss=input("Booking Id")
                  print("                             ROOM TABLE")
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                        print(list(nan))     
                  naps=input("Room Id:")
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,napssss)
                  OOM=cursor.fetchall()
                  for nanI in OOM:
                        print(nani)
                  cursor.execute("SELECT * FROM Customer ;")
                  M=cursor.fetchall()
                  for x in M:
                       print(list(x))

                  VA=input("Cust_Id:")
                  
                  baby=(naps,napss,napsss,napssss,VA)
                  xxx="INSERT INTO Booking VALUES(%s,%s,%s,%s,%s)";
                   
                  cursor.execute(xxx,baby)
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                       print(list(nani))
                  conn.commit()
                  print("Booking done!")


       if pl==8:
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))
             
                  yuo=input("Booking Id:")
                  iopl="SELECT DATEDIFF(%s,%s)"
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,yuo)
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        MK=list(nani)
                  #print(MK)
                  L123=MK[1]
                  L456=MK[2]
                  van=(L123,L456)
                  nnnnnn=cursor.execute(iopl,van)
                  #print(nnnnnn+2)
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                          if nan[0]==MK[0]:
                                SP=nan[2]
                  cursor.execute("SELECT * FROM CUSTOMER;")
                  ANDY=cursor.fetchall()
                  for anna in ANDY:
                          if anna[0]==MK[4]:
                                ABCDEFGHIJ=anna[1]
                                qwerty=anna[2]
                                ASSSO=anna[3]
                                abcandance=anna[4]
                                ILoveAGirl=anna[5]
                  #print(SP)
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLL       LLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBBBBBBBBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLLLLLLL  LLLLLLLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLLLLLLL  LLLLLLLL")
                  print("")
                  print("")
                  print("")
                  print("NAME:",ABCDEFGHIJ)
                  print("")
                  print("Is age above 18:",qwerty)
                  print("")
                  print("Customer Mobile:",ASSSO)
                  print("")
                  print("Customer Email:",abcandance)
                  print("")
                  print("Check-IN:",L123)
                  print("")
                  print("Check-Out:",L456)
                  print("")
                  print("")
                  print("")
                  Totalbill=print("           Your total bill:",SP*(nnnnnn+2))
                  GST=print("           After applying GST your final bill is:",(SP*(nnnnnn+2))*(118/100))
                  print("                    THANK YOU PLEASE COME AGAIN")
                              
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
       if pl==9:           
                 cursor.execute("SELECT * FROM ROOM ;")
                 M=cursor.fetchall()
                 for x in M:
                       print(list(x))
                 poi="INSERT INTO ROOM(ROOM_ID,ROOM_TYPE,RENT,AC,FRIDGE,No_of_beds,GEYSER) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                 VA=input("Room_Id:")
                 VAL=input("Room type:")
                 valu=input("Rent:")
                 vv=input("AC:")
                 vvv=input("Fridge:")
                 vvvv=input("Number of beds:")
                 vax=input("Geyser:")
                 value=(VA,VAL,valu,vv,vvv,vvvv,vax)
                 
                 cursor.execute(poi,value)
                 conn.commit()
                 print("Added")
       if pl==10:
           cursor.execute("SELECT * FROM ROOM ;")
           M=cursor.fetchall()
           for x in M:
                print("[",x[1],"]","[",x[0],"]",end="\n")
         
           poi=input("Room name:")
           ccopo=input("Room_Id:")
           h="DELETE FROM ROOM WHERE ROOM_TYPE=%s AND ROOM_ID=%s"
           adr=(poi,ccopo)
           
           cursor.execute(h,adr)
           print("Deleted")
           conn.commit()
                 

                              
                   

       OOO=input("Do you want to continue:(y/n)")
       if OOO=="Y" or OOO=="y":
              continue
       if OOO=="N" or OOO=="n":
              return

def Employee():
     while True:
       print("What operation do you want to perform\n Press 1 to add Customer\n Press 2 to delete Customer\n Press 3 to show Customer details\n Press 4 to generate bill\n Press 5 to do booking")
       pl=int(input("-->"))

       if pl==1:
           poi="INSERT INTO CUSTOMER(Cust_Id,Cust_Name,Age_18_Above,Cust_Mobile,Cust_Email,Identification_Document) VALUES(%s,%s,%s,%s,%s,%s)"
           VA=input("Cust_Id:")
           VAL=input("Cust_Name:")
           valu=input("Age_18_Above:")
           vv=input("Cust_Mobile:")
           vvv=input("Cust_Email:")
           vvvv=input("Identification_Document:")
           value=(VA,VAL,valu,vv,vvv,vvvv)
           
           cursor.execute(poi,value)
           conn.commit()
           print("Added")
       if pl==2:
           cursor.execute("SELECT * FROM Customer ;")
           M=cursor.fetchall()
           for x in M:
                print("[",x[1],"]",end="\n")
         
           poi=input("Customer name:")
           h="DELETE FROM Customer WHERE Cust_Name=%s"
           adr=(poi,)
           
           cursor.execute(h,adr)
           print("Deleted")
           conn.commit()
       if pl==3:
           cursor.execute("SELECT * FROM Customer ;")
           M=cursor.fetchall()
           for x in M:
                print(list(x))
       if pl==4:
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))
             
                  yuo=input("Booking Id:")
                  iopl="SELECT DATEDIFF(%s,%s)"
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,yuo)
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        MK=list(nani)
                  #print(MK)
                  L123=MK[1]
                  L456=MK[2]
                  van=(L123,L456)
                  nnnnnn=cursor.execute(iopl,van)
                  #print(nnnnnn+2)
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                          if nan[0]==MK[0]:
                                SP=nan[2]
                  cursor.execute("SELECT * FROM CUSTOMER;")
                  ANDY=cursor.fetchall()
                  for anna in ANDY:
                          if anna[0]==MK[4]:
                                ABCDEFGHIJ=anna[1]
                                qwerty=anna[2]
                                ASSSO=anna[3]
                                abcandance=anna[4]
                                ILoveAGirl=anna[5]
                  #print(SP)
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLL       LLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBBBBBBBBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBB    BBB       III        LLL       LLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLLLLLLL  LLLLLLLL")
                  print("          BBBBBBBBBB   IIIIIIIIIII    LLLLLLLL  LLLLLLLL")
                  print("")
                  print("")
                  print("")
                  print("NAME:",ABCDEFGHIJ)
                  print("")
                  print("Is age above 18:",qwerty)
                  print("")
                  print("Customer Mobile:",ASSSO)
                  print("")
                  print("Customer Email:",abcandance)
                  print("")
                  print("Check-IN:",L123)
                  print("")
                  print("Check-Out:",L456)
                  print("")
                  Totalbill=print("           Your total bill:",SP*(nnnnnn+2))
                  GST=print("           After applying GST your final bill is:",(SP*(nnnnnn+2))*(118/100))
                  print("                    THANK YOU PLEASE COME AGAIN")
                              
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")
                  print("")

             
       if pl==5:
             ppppp=input("Have you been here before?(Can we find your previous record?):(y/n)-->")
             if ppppp.upper()=="N":
                  cursor.execute("SELECT * FROM Customer ;")
                  M=cursor.fetchall()
                  for x in M:
                       print(list(x))
                  poi="INSERT INTO CUSTOMER(Cust_Id,Cust_Name,Age_18_Above,Cust_Mobile,Cust_Email,Identification_Document) VALUES(%s,%s,%s,%s,%s,%s)"
                  VA=input("Cust_Id:")
                  VAL=input("Cust_Name:")
                  valu=input("Age_18_Above:")
                  vv=input("Cust_Mobile:")
                  vvv=input("Cust_Email:")
                  vvvv=input("Identification_Document:")
                  value=(VA,VAL,valu,vv,vvv,vvvv)
                  
                 
                  cursor.execute(poi,value)
                  conn.commit()
                  print("Added")
                   
       

                  cz=1
                  while cz==1:
                        napss=input("Start_Date(Write in YYYY-MM-DD Format)")
                        napsss=input("End Date(Write in YYYY-MM-DD Format)")
                        if napss<napsss:
                              cz=2
                              break
                        else:
                              print("The dates youn have entered are not logically possible.Please try again!")


                  
                  print("                             BOOKING TABLE")

                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))

                  napssss=input("Booking Id")
                  print("                             ROOM TABLE")
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                        print(list(nan))     
                  naps=input("Room Id:")
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,napssss)
                  OOM=cursor.fetchall()
                  for nanI in OOM:
                        print(nani)

                  baby=(naps,napss,napsss,napssss,VA)
                  xxx="INSERT INTO Booking VALUES(%s,%s,%s,%s,%s)";
                   
                  cursor.execute(xxx,baby)
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                       print(list(nani))
                  conn.commit()
                  print("Booking done!")
                   
             

             if ppppp.upper()=="Y":
                  cz=1
                  while cz==1:
                        napss=input("Start_Date(Write in YYYY-MM-DD Format)")
                        napsss=input("End Date(Write in YYYY-MM-DD Format)")
                        if napss<napsss:
                              cz=2
                              break
                        else:
                              print("The dates youn have entered are not logically possible.Please try again!")
                  print("                             BOOKING TABLE")

                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                        print(list(nani))

                  napssss=input("Booking Id")
                  print("                             ROOM TABLE")
                  cursor.execute("SELECT * FROM ROOM;")
                  ABCDEFG=cursor.fetchall()
                  for nan in ABCDEFG:
                        print(list(nan))     
                  naps=input("Room Id:")
                  donkey=("SELECT * FROM BOOKING WHERE BOOKING_ID=%s")
                  cursor.execute(donkey,napssss)
                  OOM=cursor.fetchall()
                  for nanI in OOM:
                        print(nani)
                  cursor.execute("SELECT * FROM Customer ;")
                  M=cursor.fetchall()
                  for x in M:
                       print(list(x))

                  VA=input("Cust_Id:")
                  
                  baby=(naps,napss,napsss,napssss,VA)
                  xxx="INSERT INTO Booking VALUES(%s,%s,%s,%s,%s)";
                   
                  cursor.execute(xxx,baby)
                  print("                             BOOKING TABLE")
                  cursor.execute("SELECT * FROM BOOKING;")
                  cccgf=cursor.fetchall()
                  for nani in cccgf:
                       print(list(nani))
                  conn.commit()
                  print("Booking done!")


       if pl==10:
               cursor.execute("SELECT * FROM ROOM ;")
               M=cursor.fetchall()
               for x in M:
                    print("[",x[1],"]","[",x[0],"]",end="\n")
             
               poi=input("Room name:")
               ccopo=input("Room_Id:")
               h="DELETE FROM ROOM WHERE ROOM_TYPE=%s AND ROOM_ID=%s"
               adr=(poi,ccopo)
               
               cursor.execute(h,adr)
               print("Deleted")
               conn.commit()
                 
             
       OOO=input("Do you want to continue:(y/n)")
       if OOO=="Y" or OOO=="y":
            continue
       else:
            break
 


if aah=="ADMIN":
        owner()
if aah=="EMPLOYEE":
        Employee()
conn.commit()
conn.close()  





