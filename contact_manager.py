import json

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""


import json


class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []

    def load_contacts(self):
        """Loads contacts from a JSON file and converts them to a list of dictionaries"""

        try:
            with open(self.file, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

        return self.contacts

    def add_contact(self, contact):
        """Adds a contact to the list, and saves the file"""

        self.contacts.append(contact)

        with open(self.file, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def update_contact(self, contact_to_update):
        """Updates a contact and saves the file"""

        for contact in self.contacts:
            if contact["id"] == contact_to_update["id"]:
                contact["name"] = contact_to_update["name"]
                contact["email"] = contact_to_update["email"]
                contact["phone"] = contact_to_update["phone"]

                with open(self.file, "w") as file:
                    json.dump(self.contacts, file, indent=4)

                return

    def delete_contact(self, id_to_delete):
        """Deletes a contact and saves the file"""

        for contact in self.contacts:
            if contact["id"] == id_to_delete:
                self.contacts.remove(contact)

                with open(self.file, "w") as file:
                    json.dump(self.contacts, file, indent=4)

                return
