import pickle
import csv
# User Defined functions
def Laundary():
    f = open("Laundarypython.txt","w")                # Creating Laundary menu
    w = csv.writer(f)
    I= ['Sr.No',' item','Rate']
    w.writerow(I)
    s = [['1.' , '  Shirt  ' , ' 20 '],
           ['2.' , 'Jeans' , ' 30 '],
           ['3.' , ' Shorts' , ' 15 '],
           ['4.' , ' T-Shirt' , ' 15 ']]
    w.writerows(s)
    f.close()
def Restaurant():                                               # Creating Restaurant Menu
    f = open("Restaurantpython.txt", "w")
    w = csv.writer(f)
    t = ['Sr.No.',' Dishes',' Rate']
    s = [[' 1.' , 'Tea' , ' 50'],
         ['2.' , 'Coffee' , ' 60'],
         ['3.' , ' Breakfast' , ' 150'],
         ['4.' , 'Lunch' , ' 200'],
         ['5.' , 'Dinner' , ' 300']]
    w.writerow(t)
    w.writerrow(s)
def RoomAval_C():                           # for room typeC
    '''To give the room numbers for Room C'''
    fC = open("TypeC.txt","rb")
    DicC = {}
    DicC = pickle.load(fC)
    for i in DicC:
       if DicC[i] == 'a':
          r_no = i
          dicC= open("TypeC.txt", "wb")
          DicC[r_no] = 'u'
          pickle.dump(DicC,dicC)
          dicC.close()
          break
    return(r_no)
    fC.close()
    
def RoomAval_B():
    '''To give the room numbers for Room B'''  #for room type B
    fB = open("TypeB.txt", "rb")
    DicB = {}
    DicB = pickle.load(fB)
    for i in DicB:
      if DicB[i] == 'a':
         r_no = i
         dicB= open("TypeB.txt", "wb")
         DicB[r_no] = 'u'
         pickle.dump(DicB,dicB)
         dicB.close()
         break
    return(r_no)
    fB.close()
    
def RoomAval_A():
    '''To give the room numbers for Room A'''   #for room type A
    fA = open("TypeA.txt","rb")
    DictA = {}
    DictA= pickle.load(fA)
    for i in DictA:
      if DictA[i]=='a':
         r_no = i
         dictA= open("TypeA.txt", "wb")
         DictA[r_no]='u'
         pickle.dump(DictA,dictA)
         dictA.close()
         break
    return(r_no) 
    fA.close()
    
def Room():
    f1 = open("Room.txt","rb")
    No_Room = {}
    No_Room = pickle.load(f1)
    print("We have following rooms for you")
    print(" 1. Type A ----> 6000")
    print(" 2. Type B ----> 4000")
    print(" 3. Type C ----> 2000")
    r = int(input("enter your choice:"))
    q=int(input("enter the no. of rooms required:"))
    Ist = []
    if r == 1:
        if No_Room['A'] >= q:
            for i in range(q):
                r_no = RoomAval_A()
                Ist.append(r_no)
            F1 = open("Room.txt", "wb")
            No_Room['A'] = No_Room['A']-q     # Decreasing the number of rooms by number of rooms booked
            pickle.dump(No_Room, F1)
            F1.close()
        else:
         print("the no. of rooms you require are not available")
    elif r == 2:
       if No_Room['B'] >= q:
          for i in range(q):
            r_no = RoomAval_B()
            Ist.append(r_no)
          F1 = open("Room.txt", "wb")
          No_Room['B'] = No_Room['B']-q
          pickle.dump(No_Room, F1)
          F1.close()
       else:
          print("The no. of rooms you require are not available")
    elif r == 3:
        if No_Room['C'] >= q:
            for i in range(q):
            r_no = RoomAval_C()
            Ist.append(r_no)
            F1 = open("Room.txt", "wb")
            No_Room['C'] = No_Room['C']-q
          Pickle.dump(No_Room, F1)
          F1.close()
       else:
          print("The no. of rooms you require are not available")
          return(Ist,q)          # Returning list containing room numbers and number of rooms
