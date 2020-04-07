#!/usr/bin/env python3


class Contact(object):

    def __init__(self, name):
        self.name = name
        self.phone_num = ""

    def __str__(self):
        citation = "name: {} \nphone number: {}"
        return citation.format(self.name, self.phone_num)

    # def __str__(self):
    # return "{}, {}".format(self.name, self.phone_num)

    def append_to_name(self, string_to_append):
        self.name = self.name + string_to_append


c1 = Contact("Emil")
c2 = Contact("Benno")
c3 = Contact("Kalle")
c1.phone_num = "0701-111111"
c2.phone_num = "0702-222222"
c3.phone_num = "0700-123456"
c1.append_to_name(" Säll")
c2.append_to_name(" Nossbring")
c3.append_to_name(" Ytterberg")

contact_list = [c1, c2, c3]

for element in contact_list:
    print(element)
