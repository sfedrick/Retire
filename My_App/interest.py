import pandas as pd
import pdb

class Assets:
    def __init__(self,principal,age,salary,saving,inflation=1.05,returns=1.10,four01k=7500,years=100, birth_year = 1998):
        self.principal = principal
        self.age = age 
        self.salary =salary
        self.years = years
        self.saving = saving
        self.returns = returns
        self.inflation_rate = inflation
        self.current_year = birth_year + age
        self.inflation_csv = pd.read_csv("inflation.csv")
        self.debt_money_end =[]
        self.promotion_earnings =[]
        self.four01k = four01k
        self.birth = birth_year
        
        pass
    
    #calculates inflation using inflation.csv uses default inflation otherwise
    def inflation_calculate(self,year)->float:
        row_size = self.inflation_csv.shape[0]
        start_year = self.inflation_csv.loc[0,'year']
        if(year >= row_size+start_year or year< start_year):
            return self.inflation_rate
        else: 
            return self.inflation_csv.loc[year-start_year,'inflation']
        
    #calculates when a loan will end given interest and monthly payments
    def loan_end(self,principal,loan_pay,interest)-> int:
        i = 0
        while principal > 0:
            i+=1
            if(i%30 ==0):
                principal = (principal-loan_pay)*(1 + (interest-1)/365)
            else:
                principal = principal*(1 + (interest-1)/365)
        return float(i)/365
    #a function to determine whether your allocated money to pay off debt can be put into savings
    def debt_free_money(self,year,end_year,loan_payment)-> int:
        if(year>=int(end_year)+1):
            return loan_payment*12
        elif(year==int(end_year)):
            return (1-abs(end_year-int(end_year)))*12*loan_payment
        else :
            return 0
    #appends the end year and debt payment ammount associated with a given debt to
    # self.debt_money_end 
    def debt_horizon(self,debt):
        row_size = debt.shape[0]
        for i in range(row_size ):
            debt_ammount = float(debt.loc[i,'Amount'])
            debt_payment = float(debt.loc[i,'payment per month'])
            debt_interest = float(debt.loc[i,'interest'])
            year_end = self.loan_end(debt_ammount,debt_payment,debt_interest)
            self.debt_money_end.append([year_end+self.current_year,debt_payment])
    def promotion_money(self,year,promotion_year,salaryincrease):
        if(year>=promotion_year):
            return salaryincrease
        else :
            return 0

    def promotion_extraction(self,promotion):
        row_size = promotion.shape[0]
        for i in range(row_size ):
            try:
                promotion_age = float(promotion.loc[i,'age'])
                promotion_salary = float(promotion.loc[i,'Salary increase post-tax'])
                promotion_salary_tax = float(promotion.loc[i,'taxrate of new money'])
                self.promotion_earnings.append([promotion_age+ self.birth,promotion_salary,promotion_salary/promotion_salary_tax])
            except ValueError:
                print("You have an unused promotion row")
            except ZeroDivisionError:
                print("You're attempting to divide by zero")



            

    def compound_interest(self)->str:
        output =""
        inflation = 1
        for i in range(self.years):
            inflation = self.inflation_calculate(self.current_year+i)*inflation
            salary_needed = self.salary
            year_save = self.saving + self.four01k
            for item in self.debt_money_end:
                year_save = year_save + self.debt_free_money(self.current_year+i,item[0],item[1])

            for item in self.promotion_earnings:
                year_save = year_save + self.promotion_money(self.current_year+i,item[0],item[1])
                salary_needed = salary_needed+ self.promotion_money(self.current_year+i,item[0],item[2])

            principal = (self.principal+year_save*inflation)*self.returns
            self.principal = principal
            string1 = "year %d: principal %.2f saved %d money"%(i+1+self.age, principal,year_save*inflation)
            string2 = "Inflation adjusted dollars : principal %.2f saved %d money monthly save %.2f"%( principal/inflation,year_save*inflation,(year_save*inflation-self.four01k)/12)
            string3 = "Salary 2023 %d inflated salary %d"%(salary_needed,salary_needed*inflation)
            output = output+"\n"+string1+"\n"+string2+"\n"+string3 +"\n"
        return output
