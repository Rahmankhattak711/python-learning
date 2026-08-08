import csv
import os

FILENAME = "contact.csv"

if os.path.exists(FILENAME):
    with open(FILENAME, "w"):
        writer = csv.writer(open(FILENAME, "w"))
        writer.writerow(["Name", "Email", "Phone"])


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    if os.path.exists(FILENAME):
        with open(FILENAME, "a") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone])
    else:
        with open(FILENAME, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Phone"])

    with open(FILENAME, "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    print("Contact added successfully")


add_contact()
