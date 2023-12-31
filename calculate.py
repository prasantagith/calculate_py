first=input("enter  number : ")
operator=input("enter operator ( +,-,*,/,%,//) :")
second =input ("enter number : ")
first=int(first)
second=int(second)
if operator =="+":
    print(first+ second)

elif operator =="-":
    print(first- second)

elif operator =="*":
    print(first* second)

elif operator =="/":
    print(first/ second)

elif operator =="%":
    print(first% second)
    
elif operator =="//":
    print(first// second)

else:
    print("in valid requirement")
