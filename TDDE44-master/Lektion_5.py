#!/usr/bin/env python3
import Klasser.Contact

#Contact = Klasser.Contact


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
