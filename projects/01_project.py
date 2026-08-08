import csv
import os

FILENAME = "contact.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone"])


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    print("Contact added successfully")


def view_contact():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("Contact list is empty")


def search_contact():
    name = input("Enter name of contact to search: ")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print(row)
                break
            else:
                print("Contact not found")


def main():
    add = input("Do you want to add a contact? (1): ").lower()
    view = input("Do you want to view contacts? (2): ").lower()
    search = input("Do you want to search for a contact? (3): ").lower()

    if add == "1":
        add_contact()
    elif view == "2":
        view_contact()
    elif search == "3":
        search_contact()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
