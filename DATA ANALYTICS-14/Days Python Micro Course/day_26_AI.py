import pandas as pd
from datetime import datetime

# Load CSV
df = pd.read_csv("E:\LEARN-PY\DATA ANALYTICS-14\Days Python Micro Course\day24_Employee_Data.csv")

# 1. Clean names and cities (trim spaces, proper-case)
# df['Employee_Name'] = df['Employee_Name'].astype(str).str.strip().str.title()
# df['City'] = df['City'].astype(str).str.strip().str.title()


# # 2. Remove duplicates based on Employee_ID (or entire row)
df = df.drop_duplicates(subset=['Department'], keep='first')
print(df)

# 3. Add Experience column (current_year - joining_year)
# current_year = datetime.now().year
# df['Experience'] = current_year - df['Joining_Year'].astype(int)

# print(df)

# # Display cleaned data
# print(df.head())

# # Save cleaned file (optional)
# df.to_csv("day24_Employee_Data_Cleaned.csv", index=False)