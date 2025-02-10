x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

result = x%y
if result == 0:
    print(str(x)+" is divisible by "+str (y))

else:
    print(str(x)+" is not divisible by "+str (y))