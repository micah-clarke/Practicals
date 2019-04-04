
def monthly_income_report():
    incomes = []
    number_of_months = int(input("How many months? "))
    for months in range(1, number_of_months + 1):
        income = float((input("Enter income for month {}: ".format(number_of_months))))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {} - Income: ${:8.2f} \
              Total: ${:10.2f}".format(month + 1, income, total))


monthly_income_report()
