a=[] 
b=[] 
c=[] 
d=[] 
e=[] 
f=[] 
g=[] 
h=[] 
y=[] 
S=[] 
T=[] 
U=[] 
V=[] 
S1=0 
S2=0 
print(""" 
 
        .............................................................
              /////////////////////////////////////////
              ..........WELCOME TO THIS KAILASH HOTEL...........
         ///////////////////MADE BY HARSH GOYAL///////////////////// 
              <<<<<<<<<<<<IMS ENGINEERING COLLEGE>>>>>>>>>>>>>>
     .................................................................
 
""") 
 
while(True): 
     print(""" 
             1--->Enter Customer Details 
             2--->Calculate Room Rent 
             3--->Calculate Restaurant Bill 
             4--->Calculate Gaming Bill 
             5--->Calculate Laundry Bill 
             6--->Customer Details             
             7--->EXIT 
      
    """) 
     print() 
     k=int(input("Enter Choice: ")) 
     if k==1: 
         l=input("Enter the Customer Name: ") 
         m=input("Enter the Customer Address: ") 
         A=input("Enter the Customer Age: ") 
         B=input("Enter the Customer Nationality: ") 
         C=input("Enter the Customer Phone Number: ") 
         D=input("Enter the Customer E-Mail address: ") 
         n=input("Enter the Customer CheckIN Date: ") 
         o=input("Enter the Customer CheckOUT Date: ") 
         p=int(input("Enter The Customer Room no : ")) 
         a.append(l) 
         b.append(m) 
         c.append(n) 
         d.append(o) 
         e.append(p) 
         S.append(A) 
         T.append(B) 
         U.append(C) 
         V.append(D) 
          
     elif k==2: 
         print ("We have the following rooms for you:-") 
 
         print ("1.  Ultra Royal ----> 10000 INR ") 
 
         print ("2.  Royal ----------> 5000 INR ") 
 
         print ("3.  Elite ----------> 3500 INR ") 
 
         print ("4.  Budget ---------> 2500 INR ") 
          
         q=int(input("Enter the Room Type: ")) 
         r=int(input("Enter the No. of Nights: ")) 
         if q==1: 
             print("\nUltra Royal Room Rent") 
             f.append(10000*r) 
         elif q==2: 
             print("\nRoyal Room Rent") 
             f.append(5000*r) 
         elif q==3: 
             print("\nElite Room Rent") 
             f.append(3500*r) 
         elif q==4: 
             print("\nBudget Room Rent") 
             f.append(2500*r) 
         else: 
             print("\nInvalid Option") 
     elif k==3: 
         print(""" 1.  Vegetarian Combo -----> 300 INR   
 2.  Non-Vegetarian Combo -----> 500 INR
 3.  Vegetarian & Non-Vegetarian Combo -----> 750 INR
         """) 
         s=int(input("\nEnter The Choice: ")) 
         if s==1: 
             t=int(input("\nEnter The Quantity: ")) 
             g.append(300*t) 
         elif s==2: 
             t=int(input("\nEnter The Quantity: ")) 
             g.append(500*t) 
         elif s==3: 
             t=int(input("\nEnter The Quantity: ")) 
             g.append(750*t) 
         else: 
             print("\nInavalid Option ") 
     elif k==4: 
         while(1): 
             print(""" 1.  Table Tennis -----> 150 INR/HR 
 2.  Bowling -----> 100 INR/HR 
 3.  Snooker -----> 250 INR/HR 
 4.  PUBG World Gaming -----> 400 INR/HR 
 5.  Video Games -----> 300 INR/HR 
 6.  Swimming Pool Games ----->     350 INR/HR 
 7.  Exit 
 """) 
             u=int(input("\nEnter The Choice: ")) 
             if u==1: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(150*v) 
             elif u==2: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(100*v) 
             elif u==3: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(250*v) 
             elif u==4: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(400*v) 
             elif u==5: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(300*v) 
             elif u==6: 
                 v=int(input("\nEnter No. of Hours : ")) 
                 S1+=(350*v) 
             elif u==7: 
                 h.append(S1) 
                 break; 
             else: 
                 print("\nInvalid Option") 
     elif k==5: 
         while(1): 
             print(""" 1.  Shirts -----> 500 INR 
 2.  T-Shirts -----> 300 INR
 3.  Pants -----> 200 INR 
 4.  Jeans -----> 400 INR
 5.  Sarees -----> 500 INR
 6.  Chudithar -----> 300 INR 
 7.  Frock -----> 300 INR
 8.  Skirts -----> 400 INR
 9.  Trousers -----> 200 INR 
 10.  InnerWear -----> 300 INR
 11.  Exit 
 """) 
             w=int(input("\nEnter the Choice: ")) 
             if w==1: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(5*x) 
             elif w==2: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(3*x) 
             elif w==3: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(2*x) 
             elif w==4: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(4*x) 
             elif w==5: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(5*x) 
             elif w==6: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(3*x) 
             elif w==7: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(3*x) 
             elif w==8: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(4*x) 
             elif w==9: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(2*x) 
             elif w==10: 
                 x=int(input("\nEnter the Quantity: ")) 
                 S2+=(3*x) 
             elif w==11: 
                 y.append(S2) 
                 break; 
             else: 
                 print("\nInvalid Option ") 
     elif k==6: 
         z=input("Enter name of Customer: ") 
         for i in range(len(a)): 
             if z==a[i]: 
                 print("\n\n**## CUSTOMER DETAILS ##**") 
                 print("\n\t CUSTOMER NAME: ",a[i]) 
                 print("\n\t CUSTOMER ADDRESS: ",b[i]) 
                 print("\n\t CUSTOMER AGE: ",S[i]) 
                 print("\n\t CUSTOMER NATIONALITY: ",T[i]) 
                 print("\n\t CUSTOMER PHONE NUMBER: ",U[i]) 
                 print("\n\t CUSTOMER E-MAIL ADDRESS: ",V[i]) 
                 print("\n\t CUSTOMER CHECK IN DATE: ",c[i]) 
                 print("\n\t CUSTOMER CHECK OUT DATE: ",d[i]) 
                 print("\n\t CUSTOMER ROOM.NO: ",e[i]) 
                 print("\n\t CUSTOMER ROOM RENT: ",f[i]," INR") 
                 print("\n\t CUSTOMER RESTAURENT BILL: ",g[i]," INR") 
                 print("\n\t CUSTOMER GAMING BILL: ",h[i]," INR") 
                 print("\n\t CUSTOMER LAUNDRY BILL: ",y[i]," INR") 
                  
                 print("\n\t CUSTOMER TOTAL BILL: ",(f[i]+g[i]+h[i]+y[i])," INR") 
                 print("\n\t CUSTOMER ADDIIONAL CHARGES: ",((f[i]+g[i]+h[i]+y[i])/4)," INR") 
                  
                 print("\n\n\t CUSTOMER GRAND TOTAL: ",(f[i]+g[i]+h[i]+y[i])+((f[i]+g[i]+h[i]+y[i])/4)," INR") 
 
     elif k==7: 
         print("\n\n\t THANK YOU !! VISIT KAILASH HOTEL AGAIN ") 
         break; 
 
                                                        
                                                                     
 
                                                       
