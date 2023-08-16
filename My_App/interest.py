class Assets:
    def __init__(self,principal,age,salary,saving,years=30,debt_payment=12000,debt=54000,interest_debt=1.05,returns=1.10,inflation=1.05):
        self.principal = principal
        self.age = age 
        self.salary =salary
        self.years = years
        self.saving = saving
        self.debt_payment = debt_payment
        self.debt = debt
        self.interest_debt = interest_debt
        self.returns = returns
        self.inflation_rate = inflation
        
        pass

    def compound_interest(self)->str:
        output =""
        for i in range(self.years):
            inflation = self.inflation_rate**(i)
            salary_needed = self.salary
            year_save = self.saving
            principal = (self.principal+year_save*inflation)*self.returns
            self.principal = principal
            string1 = "year %d: principal %.2f saved %d money"%(i+1+self.age, principal,year_save*inflation)
            string2 = "Inflation adjusted dollars : principal %.2f saved %d money monthly save %.2f"%( principal/inflation,year_save*inflation,(year_save*inflation-7500)/12)
            string3 = "Salary 2023 %d inflated salary %d"%(salary_needed,salary_needed*inflation)
            output = output+"\n"+string1+"\n"+string2+"\n"+string3
        return output
