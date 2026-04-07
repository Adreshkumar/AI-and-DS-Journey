import json
import random
import string
from pathlib import Path
from datetime import datetime

class Bank:
    Database = 'Bank User Data.json'
    dummy_data = []
    try:
        if Path(Database).exists():
            with open(Database, 'r') as f:
                dummy_data = json.loads(f.read())
        else:
            print("This File Doesn't Exist")
    except Exception as err:
        print(f"An Exception occured as {err}")
    @staticmethod
    def __update():
        with open(Bank.Database,"w") as f:
            f.write(json.dumps(Bank.dummy_data))

    @staticmethod
    def __accountno_gen():
        alpha = random.choices(string.ascii_letters,k = 5)
        num = random.choices(string.digits,k = 5)
        special = random.choices("@#$&!%",k = 2)
        id = [alpha ,num ,special]
        random.shuffle(id)
        return "".join("".join(g) for g in id)
    
    @staticmethod
    def __pub_accountnogen():
            num = random.choices(string.digits, k = 12)
            random.shuffle(num)
            join_num = "".join(num) 
            return (int(join_num))
    def create_account(self):
        user_data = {
            "first name": input("Whats Your first Name :-"),
            "last name" : input("Enter Your last Name :-"),
            "surname" : input("Enter Your Surname :-"),
            "age" : int(input("Whats your age :-")),
            "gender" : input("Whats your gender :-"),
            "phone number" : int(input("Whats Your Phone Number :-")),
            "email" : input("Whats your email :-"),
            "pin" : int(input("Create your pin must be 4 numbers :-")),
            "account.no" : Bank.__accountno_gen(),
            "public id" : Bank.__pub_accountnogen(),
            "balance" : 0
        }

        if user_data["age"]<18 or len(str(user_data["pin"])) != 4 or "@" not in user_data["email"] or "." not in user_data["email"]:
            print("Sorry You can't Create an Account")
        else:
            print("Thankyou for creating an account")
            for i in user_data:
                print(f"{i}: {user_data[i]}")
            print("Please note down your Account.No and Pin")
            
            Bank.dummy_data.append(user_data)
            Bank.__update()
    def Deposit_money(self):
        depodetail = input("Type Your account Number :-")
        acc_pin = int(input("Type Your Pin"))
        print("! Never Share Your PIN with Anyone")

        newdata = [i for i in Bank.dummy_data if i["account.no"] == depodetail and i["pin"] == acc_pin]

        if len(newdata) == 0:
            print("Invalid Information")
        else:
            money = int(input("Enter Amount you want to Desposit"))
            if money <= 0:
                print("Please put the correct Amount")
            else:
                newdata [0] ["balance"] += money
                Bank.__update()
                print(f"Deposit Successful \nAmount Deposited {money} \nNew Balance {newdata[0]["balance"]} \n{Bank.__nowdatetime()}")

    def Withdraw_money(self):
        depodetail = input("Type Your account Number :-")
        acc_pin = int(input("Type Your Pin"))
        print("! Never Share Your PIN with Anyone")

        newdata = [i for i in Bank.dummy_data if i["account.no"] == depodetail and i["pin"] == acc_pin]

        if len(newdata) == 0:
            print("Invalid Information")
        else:
            money = int(input("Enter Amount you want to Withdraw"))
            if money <= 0 or money > newdata [0]["balance"] or money > 25000:
                print("Please put the correct Amount")
            else:
                newdata [0] ["balance"] -= money
                Bank.__update()
                print(f"Withdraw Successful \nAmount Withdrawn {money} \nRemaining Balance {newdata[0]["balance"]} \n{Bank.__nowdatetime()}")
    @staticmethod
    def __nowdatetime():
        now = datetime.now()
        return(now.strftime("Time: %I:%M:%S %p \nDate: %d %b,%Y "))
    
    def Send_money(self):
        print("First Login your account")
        depodetail = input("Type Your account Number :-")
        acc_pin = int(input("Type Your Pin :-"))
        print("! Never Share Your PIN with Anyone")

        newdata = [i for i in Bank.dummy_data if i["account.no"] == depodetail and i["pin"] == acc_pin]

        if len(newdata) == 0:
            print("Invalid Information")
        else:
            send_acc = int(input("Enter public id you want to send money to :-"))
            reciever = [i for i in Bank.dummy_data if i["public id"] == send_acc]

            if len(reciever) == 0:
                print("Invalid Information")
            else:
                    amount = int(input('Enter Amount you want to send'))
                    if newdata [0]["balance"] > amount:
                        newdata [0]["balance"] -= amount 
                        reciever [0] ["balance"] += amount
                        Bank.__update()
                        print(f"You have Successfully send {amount} \nSender: {newdata[0]["public id"]} \nReciever: {reciever[0]["public id"] } \nRemaining Balance {newdata[0]["balance"]} \n{Bank.__nowdatetime()}")
  

                    else:
                        print("Insufficient Balance")
    def Updetails(self):
        print("First Login your account")
        depodetail = input("Type Your account Number :-")
        acc_pin = int(input("Type Your Pin :-"))
        print("! Never Share Your PIN with Anyone")

        newdata = [i for i in Bank.dummy_data if i["account.no"] == depodetail and i["pin"] == acc_pin]
        if len(newdata) == 0:
            print("Invalid Information")
        else:
            for key,values in newdata[0].items():
                print(key,": ",values)
    
    def Contactus(self):
        print(f"Here are Contact details you can contact to \nNumber: 000000000 \nEmail : hello@gmail.com")
        print("Or Fill out for form so we can contact you ASAP")
        press = int("Press 1 for form 2 for cancel")

        if press == 1 :
            reason = input("Entrwe reason you want to contact for")
            contact = int(input("Enter Your contact Detail same as given on Account"))
            print("We will reach out to you ASAP")

user =Bank()   

print("Welcome To APNA BANK")
print("Press 1 to Create an Account")
print("Press 2 to Deposit Money")
print("Press 3 to Withdraw Money")
print("Press 4 to Send Money")
print("Press 5 to View Your Details")
print("Press 6 to Contact Customer Service")

user_press = int(input("Tell Us Your Response :-"))
if user_press == 1:
    user.create_account()
elif user_press == 2:
    user.Deposit_money()
elif user_press == 3:
    user.Withdraw_money()
elif user_press == 4 :
    user.Send_money()
elif user_press == 5:
    user.Updetails()
elif user_press == 6:
    user.Contactus()