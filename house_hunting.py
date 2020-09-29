annual_salary = input("Enter Your Annual Salary: ")

portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
monthly_salary_saved = (float(annual_salary)/12)*float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")

portion_down_payment = 0.25 * float(total_cost)
current_savings = 0

i = 0
#when i use i=0 test 1 is off by one month and test 2 is correct
#when i use i=1 test 1 is correct and test 2 is off by one month

while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    i+=1
    

print("Number of months: ", i)
# print("It will take you", i, "months to save up enough money for a down payment!")