#read the seller name
seller_name=input("Enter the name: ")
fixed_salary= float(input("Enter salary:"))
total_sells= float(input("Enter the sell:"))

#calculate the salary
total_salary= fixed_salary+(total_sells*0.15)

#print the result
print(f"total salary: {total_salary}")