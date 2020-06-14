import time
import random

pfs = "SYSTEM >> "
pft = "TEST >> "
result = random.randint(1,100)

password = input("What is the password to use this app")

def again():
    time.sleep(random.randint(1,2))
    print(pfs + "Downloading files")
    time.sleep(random.randint(1,2))
    print(pfs + "Importing files")
    time.sleep(random.randint(1,2))
    print(pfs + "Initiating files")
    time.sleep(random.randint(1,2))
    print(pfs + "Starting test")
    time.sleep(random.randint(1,2))
    print(pft + "Downloading required files")
    time.sleep(random.randint(1,2))
    print(pft + "Analyzing local files")
    time.sleep(random.randint(1,2))
    print(pft + "Calculating results")
    time.sleep(random.randint(1,2))
    print(pft + "Success!")
    time.sleep(random.randint(1,2))
    print(pft + "Your smartness is " + str(result) + "%")
    global again1
    again1 = input("Do you want to test again?")
    if again1 == " Yes":
        del again1
        again()
    else:
        print("Ok thanks for coming")
        exit()


def main():
    if password == " Hackz1":
        print("Correct password starting app...")
        again()
    else:
        print("Your password was incorrect meaning this code was stolen")
        exit()

main()