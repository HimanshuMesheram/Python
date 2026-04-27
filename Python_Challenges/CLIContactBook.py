import csv
import os

class CLIContactBook:

    FILE_NAME = "contacts.csv"

    def __init__(self):
        self.initialize_file()

    def menu(self):

        while True:

            print('''
            1.Add contact
            2.View all contacts
            3.Search for a contact by name
            4.Exit
            ''')

            choice = input("Enter choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contact()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                break
            else:
                print("Invalid chouce try again")


    def initialize_file(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"])
    
    def read_contacts(self):
        with open(self.FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def add_contact(self):
        contacts = self.read_contacts()
        name = input("Enter Name: ").strip()

        # Prevent duplicate
        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                print("Contact already exists!")
                return

        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()

        with open(self.FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])

        print("Contact added successfully!")

    def view_contact(self):
        contacts = self.read_contacts()

        if not contacts:
            print("No contacts found.")
            return

        print("\n" + "="*50)
        print(f"{'Name':<15}{'Phone':<15}{'Email':<20}")
        print("="*50)

        for contact in contacts:
            print(f"{contact['Name']:<15}{contact['Phone']:<15}{contact['Email']:<20}")

        print("="*50)

    def search_contact(self):
        keyword = input("Enter name to search: ").strip().lower()
        contacts = self.read_contacts()

        results = [c for c in contacts if keyword in c["Name"].lower()]

        if not results:
            print("No matching contacts found.")
            return

        print("\nSearch Results:")
        print("="*50)
        print(f"{'Name':<15}{'Phone':<15}{'Email':<20}")
        print("="*50)

        for contact in results:
            print(f"{contact['Name']:<15}{contact['Phone']:<15}{contact['Email']:<20}")

        print("="*50)


cb = CLIContactBook()
cb.menu()