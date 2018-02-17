print("This program determines the weekly salary for an employee. \
      The salary is the sum of the hourly rate times the \
      hours worked, plus the bonus. \
      For work hours exceeding 40 per week, an overtime rate \
      of 1.5 is applied. \
      The user must indicate if the worker has received a \
      bonus by answering a y/n question. \
      Input consists of: hours worked, hourly rate, bonus. \
      The output is the total salary for this week.")

hours_worked = float(input("Enter the number of hours worked this week: "))
rate_per_hour = float(input("Enter the salary rate per hour (do not include the '$' sign): "))
yes_no = input("Did the worker get a bonus ? (y/n): ")
if yes_no == 'y':
    bonus = float(input("Enter bonus: "))

if hours_worked > 40:
    overtime = (hours_worked - 40) * rate_per_hour * 1.5
    salary = overtime + bonus + (40 * rate_per_hour)
else:
    overtime = 0
    salary = bonus + (hours_worked * rate_per_hour)

print("The total salary is $" + str(salary) + " (overtime pay $" + str(overtime) + ")")
