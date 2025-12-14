monthly_income = float(input("Enter your montly income: "))
monthly_expenses = float(input("Enter your montly expenses: "))

monthly_savings = monthly_income - monthly_expenses

projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Your montly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",projected_savings)