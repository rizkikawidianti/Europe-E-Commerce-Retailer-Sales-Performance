import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max.columns', None)
pd.set_option('display.max.row', None)
pd.set_option('display.width', 500)
df = pd.read_csv(r"C:\Users\COURSE\STUDY CASE\PYTHON\europe_ecommerce_orders\europe_ecommerce_orders_15000.csv")
print(df)

df = df.drop_duplicates()

df["order_date"] = pd.to_datetime(df["order_date"], format='mixed', dayfirst=True, errors='coerce')

unique=df['country'].unique()
print(*unique, sep='\n')

unique_sub=df['sub_region'].unique()
print(*unique_sub, sep='\n')

sales_dict={'WEB': 'Website',
'website': 'Website',
'mobile app': 'Mobile App',
'marketplace' : 'Marketplace',
'App': 'Mobile App',
'Market Place' : 'Marketplace'}
df['sales_channel']=df['sales_channel'].replace(sales_dict)
print(*df['sales_channel'].unique(), sep='\n')

print(*df['product_category'].unique(), sep='\n')

print(*df['customer_segment'].unique(), sep='\n')

df['shipping_mode']=df['shipping_mode'].str.title()
print(*df['shipping_mode'].unique(), sep='\n')

print(*df['units_sold'].unique(), sep='\n')

print(*sorted(df['net_sales_eur'].unique()), sep='\n')

print(*sorted(df['discount_pct'].unique()), sep='\n')

print(*sorted(df['delivery_days'].unique()), sep='\n')

df['return_status']=df['return_status'].str.title()
return_dict={'Exchange':'Exchanged', 'No Return':'Not Returned'}
df['return_status']=df['return_status'].replace(return_dict)
print(*df['return_status'].unique(), sep='\n')

high_sales = (
    df.groupby(['country','sub_region'])['net_sales_eur']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
high_sales['%_of_Sales'] = (
    high_sales['net_sales_eur'] / high_sales['net_sales_eur'].sum() * 100
).round(2).astype(str) + '%'

print(high_sales)

order_volume = (
    df.groupby(['country','sub_region'])['units_sold']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
order_volume['%_of_orders'] = (
    order_volume['units_sold'] / order_volume['units_sold'].sum() * 100
).round(2).astype(str) + '%'
print(order_volume)

df['Year'] = df['order_date'].dt.year
df['Month'] = df['order_date'].dt.month

monthly_sales = (
    df.groupby(['Year', 'Month'])['net_sales_eur']
    .sum()
    .reset_index()
)
print(monthly_sales)

return_pivot = pd.crosstab(
    index=df['product_category'], 
    columns=df['return_status'], 
    dropna=False  # <--- The magic trick! Forces NaN to become its own column.
)
print(return_pivot)

returned_only = df[df['return_status'] == 'Returned']
return_count = (
    returned_only.groupby('product_category')
    .size()
    .sort_values(ascending=False)
    .reset_index(name='Total_Returns')
)
print(return_count)





















