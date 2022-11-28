from ticket_machine_utility import countdown
from ticket_machine_main import cosmotics
from ticket_machine_main import perfume
from ticket_machine_main import pharmacy

henok = 346377252
nigatu = 346369143
list = [henok, nigatu]
retry = 3
count = 0
timer = 8
print("DRUGSTORE MACHINE")


def ticket():
    global count
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

                con = input("Do you want to continue?")
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
