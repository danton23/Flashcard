import time
from testmod5 import Update,UserTest,Update2, deleteCat
def main():
    pass
if __name__ == '__main__':
    main()

print ("\n welcome to your vocabulary tutor \n")
time.sleep(2)

def MainProg():
    print ("please choose an option: \n test yourself (t), update existing categories(u), create a new category (cn), delete a category (d)")
    choice1=input("")
    if choice1==("cn") :
        Update()
        MainProg()
    elif choice1==("t"):
        UserTest()
        MainProg()
    elif choice1==("u"):
        Update2()
        MainProg()
    elif choice1 ==("d"):
         deleteCat()
         MainProg()
    else:
        print("sorry you have not entered a valid option please try again! \n")
        MainProg()
MainProg()
