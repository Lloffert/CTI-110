# Lydia Loffert
# 10/23/2024
# P3HW2
# Calculate reg and OT pay for an employee

# Get employee information from user
name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked as an integer: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Determine if overtime or not and assign OT hours
if hours > 40:
    OT_hours = (hours - 40)
else:
    OT_hours = 0

#Calculate variables for pay information
OT_payrate = pay_rate * 1.5
OT_pay = OT_hours * OT_payrate
regPay = pay_rate * 40
gross_pay = regPay + OT_pay

#Display pay information to user
print("-" * 50)
print(f"Employee name:   {name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("-" * 95)
print(f"{hours:<15}{pay_rate:<15}{OT_hours:<15}{OT_pay:<15}{regPay:<15}{gross_pay}")












