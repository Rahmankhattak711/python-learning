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


def delete_contact():
    name = input("Enter name of contact to delete: ")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != name:
                writer.writerow(row)

    print("Contact deleted successfully")


def update_contact():
    name = input("Enter name of contact to update: ")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for i in rows:
            if i[0] == name:
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                new_phone = input("Enter new phone: ")
                i[0] = new_name
                i[1] = new_email
                i[2] = new_phone
                writer.writerow(i)

    print("Contact updated successfully")


def main():
    print("Do you want to add a contact? (1): ")
    print("Do you want to view all contacts? (2): ")
    print("Do you want to search for a contact? (3): ")
    print("Do you want to delete a contact? (4): ")
    print("Do you want to update a contact? (5): ")

    choice = input("Enter your choice: (1-5)")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        update_contact()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
