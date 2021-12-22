import datetime
import re
import sys
import time
import pyfiglet
from colorama import Fore,Style
import os,random

def sprint(str):
    for i in str + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(5.0 / 90)

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

def banner():
        os.system("clear")

        print(ran, pyfiglet.figlet_format("\tSeperator"))
        print(ran + "\t\tV_2.5.0\t\n\n")
        print("*" * 63)

        print(Style.BRIGHT+Fore.LIGHTCYAN_EX, "\n" ,"- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        print("\n" , "*" * 63)
        sprint(Style.BRIGHT + Fore.LIGHTBLUE_EX + "\n\t\tNote: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + "\n\tConvert all text in one or two lines with minimum use of spaces before procceding!")


banner()
def view():
    file  = open("seperator.txt", "r")
    read = file.read()
    print(ran + read)

def exit():
    sys.exit()

cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Seperator\n\t\t[2] View Data\n\t\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        in_text = input("Enter Text full of number: ")

        my_list = re.split("(\d+)", in_text)

        for i in my_list:

            if i.istitle() or i.isalpha():
                file = open("seperator.txt", "a+")
                try:
                    file.write("\nName: " + i)

                except UnicodeEncodeError:
                    pass
                print("\nName: " + i + " Saved Successfully")


            if i.isdigit():
                file = open("seperator.txt", "a+")
                file.write(f"\nPhone: {i}")
                print("Contact: " + i + " Saved Successfully")
                file.write("\n-------------------------------------------\n")
        sprint(ran + "\n\t\tMaking things ready......\n\t\tAlmost Done!....\n")
        print("\n\t\tDone and saved successfully! \n\t\tType cat seperator.txt to access the contents")

    elif choice == "2":
        view()
    elif choice == "3":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        sprint(ran + "\nExiting......")

        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()











