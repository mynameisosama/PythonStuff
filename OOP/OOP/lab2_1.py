def isPrime(num):
    return [element for element in range(1,num) if num%element==0] == [1]
num = int(input("Enter a number and I'll tell if it's a prime number: "))
if(isPrime(num)):
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")