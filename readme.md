This is a my customized retirement app calculater. 

First run the following command 
<code>chmod +x set_up.sh</code>

then run the code using <code>./run_app</code>

# Features
There are several features for this app. It includes basic things like compound interest from savings. Along with how much your salary has to increase to keep up with inflation. I recommend starting from when you first started saving. To see if you are on track with your retirement goals and if you can save less or more.

Inflation adjusts money for the first year entered. I.e if you entered your age of 25 and birth year 1996 than we would assume we're in the year 2021 and all inflated dollars will be reverted to their 2021 equivalent. Fill out the inflation.csv with inflation information for each specific year. For any year not entered we use the default inflation entered by the user in the app.

Debt money isn't assumed to keep up with inflation. We assume you are performing constant payments over the coarse of your loan. So we don't require you to increase debt money with inflation once it frees we make sure that the ammount saved keeps up with inflation

All textboxes with a star require input in order to run the app

Because 401ks and roth iras have taxable limits we assume that these payments can't be increased with inflation and will be the same year after year.

# Debt payoff 
I include an option to enter debts and the speed at which you pay them off. Once this debt is paid off the money once used to pay off the debt is added to your savings.

# Promotions 
You can enter anticipated promotions in your career planning.

# Windfalls 
You can enter one time payments and windfalls to see if you should really buy that new car or not, or what you should do with the money your Pops left you.

# Load in previous finance scenarios 
You can now save your results to a csv file and load them in for later to see how well you have kept up with your financial goals and projections. The CSV's get saved to a folder called Saved_Data. The format of the data in the CSV is as follows as an example :
0 #first row doesn't mean anything it will always be zero
0 #second row is your starting principle
25 # third row is your age
70000 # income after tax
12000 # ammount saved per year
"name,Amount,interest,payment_per_month # debt pandas array
0,54000,1.05,1000
1,0,0,0
2,0,0,0"
"name,age,Salary_increase_post-tax # promotion pandas array
0,30,12000"
"name,age,windfall_or_payment #windfall array
0,0,0" 
2023 #current year
1.05 # inflation estimate for years that don't have inflation data in the inflation.csv array
1.10 # projected returns year over year
7500 # fixed ammount saved to your 401k each year
13000 # principal ammount in your 401k 

you can edit these values and load them in to check different scenarios.

# Upcoming features
I will add a plots of income over time adjusted for inflation.

I will add an auto lynter.



