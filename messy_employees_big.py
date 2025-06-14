import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the excel data 
df = pd.read_excel("/Users/hitarthwadhwani/Desktop/practice_files/employee_data_dirty.xlsx")

#Dropping with null names
df = df.dropna(subset=["name"])
df["name"] = df["name"].str.title()

#Dropping duplicate rows
df.drop_duplicates(subset=["name", "department", "joining_date"], inplace=True)

#Filling Null salaries with mean
mean_salary = np.nanmean(df["salary"])
df["salary"] = df["salary"].fillna(mean_salary)
#Removing salary outliers
df = df[df["salary"] < 500000]

#Handling missing ages
df["age"] = df["age"].apply(lambda x: np.random.randint(25, 36) if pd.isna(x) else x)

#Converting joining_date to datetime
df["joining_date"] = pd.to_datetime(df["joining_date"], errors='coerce')

#Fill missing joining dates with random any date 
df["joining_date"] = df["joining_date"].apply(
    lambda x: pd.to_datetime(f"{np.random.randint(2015, 2021)}-01-01") if pd.isna(x) else x
)

#Dropping rows with missing departments
df = df.dropna(subset=["department"])
df["department"] = df["department"].str.title()

#Calculating experience in years
today = pd.to_datetime(datetime.today())
df["experience_years"] = (today - df["joining_date"]).dt.days // 365

df = df.reset_index(drop=True)

#Saving the Cleaned data 
df.to_csv("cleaned_employees_data.csv", index=False)

#Visualizing the Clean Data

plt.figure(figsize=(10, 5))
sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.close()

plt.figure(figsize=(10, 5))
sns.barplot(x="department", y="salary", data=df)
plt.title("Average Salary by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_salary_by_department.png")
plt.close()

plt.figure(figsize=(10, 5))
sns.scatterplot(x="experience_years", y="salary", data=df)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("experience_vs_salary.png")
plt.close()

plt.figure(figsize=(10, 5))
sns.countplot(x="department", data=df)
plt.title("Employee Count per Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("employee_count_by_department.png")
plt.close()

