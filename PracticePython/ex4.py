num = int(raw_input("Enter a Number: "))
print [element for element in range(1,num) if not num%element]
