import sys
import csv
from exceptions import *

def main():
    if password():
        while True:
            action = input("\nSelect action[write/read/cancel]: ").lower()
            
            if PassError().catch(action, False):
                if action == "read":
                    selection()
                elif action == "write":
                    write()
                elif action == "cancel":
                    break
                else:
                    print("Response was unclear, try again.")     

def password():
    attempts = 3

    for i in range(attempts):
        code = int(input("Enter access code: "))

        if PassError().catch(code, True):
            if code == 8316:
                print("System access granted.")
                return True
            else:
                if i != 2:
                    print("Invalid code.", (attempts - (i + 1)), "attempts remaining.")
                else:
                    sys.exit("Invalid code. System has been locked.")

#to read from file
def selection():
    while True:
        subject = input("\nWho would you like to assess[name or ID]: ").title()
        stats(subject)

        response = input("\nWould you like to proceed: ").title()

        if response != "Yes":
            break

def stats(subject): #helper method to selection()
    with open("facility.csv") as file:
        reader = csv.DictReader(file)
        identified = False

        if subject != "Access All":
            for line in reader:
                if line["subject"] == subject or line["ID"] == subject:
                    print("\nName:", line["subject"])
                    print("Subject Number:", line["ID"])
                    print("Abilities:", line["abilities"])
                    identified = True
                    break
            
            if not identified:
                print("Subject was not able to be identified.")
        else:
            list = []

            for line in reader:
                list.append(line)
            
            for element in sorted(list, key=lambda element: element["subject"]):
                print("\nName:", element["subject"])
                print("Subject Number:", element["ID"])
                print("Abilities:", element["abilities"])

#to write into file
def write():
    while True:
        subject = input("\nEnter subject: ")
        ID = int(input("Enter ID: "))
        abilities = input("Enter abilities[list format]: ")

        with open("facility.csv", 'a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=["subject", "ID", "abilities"])
            writer.writerow({"subject": subject, "ID": ID, "abilities": abilities})

        response = input("\nWould you like to proceed: ").title()

        if response != "Yes":
            break

if __name__ == "__main__":
    main()
