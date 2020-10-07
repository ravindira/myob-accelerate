from mamba import context, description, it

from util.payslip_functional import calc_tax

with description("calculate_tax"):
    #
    with context("given a annual salary") as cont:
        #
        with it("when salary is 17000"):
            expected_income_tax = 0
            response_income_tax = calc_tax(17000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 20000"):
            expected_income_tax = 29
            response_income_tax = calc_tax(20000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 60000"):
            expected_income_tax = 921
            response_income_tax = calc_tax(60000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 100000"):
            expected_income_tax = 2053
            response_income_tax = calc_tax(100000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 200000"):
            expected_income_tax = 5270
            response_income_tax = calc_tax(200000)
            assert response_income_tax == expected_income_tax