def restaurant_file():
    '''opens the restaurant menu'''
    Restaurant()
    f = open("Restaurantpython.txt","r")
    s = f.read()
    print(s)
    f.close()
    
def Cdetails():
    '''To take the details for current booking'''
    name = input("enter your name:")
    p = int(input("enter your phone number:"))
    a = input("enter your address:")
    d = input("enter your date of check in :") 
    n = int(input("enter the no. days:"))
    R_no,Q= Room()
    if R_no[0] >= 101 and R_no[0] <= 125:
       pr=6000*Q*n
       typ = 'A'
    elif R_no[0] >= 126 and R_no[0] <= 150:
       pr = 4000*Q*n
       typ= 'B'
    elif R_no[0] >= 151 and R_no[0] <= 175:
       pr = 2000*Q*n        # calculating room rent
       typ = 'C'
    try:
       f2 = open("Customer_Details.txt","rb")
       Cust_Dat = []
       Cust_Dat = pickle.load(f2)
       Details = {}
       Details ['Name'] = name
       Details['phone_number'] = p
       Details['Address'] = a
       Details['Date_of_check_in'] = d
       Details['Roomrent'] = pr
       Details['Type_Room'] = typ
       Details['Room Nos'] = R_no
       Cust_Dat.append(Details)   # Entering data
       f3= open("Customer_Details.txt", "wb")
       pickle.dump(Cust_Dat,f3)
       f3.close()
       f2.close()
    except:
       f21 = open("Customer_Details.txt", "wb")
       Cust_Dat = []
       Details = {}
       Details ['Name'] = name
       Details['phone_number'] = p
       Details['Address'] = a
       Details['Date_of_check_in'] = d
       Details['Roomrent'] = pr
       Details['Type_Room'] = typ
       Details['Room Nos'] = R_no
       Cust_Dat.append(Details)
       pickle.dump(Cust_Dat,f21)
       f21.close() 
    return(R_no)

def restaurantbill():
    '''Caluates the restaurant bill'''
    restaurant_file()       # to open restaurant menu
    ch= int(input("enter your choice:"))
    if ch == 1:
       q = int(input("enter the quantity:"))
       p = q*50
       return(p)
    elif ch == 2: 
       q=int(input("enter the quantity:"))
       p = q*20
       return(p)
    elif ch == 3:
       q=int(input("enter the quantity:"))
       p = q*150
       return(p)
    elif ch == 4:
       q=int(input("enter the quantity:"))
       p = q*200
       return(p)
    elif ch == 5:
       q = int(input("enter the quantity:"))
       p=q*250
       return(p)
    else:
       print("wrong choice!")
    return(p)

def laundary_file():
    Laundary()
    fl = open("Laundarypython.txt", "r")
    ss=fl.read()
    print(ss)
def laundarybill():
    '''Calculates laundary bill'''
    laundary_file()        # to open Laundary menu
    ch= int(input("enter your choice:"))
    if ch == 1:
       q=int(input("enter the quantity:"))
       p = q*20
       return(p)
    elif ch == 2:
       q=int(input("enter the quantity:"))
       p = q*30
       return(p)
    elif ch == 3:
       q = int(input("enter the quantity:"))
       p = q*15
       return(p)
    elif ch == 4:
       q=int(input("enter the quantity:"))
       p=q*15
       return(p)
    else:
       print("wrong choice!") 
