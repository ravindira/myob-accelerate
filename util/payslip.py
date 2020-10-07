import math


class PaySlip:

    def __init__(self):
        self.first_name = input("Please input your name:")
        self.surname = input("Please input your surname:")
        self.annual_salary = int(input("Please enter your annual salary:"))
        self.super_rate = int(input("Please enter your super rate:"))
        self.payment_start_date = input("Please enter your payment start date:")
        self.payment_end_date = input("Please enter your payment end date:")

        # self.first_name = "Ravi"
        # self.surname = "Kasi"
        # self.annual_salary = int("84000")
        # self.super_rate = int("9")
        # self.payment_start_date = "1 March"
        # self.payment_end_date = "30 March"

    def calc_income_tax(self):
        if self.annual_salary > 180000:
            annual_income_tax = 54232 + ((self.annual_salary - 180000) * 0.45)
        elif self.annual_salary > 87000:
            annual_income_tax = 19822 + ((self.annual_salary - 87000) * 0.37)
        elif self.annual_salary > 37000:
            annual_income_tax = 3572 + ((self.annual_salary - 37000) * 0.325)
        elif self.annual_salary > 18200:
            annual_income_tax = (self.annual_salary - 18200) * 0.19
        else:
            annual_income_tax = 0

        income_tax = math.ceil(annual_income_tax / 12)
        return income_tax

    def calc_gross_income(self):
        return int(self.annual_salary / 12)

    def calc_net_income(self):
        return int(self.gross_income - self.income_tax)

    def calc_super(self):
        super_amount = self.net_income * self.super_rate / 100
        return int(super_amount)

    def output_payslip(self):
        print("Name : ", self.first_name, self.surname)
        print("Pay Period: ", self.payment_start_date, "-", self.payment_end_date)

        print("Gross Income: ", self.gross_income)
        print("Net Income: ", self.net_income)
        print("Super: ", self.super)


if __name__ == "__main__":
    payslip1 = PaySlip()
    payslip1.income_tax = payslip1.calc_income_tax()
    payslip1.gross_income = payslip1.calc_gross_income()
    payslip1.net_income = payslip1.calc_net_income()
    payslip1.super = payslip1.calc_super()
    payslip1.output_payslip()
