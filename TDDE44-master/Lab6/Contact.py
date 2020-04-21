#!/usr/bin/env python3


class Contact(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        frase = "{}, {}"
        return frase.format(self.last_name, self.first_name)


# c1 = Contact("Ada", "Lovelace")
# c2 = Contact("Alan", "Turing")
# print(c1)


class ContactList(object):

    def __init__(self):
        self.contacts = []

    def create_and_add_contact(self, first_name, last_name):
        self.contacts.append(Contact(first_name, last_name))

    def __str__(self):
        string = ""
        for name in self.contacts:
            if name  == self.contacts[-1]:
                string += Contact.__str__(name)
            else:
                string += Contact.__str__(name) + "\n"
        return string

contactlist = ContactList()
contactlist.create_and_add_contact("Ada", "Lovelace")
contactlist.create_and_add_contact("Alan", "Turing")

print(contactlist)
