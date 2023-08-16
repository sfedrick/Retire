import pandas as pd
import pdb

class Assets:
    def __init__(self,principal,age,salary,saving,inflation=1.05,returns=1.10,four01k=7500,birth_year = 1998,years=100):
        self.principal = principal
        self.inflation_adjusted_principal = principal
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
        self.windfalls = []
        
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

    def windfall_money(self,year,windfall_year,money):
        if(year==windfall_year):
            return money
        else :
            return 0

    def windfall_extraction(self,windfall):
        row_size = windfall.shape[0]
        for i in range(row_size):
                windfall_age = float(windfall.loc[i,'age'])
                windfall_money= float(windfall.loc[i,'windfall or payment'])
                self.windfalls.append([windfall_age+self.birth,windfall_money])
                    

    def compound_interest(self)->str:
        output =""
        inflated_salary = self.salary
        inflated_year_save = self.saving + self.four01k
        inflation = 1
        one_time_payment = 0
        debt_money = 0
        for i in range(self.years):
            if(i>0):
                inflation = self.inflation_calculate(self.current_year+i)*inflation
            else:
                pass

            salary_needed = self.salary
            year_save = self.saving + self.four01k

            for item in self.debt_money_end:
                debt_money = debt_money+self.debt_free_money(self.current_year+i,item[0],item[1])

            for item in self.promotion_earnings:
                money_increase = self.promotion_money(self.current_year+i,item[0],item[1])
                year_save = year_save + money_increase
                sal_increase = self.promotion_money(self.current_year+i,item[0],item[2])
                salary_needed = salary_needed + sal_increase 
                inflated_salary = inflated_salary + sal_increase 

            for item in self.windfalls:
                one_time_payment = one_time_payment + self.windfall_money(self.current_year+i,item[0],item[1])
            
            if(i>0):
                principal = (self.principal+year_save*inflation + debt_money)*self.returns + one_time_payment
            else:
                principal = (self.principal+year_save*inflation + debt_money) + one_time_payment

            self.principal = principal
            inflation_adjusted_principal = principal/inflation
            inflated_salary = salary_needed*inflation 
            inflated_year_save = year_save*inflation + debt_money 
            one_time_payment = 0
            debt_money = 0

            string1 = "year %d: principal %.2f saved %d money"%(i+self.age, principal,inflated_year_save)
            string2 = "Inflation adjusted dollars : principal %.2f saved %d money monthly save %.2f"%(inflation_adjusted_principal,inflated_year_save,(inflated_year_save -self.four01k)/12)
            string3 = "Salary 2023 %d inflated salary %d"%(salary_needed,inflated_salary)
            output = output+"\n"+string1+"\n"+string2+"\n"+string3 +"\n"
        return output
