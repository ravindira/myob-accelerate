def get_input():
    first_name = input("Please input your name:")
    surname = input("Please input your surname:")
    annual_salary = input("Please enter your annual salary:")
    super_rate = input("Please enter your super rate:")
    payment_start_date = input("Please enter your payment start date:")
    payment_end_date = input("Please enter your payment end date:")
    return {'first_name': first_name, 'surname': surname,
            'annual_salary': annual_salary, 'super_rate': super_rate,
            'payment_start_date': payment_start_date, 'payment_end_date': payment_end_date}


def calculate_tax(annual_salary):
    if annual_salary > 180000:
        income_tax = 54232 + ((annual_salary - 180000) * 0.45)
    elif annual_salary > 87000:
        income_tax = 19822 + ((annual_salary - 87000) * 0.37)
    elif annual_salary > 37000:
        income_tax = 3572 + ((annual_salary - 37000) * 0.325)
    elif annual_salary > 18200:
        income_tax = (annual_salary - 18200) * 0.19
    else:
        income_tax = 0

    return income_tax


def calculate_super(net_income, super_rate):
    super_amount = net_income * super_rate / 100
    return super_amount

def output_payslip():
    pass

if __name__ == "__main__":
    print("payslip")
    # get_input()
    print(calculate_tax(30000))
