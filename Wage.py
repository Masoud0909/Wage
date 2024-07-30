numEmployee = int (input ("Enter the number of employees: "))
total_wage=0  
#getting employee details
for i in range (numEmployee):
    employee_name = input (f"Enter the name of employee {i + 1}: ")
    hours_Worked = float(input(f"Enter the hours worked by {employee_name}: "))
    hourly_rate  = float (input(f"Enter the hourly rate for {employee_name}: "))    
#Calculating regular vs. overtime
if hours_Worked>40:
    overtime=hours_Worked-40
    regular= 40
else:
    overtime = 0
    regular = hours_Worked
#Calculating pay
overtime = overtime * hourly_rate * 1.5
regular = regular * hourly_rate
wage = regular + overtime
#Output employee wages
print(f"{employee_name}'s wages: ${wage:.2f}") #using .2f to round two decimal places
#accumulating total wage
total_wage +=wage
#output total wage
print(f"Total wages for all employees: ${total_wage:.2f}") 



