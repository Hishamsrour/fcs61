def main():
    salary = float(input("Enter your salary for the month: $"))
    month = input("Enter the name of the month: ")

    savings_percentage = float(input("Enter the percentage of your salary you want to save: "))
    rent_percentage = float(input("Enter the percentage of your salary for rent: "))
    electricity_percentage = float(input("Enter the percentage of your salary for electricity: "))

    savings_amount = (savings_percentage / 100) * salary
    rent_amount = (rent_percentage / 100) * salary
    electricity_amount = (electricity_percentage / 100) * salary