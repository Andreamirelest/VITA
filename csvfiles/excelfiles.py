# How to create a code in pyton 101

# code in python that allows to analyze financial data from excel

import panda as pd # import ándas library as pd , used for data manipulation 

import matplotlib.pyplot as plt # used for data visualization 


df = pf.read_excel(¨financial_data.xlsx¨)   #financial data inserted into python file from excel 

# displaying DataFrame infortmation

print(df.head())     # displays the first few rows of the data frame giving an overview of the data 
print(df.describe()) # provides basic statistics (count, mean, standard deviation, min, quartiles, and max) for numerical columns in the DataFrame.


#Calculating Total Revenue, Expenses and Profit 

total_revenue = df['Revenue'].sum()
total_expenses = df['Expenses'].sum()
total_profit = total_revenue - total_expenses

# use sum() function to calculate the values in reveue and expenses

# printing total revenue, expenses and profit 
print(f"Total Revenue: ${total_revenue}")
print(f"Total Expenses: ${total_expenses}")
print(f"Total Profit: ${total_profit}")

#Plot Revenue and Expanses over time 

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Revenue'], label='Revenue')
plt.plot(df['Date'], df['Expenses'], label='Expenses')
plt.xlabel('Date')
plt.ylabel('Amount ($)')
plt.title('Revenue and Expenses Over Time')
plt.legend()
plt.show()