def Billing():
    '''Final Billing'''
    print('******** BILL ********')
    name = input("Enter your name:")
    f4= open("Customer_Details.txt","rb")
    Data = pickle.load(f4)
    for i in range (len(Data)):
       A = {}
       A = Data[i]
       if A['Name'] == name:
          k = A.keys()
          fR = open("Room.txt","rb")
          No_room = {}
          No_room = pickle.load(fR)
       if len(k) == 7:
          print("Name:", A['Name'])
          print("Phone number:", A['phone_number'])
          print("Address:", A['Address'])
          print("Date of check in:", A['Date_of_check_in'])
          print("Roomrent:", A['Roomrent'])
          Gst = 0.1*(A['Roomrent'])
          print("GST:", Gst)
          total_amount=A['Roomrent']+ Gst
          print("Total Amount:", total_amount)
          if A['Type_Room'] == 'A':
             No_room['A'] = No_room['A'] + len(A['Room Nos'])
             fn = open("TypeA.txt","rb")
             room_n = {}
             room_n = pickle.load(fn)
             for N in A['Room_Nos']:
               room_n[N] = 'a'    #changing room to Available
             fN = open("TypeA.txt", "wb")
             pickle.dump(room_n,fN)
             fn.close()
             fN.close()
          elif A['Type_Room'] == 'B':
             No_room['B'] = No_room['B'] + len (A['Room Nos'])
             fn = open("TypeB.txt","rb")
             room_n = {}
             room_n = pickle.load(fn)
             for N in A['Room Nos']:
               room_n[N]='a'
             fN = open("TypeB.txt", "wb")
             pickle.dump(room_n,fN)
             fn.close()
             fN.close()
          elif A['Type_Room'] == 'C':
             No_room['C'] = No_room['C'] + len(A['Room_Nos'])
             fn = open("TypeC.txt","rb")
             room_n = {}
             room_n = pickle.load(fn)
             for N in A['Room_Nos']:
                    room_n[N] = 'a'
             fN = open("TypeC.txt", "wb")
             pickle.dump(room_n,fN)
             fn.close()
             fN.close()
          elif len(k) == 8:
             for ab in k:
              if ab == 'Restaurant':
                  print("Name:", A['Name'])
                  print("Phone number:", A['phone_number'])
                  print("Address:", A['Address'])
                  print("Date of check in:", A['Date_of_check_in'])
                  print("Roomrent:", A['Roomrent'])
                  print("Restaurant price:", A['Restaurant'])
                  gst = 0.1*(A['Roomrent']+A['Restaurant'])
                  print("GST:", gst)
                  tot = gst+(A['Roomrent']+A['Restaurant'])
                  print("Total Cost:", tot)
              elif ab == 'Laundary':
                  print("Name:", A['Name'])
                  print("Phone number:", A['phone_number'])
                  print("Address:", A['Address'])
                  print("Date of check in:", A['Date_of_check_in'])
                  print("Roomrent:", A['Roomrent'])
                  print("Laundary price:", A['Laundary'])
                  gst = 0.1*(A['Roomrent']+A['Laundary'])
                  print("GST:", gst)
                  tot = gst + (A['Roomrent']+A['Laundary'])
                  print("Total Cost:", tot)
              if A['Type_Room'] == 'A':
                  No_room['A'] = No_room['A'] + len(A['Room_Nos'])
                  fn= open("TypeA.txt","rb")
                  room_n = {}
                  room_n = pickle.load(fn)
                  for N in A['Room_Nos']:
                         room_n[N] = 'a'
                  fN = open("TypeA.txt", "wb")
                  pickle.dump(room_n,fN)
                  fn.close()
                  fN.close()
              elif A['Type_Room'] == 'B':
                  No_room['B'] = No_room['B'] + len(A['Room Nos'])
                  fn= open("TypeB.txt","rb")
                  room_n = {}
                  room_n = pickle.load(fn)
                  for N in A['Room_Nos']:
                         room_n[N] = 'a'
                  fN = open("TypeB.txt", "wb")
                  pickle.dump(room_n,fN)
                  fn.close()
                  fN.close()
              elif A['Type_Room'] == 'C':
                  No_room['C'] = No_room['C'] + len(A['Room Nos']) # Increasing the room availability
                  fn = open("TypeC.txt","rb")
                  room_n = {}
                  room_n = pickle.load(fn)
                  for N in A['Room_Nos']:
                      room_n[N] = 'a'
                  fN= open("TypeC.txt", "wb")
                  pickle.dump(room_n,fN)
                  fn.close()
                  fN.close()
              elif len(k) == 9:
                  print("Name:", A['Name'])
                  print("Phone number:", A['phone_number'])
                  print("Address:", A['Address'])
                  print("Date of check in:", A['Date_of_check_in'])
                  print("Roomrent:", A['Roomrent'])
                  print("Restaurant price:", A['Restaurant'])
                  print("Laundary price:", A['Laundary'])
                  gst = 0.1*(A['Roomrent']+A['Laundary']+A['Restaurant'])
                  print("GST:", gst)
                  tot =gst+(A['Roomrent']+A['Restaurant']+A['Laundary'])
                  print("Total Cost:", tot)
                  if A['Type_Room'] == 'A':
                     No_room['A'] = No_room['A'] + len(A['Room Nos'])
                     fn= open("TypeA.txt","rb")
                     room_n = {}
                     room_n = pickle.load(fn)
                     for N in A['Room_Nos']:
                         room_n[N]='a'
                     fN= open("TypeA.txt", "wb")
                     pickle.dump(room_n,fN)
                     fn.close()
                     fN.close()
              elif A['Type_Room'] == 'B':
                     No_room['B'] = No_room['B'] + len (A['Room Nos'])
                     fn= open("TypeB.txt","rb")
                     room_n = {}
                     room_n = pickle.load(fn)
                     for N in A['Room_Nos']:
                       room_n[N] = 'a'
                     fN = open("TypeB.txt", "wb")
                     pickle.dump(room_n,fN)
                     fn.close()
                     fN.close()
              elif A['Type_Room'] == 'C':
                     No_room['C'] = No_room['C'] + len(A['Room Nos'])
                     fn = open("TypeC.txt","rb")
                     room_n = {}
                     room_n = pickle.load(fn)
                     for N in A['Room_Nos']:
                            room_n[N] = 'a'
                     fN = open("TypeC.txt", "wb")
                     pickle.dump(room_n,fN)
                     fn.close()
                     fN.close()
              fR1 = open("Room.txt", "wb")
              pickle.dump(No_room, fR1)
              fR.close()
              fR1.close()
              del Data[i]
              f4A = open("Customer_Details.txt", "wb")
              pickle.dump(Data,f4A)
              f4.close()
              fR.close()
