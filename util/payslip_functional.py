import math


def get_input():
    first_name = input("Please input your name:")
    surname = input("Please input your surname:")
    annual_salary = int(input("Please enter your annual salary:"))
    super_rate = int(input("Please enter your super rate:"))
    payment_start_date = input("Please enter your payment start date:")
    payment_end_date = input("Please enter your payment end date:")
    return {'first_name': first_name, 'surname': surname,
            'annual_salary': annual_salary, 'super_rate': super_rate,
            'payment_start_date': payment_start_date, 'payment_end_date': payment_end_date}


def calc_tax(annual_salary):
    if annual_salary > 180000:
        annual_income_tax = 54232 + ((annual_salary - 180000) * 0.45)
    elif annual_salary > 87000:
        annual_income_tax = 19822 + ((annual_salary - 87000) * 0.37)
    elif annual_salary > 37000:
        annual_income_tax = 3572 + ((annual_salary - 37000) * 0.325)
    elif annual_salary > 18200:
        annual_income_tax = (annual_salary - 18200) * 0.19
    else:
        annual_income_tax = 0
    return math.ceil(annual_income_tax / 12)


def calc_gross_income(annual_salary):
    return int(annual_salary / 12)


def calc_net_income(gross_income, income_tax):
    return int(gross_income - income_tax)


def output_payslip(income_details):
    print("Name : ", income_details["first_name"], income_details["surname"])
    print("Pay Period: ", income_details["payment_start_date"], "-", income_details["payment_end_date"])
    print("Gross Income: ", income_details["gross_income"])
    print("Income Tax: ", income_details["income_tax"])
    print("Net Income: ", income_details["net_income"])
    print("Super: ", income_details["super"])


def calc_super(net_income, super_rate):
    super_amount = net_income * super_rate / 100
    return int(super_amount)


if __name__ == "__main__":
    income_details = get_input()
    #print(income_details["annual_salary"])
    # print(calculate_tax(income_details["annual_salary"]))
    income_details["income_tax"] = calc_tax(income_details["annual_salary"])
    income_details["gross_income"] = calc_gross_income(income_details["annual_salary"])
    income_details["net_income"] = calc_net_income(income_details["annual_salary"], income_details["income_tax"])
    income_details["super"] = calc_super(income_details["net_income"], income_details["super_rate"])
    output_payslip(income_details)
