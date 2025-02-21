def main():
    salary = float(input("Enter your salary for the month: $"))
    month = input("Enter the name of the month: ")

    savings_percentage = float(input("Enter the percentage of your salary you want to save: "))
    rent_percentage = float(input("Enter the percentage of your salary for rent: "))
    electricity_percentage = float(input("Enter the percentage of your salary for electricity: "))

    savings_amount = (savings_percentage / 100) * salary
    rent_amount = (rent_percentage / 100) * salary
    electricity_amount = (electricity_percentage / 100) * salary

    total_expenses = savings_amount + rent_amount + electricity_amount
    remainder = salary - total_expenses

    yearly_rent = rent_amount * 12
    yearly_electricity = electricity_amount * 12

    additional_savings = 50
    if savings_amount > 0:
        savings_division = additional_savings / savings_amount
    else:
        savings_division = "undefined (you are not saving anything)"

    print("\n--- Monthly Financial Summary for {} ---".format(month))
    print("Your Salary: ${:.2f}".format(salary))
    print("Amount allocated to Savings: ${:.2f}".format(savings_amount))
    print("Amount allocated to Rent: ${:.2f}".format(rent_amount))
    print("Amount allocated to Electricity: ${:.2f}".format(electricity_amount))
    print("Total Expenses (Savings + Rent + Electricity): ${:.2f}".format(total_expenses))
    print("Remaining Amount after Expenses: ${:.2f}".format(remainder))
    print("Estimated Yearly Rent: ${:.2f}".format(yearly_rent))
    print("Estimated Yearly Electricity: ${:.2f}".format(yearly_electricity))
    print("If you save an extra $50, it would be divided by your savings amount: {}".format(savings_division))

    if __name__ == "__main__":
        main()