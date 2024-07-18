import os

def menu():
    menu_string = "1. Show Menu\n"
    menu_string += "2. Add Numbers\n"
    menu_string += "3. Substract Numbers\n"
    menu_string += "4. Quit\n"
    return menu_string

os.system("cls" if os.name == "nt" else "clear")
choice = 0

while choice != 4:

    print(menu())
    choice = int(input("Enter your choice: "))

    if choice == 1:
        os.system("cls" if os.name == "nt" else "clear")
    elif choice == 2:
        print("\n\nAdd Some Numbers\n\n")
    elif choice == 3:
        print("\n\nSubtract some Numbers\n\n")
    else:
        pass

#Save the result as .txt file in a file named results_Ruby
with open("results_Ruby.txt", "w") as f:
    f.write(f"Choice: {choice}")
      