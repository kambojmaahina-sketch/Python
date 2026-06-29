'''enter basic salary of employee and cal net salary HRA=20%,DA=10%'''
a=float(input("enter basic salary:"))
HRA=a*20/100
DA=a*10/100
PF=a*12/100
net_salary=a+HRA+DA-PF
print(f"basic_salary=",a)
print(f"HRA=",HRA)
print(f"DA=",DA)
print(f"PF=",PF)
print(f"net_salary=",net_salary)