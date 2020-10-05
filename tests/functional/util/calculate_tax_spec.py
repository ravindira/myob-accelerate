from mamba import context, description, it

from util.payslip import calculate_tax

with description("calculate_tax"):
    #
    with context("given a annual salary") as cont:
        #
        with it("when salary is 17000"):
            expected_income_tax = 0
            response_income_tax = calculate_tax(17000)
            # print(response_income_tax)
            assert response_income_tax == expected_income_tax

        with it("when salary is 20000"):
            expected_income_tax = 342
            response_income_tax = calculate_tax(20000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 60000"):
            expected_income_tax = 11047
            response_income_tax = calculate_tax(60000)
            assert response_income_tax == expected_income_tax

        with it("when salary is 100000"):
            expected_income_tax = 24632
            response_income_tax = calculate_tax(100000)
            # print(response_income_tax)
            assert response_income_tax == expected_income_tax

        with it("when salary is 200000"):
            expected_income_tax = 63232
            response_income_tax = calculate_tax(200000)
            # print(response_income_tax)
            assert response_income_tax == expected_income_tax