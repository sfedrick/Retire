This is a my customized retirement app calculater. 

First run the following command 
<code>chmod +x activate_first_time.sh</code>

then run the code using <code>./run_app</code>

# Features
There are several features for this app. It includes basic things like compound interest from savings. Along with how much your salary has to increase to keep up with inflation. I recommend starting from when you first started saving. To see if you are on track with your retirement goals and if you can save less or more.

Inflation adjusts money for the first year entered. I.e if you entered your age of 25 and birth year 1996 than we would assume we're in the year 2021 and all inflated dollars will be reverted to their 2021 equivalent. Fill out the inflation.csv with inflation information for each specific year. For any year not entered we use the default inflation entered by the user in the app.

Debt money isn't assumed to keep up with inflation. We assume you are performing constant payments over the coarse of your loan. So we don't require you to increase debt money with inflation once it frees up in the same way we do with normal yearly savings.

All textboxes with a star require input in order to run the app

# Debt payoff 
I include an option to enter debts and the speed at which you pay them off. Once this debt is paid off the money once used to pay off the debt is added to your savings.

# Promotions 
You can enter anticipated promotions in your career planning.

# Windfalls 
You can enter one time payments and windfalls to see if you should really buy that new car or not, or what you should do with the money your Pops left you.

# Upcoming features
I will add a plots of income over time adjusted for inflation.

I will add an auto lynter.

I can't get the flag button to work I will add that as well.

