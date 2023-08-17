import pandas as pd
import pdb
from datetime import date
class Assets:
    def __init__(self,principal,age,salary,saving,current_year = -1,inflation=1.05,returns=1.10,four01k=7500,four01k_total=0,years=100):
        self.principal = principal + four01k_total
        self.inflation_adjusted_principal = principal
        self.age = age 
        self.salary =salary
        self.years = years
        self.saving = saving
        self.returns = returns
        self.inflation_rate = inflation
        self.inflation_csv = pd.read_csv("inflation.csv")
        self.debt_money_end =[]
        self.promotion_earnings =[]
        self.four01k = four01k
        self.four01k_total = four01k_total
        self.windfalls = []
        
        if(current_year <= 0):
            today = date.today()
            self.current_year = float(today.year)
            self.birth = self.current_year - self.age
        else:
            self.current_year = current_year
            self.birth = current_year-age

        
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
                self.promotion_earnings.append([promotion_age+ self.birth,promotion_salary])
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
        #create copies of variables being modified in function
        output =""
        inflated_salary = self.salary
        inflated_year_save = self.saving 
        inflation = 1
        total_inflation = 1
        four01k = self.four01k
        four01k_total = self.four01k_total
        uninflated401k = self.four01k_total
        inflation_adjusted_principal = self.principal
        salary_needed = self.salary
        year_save = self.saving 

        for i in range(self.years):
            #initialize money gains for the year
            debt_money = 0
            money_increase = 0
            one_time_payment = 0

            if(i>0):
                inflation = self.inflation_calculate(self.current_year+i)
                total_inflation = self.inflation_calculate(self.current_year+i)*total_inflation
            else:
                pass
            
            for item in self.debt_money_end:
                debt_money = debt_money+self.debt_free_money(self.current_year+i,item[0],item[1])

            for item in self.promotion_earnings:
                money_increase = money_increase+self.promotion_money(self.current_year+i,item[0],item[1])
            
            for item in self.windfalls:
                one_time_payment = one_time_payment + self.windfall_money(self.current_year+i,item[0],item[1])
            

            #calculate ammount saved and ammount that should be saved given inflation
            year_save = self.saving + money_increase + debt_money
            inflated_year_save = year_save*total_inflation

            #calculate salary and inflated salary 
            salary_needed = self.salary + money_increase 
            inflated_salary = salary_needed*total_inflation

            #prevent returns from being applied when an item is first added to principal
            if(i>0):
                #principal is a combination of itself, one time payment,savings for the year, and 401k total 
                principal = (self.principal)*self.returns + one_time_payment + inflated_year_save + four01k
                #inflated principal is the same as principal but we scale it by this years inflation before adding returns and additions
                inflation_adjusted_principal = (inflation_adjusted_principal/inflation)*self.returns + one_time_payment + inflated_year_save + four01k
                four01k_total = (four01k_total)*self.returns + self.four01k
                uninflated401k =  (uninflated401k/inflation)*self.returns + self.four01k
            else:
                principal = self.principal + one_time_payment
                four01k_total = four01k_total
            self.principal = principal
            inflation_adjusted_principal = principal/total_inflation 
            
            

            string1 = "Current year:%d Age: %d: principal %.2f saved %.2f money"%(i+self.current_year,i+self.age, principal,inflated_year_save+ self.four01k)
            string2 = "Inflation adjusted dollars : principal %.2f money monthly save (does not include 401k) :%.2f"%(inflation_adjusted_principal,(inflated_year_save)/12)
            string3 = "Post tax Salary %d: %d inflated salary: %d"%(self.age+self.birth,salary_needed,inflated_salary)
            try:
                string4 = "total 401k Saved:%.2f Inflation adjusted 401k: %.2f retirement/private: %.2f"%(four01k_total,uninflated401k,four01k_total/self.principal)
            except ZeroDivisionError:
                string4 = "total 401k Saved:%.2f Inflation adjusted 401k: %.2f retirement/private:0"%(four01k_total,uninflated401k)
            output = output+"\n"+string1+"\n"+string2+"\n"+string3 +"\n"+string4+"\n"
            
        return output
