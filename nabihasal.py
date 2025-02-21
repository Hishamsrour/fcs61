import random

10
def manage_finances():
    print("Welcome to Nabiha's Monthly Finance Manager!\n")

    # User inputs
    salary = float(input("Enter your salary for the month: $"))
    month = input("Enter the name of the month: ")
    
    print("\nEnter the following percentages (without % sign):")
    savings_percent = float(input("Percentage for Savings: ")) / 100
    rent_percent = float(input("Percentage for Rent: ")) / 100
    electricity_percent = float(input("Percentage for Electricity: ")) / 100

    # Calculations
    savings_amount = salary * savings_percent
    rent_amount = salary * rent_percent
    electricity_amount = salary * electricity_percent

    total_allocations = savings_amount + rent_amount + electricity_amount
    remainder = salary - total_allocations

    yearly_rent = rent_amount * 12
    yearly_electricity = electricity_amount * 12

    additional_savings = 50  # Random additional savings amount
    division_result = additional_savings / savings_amount if savings_amount != 0 else "N/A (Savings is zero)"

    print(f"\nFinancial Summary for {month}:")
    print(f"- Savings Allocation: ${savings_amount:.2f}")
    print(f"- Rent Allocation: ${rent_amount:.2f}")
    print(f"- Electricity Allocation: ${electricity_amount:.2f}")
    print(f"- Total Allocations: ${total_allocations:.2f}")
    print(f"- Remainder after expenses: ${remainder:.2f}")
    print(f"- Estimated Yearly Rent: ${yearly_rent:.2f}")
    print(f"- Estimated Yearly Electricity: ${yearly_electricity:.2f}")
    print(f"- $50 divided by total savings allocation: {division_result}")

if __name__ == "__main__":
    manage_finances()
