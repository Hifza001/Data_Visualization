# Loading Dataset

import pandas as pd
import matplotlib.pyplot as plt
file_name = 'sales_data_sample.csv'
pd.set_option('display.max_columns', None)
df = pd.read_csv(file_name, encoding='latin1')
#print(df.head(5))



#Line Chart
def create_yearly_sales_line_chart(df):
    yearly_sales = df.groupby('YEAR')['SALES'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(2,2))
    ax.plot(yearly_sales['YEAR'], yearly_sales['SALES'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Sales')
    plt.title('Yearly Sales Trend')
    ax.yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=False))
    plt.grid()
    plt.show()
    
#Function Calling
create_yearly_sales_line_chart(df)


#Pie Chart
def top10_customer_pie_chart(df):
    customer_quantities = df.groupby('CUSTOMERNAME')['QUANTITYORDERED'].sum().reset_index()
    top10_customers = customer_quantities.nlargest(10, 'QUANTITYORDERED')
    fig, ax = plt.subplots()
    ax.pie(top10_customers['QUANTITYORDERED'], labels=top10_customers['CUSTOMERNAME'], autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Customers by Quantity Ordered')
    plt.show()
    
#Function Calling
top10_customer_pie_chart(df)

# Bar Plot

def sales_comparison_bar_plot(df):
    uk_sales = df[df['COUNTRY'] == 'UK']['SALES'].sum()
    us_sales = df[df['COUNTRY'] == 'USA']['SALES'].sum()
    countries = ['UK', 'US']
    sales = [uk_sales, us_sales]

    plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
    plt.bar(countries, sales, color=['blue', 'green'])
    plt.xlabel('Country')
    plt.ylabel('Total Sales')
    plt.title('Sales Comparison Between UK and US')
     # Show the plot
    plt.show()

# Function Calling
sales_comparison_bar_plot(df)
