monthlyIncome = int(input("Enter your montly income: "))
monthlyExpenses = int(input("Enter your montly expenses: "))

monthlySavings = monthlyIncome - monthlyExpenses

projectedSavings = (monthlySavings * 12 + (monthlySavings * 12 * 0.05))

print("Your montly savings are $",monthlySavings)
print("Projected savings after one year, with interest, is: $",projectedSavings)