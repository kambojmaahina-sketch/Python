'''swapping of 2 num'''

#--method1
n1=int(input("enter 1st num"))
n2=int(input("enter 2nd num"))
n1,n2=n2,n1
print(f"after swapping:")
print(f"n1=",n1)
print(f"n2=",n2)

#--method2
n1=int(input("enter 1st num"))
n2=int(input("enter 2nd num"))
temp=n1
n1=n2
n2=temp
print(f"after swapping:")
print(f"n1=",n1)
print(f"n2=",n2)