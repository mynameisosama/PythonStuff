import sys

num = int(sys.argv[1])
print [element for element in range(1,num) if not num%element]==[1]
