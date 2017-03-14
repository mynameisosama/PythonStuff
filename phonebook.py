class Contact:
    def input(self, name, dob, email, phone):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
    def display(self):
        print("Name: " + self.name)
        print("Date of Birth: " + self.dob)
        print("Email Address: " + self.email)
        print("Phone Number: " + self.phone)

myContacts = [ ]
for i in range(1,2):
    name = input("Enter Name: ")
    dob = input("Enter Date of Birth: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")
    c = Contact(name, dob, email, phone)
    myContacts.append(c)

for i in range(0,1):
    myContacts[i].display()
