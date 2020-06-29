stock_prices=[("APPLE",200),("GOOGLE", 400), ("MICROSOFT", 500)]
for item in stock_prices:
    print (item)

for ticker,price in stock_prices:
    print (ticker)
    print (price+(0.1*price))

work_hours=[("abby",100),("Billy",400),("cassie",800)]

def employee_check(work_hours):
    current_max=0
    employee_of_month=""

    for employee, hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
    #print (employee_of_month, current_max)
    return(employee_of_month,current_max)





result=employee_check(work_hours)

print (result)

name,hours=employee_check(work_hours)

print (name)
print (hours)