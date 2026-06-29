'''enter marks of subjects print total and percentage assume marks out of 100 
( INPUT MAX MARKS ALSO)'''
m1 = float(input("Enter marks of Sub 1:"))
max1 = float(input("Enter maximum marks of Sub 1:"))
m2 = float(input("Enter marks of Subject 2:"))
max2 = float(input("Enter maximum marks of Sub 2:"))
m3 = float(input("Enter marks of Sub 3:"))
max3 = float(input("Enter maximum marks of Sub 3:"))
m4 = float(input("Enter marks of Sub 4:"))
max4 = float(input("Enter maximum marks of Sub 4:"))
m5 = float(input("Enter marks of Sub 5:"))
max5 = float(input("Enter maximum marks of Sub 5:"))
total = m1 + m2 + m3 + m4 + m5
max_total = max1 + max2 + max3 + max4 + max5
percentage = (total / max_total) * 100
print("Total Marks =", total)
print("Maximum Marks =", max_total)
print("Percentage =", percentage, "%")