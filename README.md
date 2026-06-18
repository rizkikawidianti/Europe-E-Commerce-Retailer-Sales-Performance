# Europe-E-Commerce-Retailer-Sales-Performance
**Executive Summary**
This project analyzes sales performance and return behavior for a mid-sized e-commerce retailer operating across Europe. The analysis uses Python to clean, transform, and explore order-level sales data from 2024 to 2025.
The goal is to understand how sales and order volume vary across countries, sub-regions, and product categories. The analysis also looks at monthly sales trends and return patterns to identify areas that may need further investigation.
Key findings show that Germany in Western Europe generated the highest sales contribution and order volume. Monthly sales increased steadily throughout 2024, but showed a downward trend in 2025. Fashion had the highest return volume across the two-year period.

**Business Problem:**
A mid-sized e-commerce retailer operating across Europe wants to understand why sales performance and return behavior vary across countries, channels, and product categories. Management suspects that recent growth in marketplace sales and discounting may be affecting delivery times, customer behavior, and return rates, especially in Southern and Eastern European markets.

**Management wants to explore:**
- Which countries and regions generate the highest sales and order volume
- How monthly sales trends changed between 2024 and 2025
- Which product categories have the highest return behavior
- Which areas may need deeper follow-up analysis

**Dataset Overview:**
- 1 row represents one customer order
- 15.000 rows and 13 columns
- Date range: 2024-2025

**Cleaning steps included:**
- Standardized categorical values into consistent formats
- Standardized date values into proper date format
- Replaced inconsistent missing values such as blanks, unknowns, and symbols with `NaN`
- Converted columns into appropriate data types
- Prepared cleaned fields for grouping and aggregation

**Exploratory Analysis:**
Key questions explored:
1. Which countries and sub-regions generate the highest sales and order volume?
2. How do monthly sales trends change over time across Europe?
3. Which product categories have the highest return rates?

**Key Findings:**
1. Germany generated the highest sales and order volume. Germany - Western Europe contributed the highest share of sales and orders.
    - Sales contribution: 17.94%
    - Order volume contribution: 17.24%
  
      <img width="577" height="291" alt="1" src="https://github.com/user-attachments/assets/5c6fd31c-fab9-4fe7-b8fe-b06ccae980d7" />

      <img width="548" height="289" alt="1 1" src="https://github.com/user-attachments/assets/0bb11870-ed2e-4db3-90bb-a85aa7871fe9" />

    This suggests that Germany is the strongest market in the dataset and may be an important country to monitor for sales performance.


2. Monthly sales showed a steady increase throughout 2024. However, sales performance declined during 2025. This pattern suggests that the business may need to investigate what changed in 2025, such as demand, discount strategy, customer behavior, product mix, or marketplace performance.

      <img width="322" height="477" alt="2" src="https://github.com/user-attachments/assets/40e61ad4-3c00-4158-9123-f651b3a12d9b" />

      <img width="838" height="283" alt="2 1" src="https://github.com/user-attachments/assets/1e6284e9-519e-4e11-b730-1f642ad307c9" />


3. Fashion had the highest return volume across 2024 and 2025. This may indicate issues related to sizing, customer expectations, product quality, or category-specific return behavior.

      <img width="282" height="176" alt="3" src="https://github.com/user-attachments/assets/c505e710-1698-4379-976b-e7ecfd546312" />


**Recommended Next Steps:**
1. Investigate the sales decline in 2025
    Analyze monthly sales by country, channel, and product category to understand which segments contributed most to the decline.
2. Review Fashion return behavior
    Explore Fashion returns by country, channel, discount level, and month to identify whether returns are concentrated in specific markets or sales conditions.
3. Compare sales performance by region
    Since Germany and Western Europe generated the strongest sales contribution, compare performance across Western, Southern, Northern, and Central & Eastern Europe to identify growth gaps.
4. Analyze discount impact
    Check whether higher discounts are associated with higher sales, lower sales, or higher return rates.
5. Add channel-level analysis
    Compare marketplace, website, and other sales channels to understand whether growth or returns are concentrated in specific channels.
    

**Project Outcome:**
This project demonstrates basic Python data analysis skills, including:
- data cleaning with pandas
- missing value handling
- data type conversion
- grouping and aggregation
- sales trend analysis
- return behavior analysis
- basic data visualization
