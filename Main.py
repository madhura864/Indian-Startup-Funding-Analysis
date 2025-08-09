import pandas as pd
df=pd.read_csv('/content/startup_funding.csv')
display(df.head())


# Funding trend plot - using funding_by_month from previous cell
plt.figure(figsize=(10,6))
sns.lineplot(data=funding_by_month, x='year_month', y='total_funding')
plt.title("Funding Trend Over Time (Monthly)")
plt.xlabel("Date")
plt.ylabel("Amount in USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top sectors plot - using top_sectors_count from previous cell
plt.figure(figsize=(8, 5))
sns.barplot(x=top_sectors_count.values, y=top_sectors_count.index, palette='viridis')
plt.title("Top Sectors by Number of Fundings")
plt.xlabel("Number of Startups")
plt.ylabel("Industry Vertical")
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data and perform initial cleaning
df = pd.read_csv('/content/startup_funding.csv')

# Strip whitespace from column names
df.columns = df.columns.str.strip()

df.rename(columns={'Date dd/mm/yyyy': 'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)
df = df.dropna(subset=['Date'])
df['Amount in USD'] = df['Amount in USD'].replace('[\$,]', '', regex=True)

# Ensure 'City' and other text columns exist and handle potential missing values
text_cols = ['City', 'Location', 'Startup Name', 'Investors Name', 'InvestmentnType']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown').astype(str)
    else:
        # Handle case where column might be missing entirely if necessary
        print(f"Warning: Column '{col}' not found in the DataFrame.")

df['amount_numeric'] = pd.to_numeric(df['Amount in USD'], errors='coerce')


# Data processing for Active investors (by count of deals)
top_investors_count = df['Investors Name'].value_counts().head(20)

# Convert top_investors_count Series to a pandas DataFrame for easier plotting
top_investors_df = pd.DataFrame({
    'Investor Name': top_investors_count.index,
    'Number of Investments': top_investors_count.values
})


plt.figure(figsize=(12, 6)) # Increased figure size for better readability
sns.barplot(x='Number of Investments', y='Investor Name', data=top_investors_df, palette='viridis') # Swapped x and y for horizontal bar plot
plt.title("Top 20 Investors by Number of Investments") # Updated title to reflect top 20
plt.xlabel("Number of Investments")
plt.ylabel("Investor Name")
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels
plt.tight_layout()
plt.show()