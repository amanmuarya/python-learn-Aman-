# DAY 24 – PANDAS COMPLETE PRACTICE FILE

import pandas as pd


# 1. LOAD CSV FILE

df = pd.read_csv("E:\LEARN-PY\DATA ANALYTICS-14\Days Python Micro Course\day24_Employee_Data.csv")
# print("\n--- Raw Data ---")
# print(df.head())
# print("\n--- Output ---")



# print("\n--- Bootom 5 Rows ---")
# print(df.tail())



# # 2. BASIC INFORMATION

print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print(df.info())
print(df.describe())


# # 3. CLEAN TEXT DATA (VERY IMPORTANT)


# Clean Employee Names
# df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
# print(df.head())

# Clean City Names
# df["City"] = df["City"].str.strip().str.title()
# print(df.head())

# # Clean Department
# df["Department"] = df["Department"].str.strip().str.title()
# print(df.head())

# print("\n--- Cleaned Text Columns ---")
# print(df[["Employee_Name", "City", "Department"]].head())



# # 4. REMOVE DUPLICATES


# print("\nDuplicate Rows:", df.duplicated().sum())
# df = df.drop_duplicates()

# print(df)

# # 5. FILTER DATA


# # Employees from Mumbai
# df["City"] = df["City"].str.strip().str.title()
# mumbai_emp = df[df["City"] == "Mumbai"]
# # print(mumbai_emp)
# mumbai_emp.to_csv("Mumbai_emp.csv", index=False)



# # Employees with Salary > 60000
# high_salary = df[df["Salary"] > 60000]
# print(high_salary)


# print("\nEmployees from Mumbai:", mumbai_emp.shape[0])
# print("Employees with Salary > 60000:", high_salary.shape[0])


# # 6. SORT DATA

# Sort by Salary (Descending)
# df_sorted_salary = df.sort_values("Salary", ascending=False)
# print(df_sorted_salary.head())

# Sort by Joining Year
# df_sorted_year = df.sort_values("Joining_Year")
# print(df_sorted_year.head())


# # 7. ADD NEW COLUMNS

# # Salary Category
# df["Salary_Category"] = df["Salary"].apply(
#     lambda x: "High" if x >= 60000 else "Medium" if x >= 50000 else "Low"
# )
# print(df.head())

# Experience (Years)
# df["Experience"] = 2025 - df["Joining_Year"]
# print(df.head())



# # 8. GROUP BY OPERATIONS 

# # Average Salary by Department
# avg_salary_dept = df.groupby("Department")["Salary"].mean()
# print(avg_salary_dept)

# Total Salary by City
# df["City"] = df["City"].str.strip().str.title()
# total_salary_city = df.groupby("City")["Salary"].sum()
# print(total_salary_city)

# # Employee Count by Department
# count_dept = df.groupby("Department")["Employee_ID"].count()
# print(count_dept)




# # # # 9. EXPORT CLEANED DATA - Sort by Salary (Descending)
# df_sorted_salary = df.sort_values("Salary", ascending=False)
# # print(df_sorted_salary)
# df_sorted_salary.to_csv("employee_sorted_by_salary.csv", index=False)

