print("**********WELCOME TO INDIAN BANK**********")

def take_data():
    acc_num = input("Enter account number:")
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
    cursor=mycon.cursor()
    quary="select account_number from user_data where account_number=%s"
    account_number=(acc_num,)
    cursor.execute(quary,account_number)
    data = cursor.fetchone()
    hk=len(acc_num)
    
    if data==None:
        print("-----------------------")
        if hk==12:   
          user_name = input("Enter your Name:")
          addr = input("Enter your Address:")
          phone_num = int(input("enter your phone number:"))
          aadhar_num = int(input("enter your aadhar number:"))
          am = int(input("enter ammount you want to deposit:")) 
          import mysql.connector as sqltor
          mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
          cursor=mycon.cursor()
          st="insert into user_data(account_number,name,address,phone_number,aadhar_number,amount) values('{}','{}','{}','{}','{}','{}')".format(acc_num,user_name,addr,phone_num,aadhar_num,am)
          cursor.execute(st)
          mycon.commit()
    

          print("------ACCOUNT CREATED------")
          print("****************************")
          return
        else:
            print("****please enter account number provided by bank****")
    else:
        print("****please enter account number provided by bank****")       
                

while True:

    ch = int(input("1.New Customer\n2.Existing customer\n3.close your account\n4.Exit the Site\nEnter your choice:"))

    if ch == 1:
        phone_num = int(input("enter your phone number:" ))
        print("your account number is deliver to your register phone number")
        take_data()

    elif ch == 2:
        
        acc_num = int(input("Enter your account number:"))
        import mysql.connector as sqltor
        mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
        cursor=mycon.cursor()
        quary="select account_number from user_data where account_number=%s"
        account_number=(acc_num,)
        cursor.execute(quary,account_number)
        data = cursor.fetchone()
        mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
        cursor=mycon.cursor()
        sql_quary="select amount from user_data where account_number=%s"
        account_number=(acc_num,)
        cursor.execute(sql_quary,account_number)
        BALANCE = cursor.fetchone()
        sql_quar="select name from user_data where account_number=%s"
        account_number=(acc_num,)
        cursor.execute(sql_quar,account_number)
        use = cursor.fetchone()
        if data==None:
            print("*****account not found*****")
        else:
            import functools
            res=functools.reduce(lambda sub,ele: sub*10 + ele,data)
            val=int(res)
            ab=functools.reduce(lambda sub,ele: sub*10 + ele,BALANCE)
            abc=int(ab)
            ps=functools.reduce(lambda sub,ele: sub*10 + ele,use)
            ahr=str(ps)
        
            if acc_num==val:
               print(" ******Account Found******")
               print("welcome",ahr)
            
               while True:
                   op = int(input("1.#Check your Balance\n2.#Withdraw Amount\n3.#Deposite Amount\n4.#Back to Main Menu\nEnter your choice:"))
                   if op == 1:
                       print("------AVAILABLE BALANCE IS:",abc)
                    
                   elif op == 2:
                      amt = int(input("Enter amount you want to withdraw:"))
                      new_amt = abc-amt
                      bcd = new_amt
                      print("Withdraw Successful")
                      print("------Account Balance:",bcd)
                    
                      mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
                      cursor=mycon.cursor()
                      st="""update user_data set amount=%s where account_number=%s"""
                      amount=bcd
                      account_number=val
                      inp=(amount,account_number)
                      cursor.execute(st,inp)
                      mycon.commit()
                      break
                    
                   elif op == 3:
                       amt = int(input("Enter amount you want to Deposite:"))
                       new_amt = abc+amt
                       cd = new_amt
                       print("Deposited Successful")
                       print("------Account Balance:",cd)
                    
                       mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
                       cursor=mycon.cursor()
                       st="""update user_data set amount=%s where account_number=%s"""
                       amount=cd
                       account_number=val
                       inp=(amount,account_number)
                       cursor.execute(st,inp)
                       mycon.commit()
                       break
                   elif op == 4:
                       break
                       print("--------------------------------------------")    
                    
                   else :
                        print("*******Please enter valid choice*******")
        
    
    elif ch == 3:
        acc_num = int(input("Enter your account number:"))
        import mysql.connector as sqltor
        mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
        cursor=mycon.cursor()
        quary="select account_number from user_data where account_number=%s"
        account_number=(acc_num,)
        cursor.execute(quary,account_number)
        data = cursor.fetchone()
        if data==None:
            print("*******Account not found*******")
            break
        else:
            import functools
            res=functools.reduce(lambda sub,ele: sub*10 + ele,data)
            val=int(res)
        
            if acc_num==val:
                print("******Your Account is closed successfully******")
                print("-----------------------------------")
                while True:
                 import mysql.connector as sqltor
                 mycon = sqltor.connect(host="localhost",user="root",passwd="root",database="bank")
                 cursor=mycon.cursor()
                 st="delete from user_data where account_number=%s"
                 account_number=(acc_num,)
                 cursor.execute(st,account_number)
                 dat = cursor.fetchone()
                 mycon.commit()
                 break
      
    elif ch == 4:
        print("*********Thanks for using our Bank, Please visit Again**********")
        break

    else :
        print("*******please enter valid choice*******")