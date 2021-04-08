import random

userdatabase=[
        {
        'name':'jenny', 'password': 11111
    },
    {
        'name':'cynthia','password':2222
    }
]

def login():
    print("*****login page******")
    accountnumber=input(' validregistered account\n')
    username=input('Enter your username \n')
    password=input('Enter your password \n')

    if (username and password== userdatabase):
        print(f"Welcome {userdatabase}" )

        return True
    else:
        print("invalid password! please try again \n")
        return False


        
def register():
    print("please fill in the details here")

def init():

    isValidoptionSelected=False
    print('welcome to bankn')
    while isValidoptionSelected==False:
        Account=int(input("Do you have account with us: 1 (yes) 2(no) \n"))
        if(Account==1):
            isValidoptionSelected=True
            login()
        elif(Account==2):
            isValidoptionSelected=True
            print( register())
        else:
            print('you have seLected invalid entry')     




def accountgenerated():
    return random.randrange(3333333333,11111111111)