#_main_
ans_while = 'y'
while ans_while == 'y':   #Using loop as long as user wants
  print(" !!! WELCOME TO TAJ HOTEL !!!")
  print("1. Booking ")
  print("2. Restaurant ")
  print("3. Laundary")
  print("4. Billing")
  print("5. Exit")
  choice = int(input("enter your choice:"))
  if choice == 1:
     R = Cdetails()
     print("Your Room Nos are")
     for b in R:
       print(b)
  elif choice == 2:
     Rest_pr = restaurantbill()
     f2A= open("Customer_Details.txt","rb")
     r_n=int(input("enter Room no:"))
     data = []
     back_data = {}
     data = pickle.load(f2A)
     for i in range(len(data)):
       a = {}
       a = data[i]
       for z in a['Room_Nos']: 
         if z == r_n:
           a['Restaurant'] = Rest_pr
           back_data = a
           del data[i]
           data.append(back_data)   #adding restaurant bill to customer data
           f3= open("Customer_Details.txt", "wb")
           pickle.dump(data,f3)
           f3.close()
     f2A.close()
  elif choice == 3:
     f2B = open("Customer_Details.txt","rb")
     datal = []
     datal = pickle.load(f2B)
     back_datal = {}
     L_P = laundarybill()
     r_n=int(input("enter the room no:"))
     for i in range(len(datal)):
       a = {}
       a = datal[i]
       for z in a['Room_Nos']:
         if 2 == r_n:
           a['Laundary'] = L_P
           back_dataL = a
           del datal[i]
           datal.append(back_dataL)
           F3B= open("Customer_Details.txt", "wb")
           pickle.dump(datal,F3B)
           F3B.close()  
     f2B.close()
  elif choice == 4:
         Billing()
         break
  elif choice == 5:
         break
         exit
  ans_while = input(" If you want to Continue press y else n:")
print("THANK YOU FOR CHOOSING TAJ HOTEL")
print("END")