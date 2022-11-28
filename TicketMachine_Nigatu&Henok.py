
import time


def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1


def cosmotics():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1


def perfume():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1


def pharmacy():
    number1 = 1
    number2 = 0
    while True:
        yield number1
        number1, number2 = number1 + 1, number2 + 1


henok = 346377252
nigatu = 346369143
list = [henok, nigatu]
retry = 3
count = 0
timer = 8
print("DRUGSTORE MACHINE")
while count < retry:
    employee_id = int(input("**Please enter your correct ID number: "))
    if employee_id in list:
        cosmotics_ticket = cosmotics()
        perfume_ticket = perfume()
        pharmacy_ticket = pharmacy()

        print("\n\t *****  WELLCOME TO OUR DRUGSTORE!!! ******")
        while True:
            print("\n\n\n\t\t\t\t\tCUSTOMER = 'c'\n"
                  "\t\t\t\t\tPHARMACY = 'ph'\n"
                  "\t\t\t\t\tPERFECT = 'p'\n\n")
            place = input("Which of the place you want to vist? ")
            if place == "p":
                print("YOUR NUMER IS:  P", next(perfume_ticket))
            elif place == "ph":
                print("YOUR NUMER IS:  PH", next(pharmacy_ticket))
            elif place == "c":
                print("YOUR NUMER IS:  C", next(cosmotics_ticket))
            else:
                print("Sorry, you didn't choice the correct place.")

            con = input("do you want to continue?")
            if con == "no":
                break

    else:
        count += 1
        continue
else:
    print("Sorry,  come back another time")
    print("The system will be blocked with in 8 second!")
    countdown(timer)
    print("YOU ARE BLOCKED")


