import datetime
class bank:
    bname="ASI Bank"
    branch="Sainagar"
    branch_code='420'
    ifsc='AAI000N420'
    tool_no=9390899287
    roi=7
    no_cost=0
    cust_deatils={}
    cust_transcations={}
    def __init__(self,name,age,email,phone,address,adhaar,pancard,dob,gender,pin,bal):
        self.cname=name
        self.age=age
        self.email=email
        self.phone=phone
        self.address=address
        self.adhaar=adhaar
        self.pancard=pancard
        self.dob=dob
        self.gender=gender
        self.pin=pin
        self.bal=bal
        self.no_cust_inc()
        self.account_no=100+self.no_cust
        self.concat_cust_details(self.account_no,self)

        @classmethod
        def no_cust_inc(cls):
            cls.no_cust+=1
        
        @classmethod
        def concat_cust_deatils(cls,acc_no,obj):
            cls.cust_details[acc_no]=obj

        @classmethod
        def change_ROI(cls):
            cls.roi=int(input("enter the ROI:"))
            print("ROI is changed")

        @classmethod
        def Check_Bal(cls):
            acc_no=int(input("enter the Account NO:"))
            pin=int(input("enter the Account Pin No:"))
            for i in cls.cust_details:
                res=cls.cust_details[i]
                if res.account_no==acc_no and res.pin==pin:
                    print(res.account_no,"balance is:",res.bal)
                    return
                
                else:
                    print("Invaild acc_no or")

        @classmethod
        def concat_cust_tran(cls,acc_no,data):
            if acc_no in cls.cust_transcations:
                cls.cust_transactions[acc_no]+=[data]
                print(acc_no,data)
            else:
                cls.cust_transcations[acc_no]=[data]
                print(acc_no.data)

        def deposit(self,count=0):
            if count==3:
                return
            amt=int(input("enter the Deposit amount:"))
            if amt>=50:
                self.bal+=amt
                self.success()
                self.conact_cust_tran(self.account_no,{'date':datetime.datetime.now(),'type':'deposit','amount':amt,'bal':self.bal})
                return
            else:
                print("amount should be minimum 50 rps")
                self.failed()
                return self.deposit(count+1)
        def withdraw(self,count=0):
            if count==3:
                return
            amt=int(input("enter the withdraw amount:"))
            if amt>=100 and self.bal>=amt:
                self.bal-=amt
                self.success()
                self.conact_cust_tran(self.account_no,{'date':datetime.datetime.now(),'type':'deposit','amount':amt,'bal':self.bal})
                self.success()
                return
            else:
                print("amount should be minimum 100 rps")
                self.failed()
                return self.withdraw(count+1)
        def mini_statement(self):
            print('Date'.center(25),'Type'.center(15),'Amount'.center(15),'Balance'.center(15),sep=' | ')
            print(80+'-')
            for i in self.cust_transactions[self.account_no]:
            print(str(i['date']).center(25),str(i['type']).center(15),str(i['amount']).center(15),str(i['bal'])center(15),sep=' | ')
            print(80*'-')
        
        def Check_bal(self):
            print("ypur current balance:",self.bal)

        def pin_change(self):
            old=int(input("enter the old pin:"))
            if self.pin==old:
                self.pin=int(input("enter the new pin:"))
                print("pin changed")
                self.success()
            else:
                self.failed()
        def cust_update(self):
            n=int(input("choose the option:\n1.Name\n2.Phone\n3.Email\n4.Address\n5.Exit"))
            match n:
                case 1:
                    self.cname=input("Enter the Name:")
                case 2:
                    self.phone=int(input("Enter the Phone:"))
                case 3:
                    self.email=int(input("Enter the Email"))
                case 4:
                    self.address=input("Enter the Address:")
                case _:
                    return
            return self.cust_update()
        
        def account_details(self):
            print("Account no:",self.account_no)
            print("Name:",self.cname)
            print("Age:",self.age)
            print("Email:",self.email)
            print("Phone:",self.phone)
            print("Balance:",self.bal)
            print("IFSC code:",self.ifsc)
            print("Pan:",self.pancard)
            print("Adhaar:",self.adhaar)
            print("Address:",self.address)
        
        def transfer(self):
            print("your current balance:",self.bal)
            acc_no=int(input("enter the Benificiary Accno:"))
            ifsc_code=input("enter the Benificiary IFSC:")
            if acc_no in self.cust_details and ifsc_code == self.cust_details[acc_no].ifsc:
                amt=int(input("Enter the Transfer Amount:"))
                if self.bal>=amt:
                    other=self.cust_details[acc_no]
                    other.bal+=amt
                    self.bal-+amt
                    self.concat_cust_tran(self.account_no,{'date':datetime.datetime.now(),'type':'Transfer(w)','amount':amt,'bal':self.bal})
                    self.concat_cust_tran(other.account_no,{'date':datetime.datetime.now(),'type':'Transfer(d)','amount':amt,'bal':other.bal})
                    self.success()
                    print("After transfer current balance",self.bal)
                    return
                else:
                    self.failed()
                    print("insufficient balance")
            else:
                print("invalid account number or Ifsc code")
            return
        
        @classmethod
        def home(cls,self):
            n=int(input("choose the option:\n0.AccountDetails\n1.Check Bal\n2.Deposit\N3.Withdraw\n4.Mini statement\n5.Update\n6.Pin change\n7.check ROI \n98.Transfer\9.Exit"))
            print("*"*150)
            match n:
                case 0:
                    self.account_details()
                case 1:
                    self.check_bal()
                case 2:
                    self.deposit()
                case 3:
                    self.withdraw()
                case 4:
                    self.mini_statement()
                case 5:
                    self.cust_update()
                case 6:
                    self.pin_change()
                case 7:
                    print("Today Rate Of Interest",self.roi)
                case 8:
                    self.transfer()
                case _:
                    return
            return cls.home(self)
        
        @staticmethod
        def success():
            print('|----------------|')
            print("Transaction is success|")
            print('|------------------|')
        
        @staticmethod
        def failed():
            print('|----------------|')
            print("Transaction is failed|")
            print('|------------------|')

    obj=bank('krishna'26,'krishna@gmail.com',9911776655,'hyd','987456321451','abcd826G1','1997-08-09','male',1234,500)
    obj1=bank('radha'26,'radha@gmail.com',9911776655,'hyd','987456321451','abcd826G1','1997-08-09','male',9876)

    def main(cls):
        acc_no=int(input("enetr the Account+_no:"))
        pin=int(input("enter the Pin_n0:"))
        if acc_no in cls.cust_details and cls.cust_details[acc_no].pin==pin:
            self=cls.cust_details[acc_no]
            cls.home(self)
        else:
            print("invaild account no or pin")
main(bank)