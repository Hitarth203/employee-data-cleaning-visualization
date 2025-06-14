# Employee Data Cleaning & Visualization Project

Hi! This is a small project I worked on to practice **real-world data cleaning and analysis** using Python. I was given a messy dataset of over 250 employee records, and the goal was to clean it up and draw some useful insights using **Pandas, NumPy, Matplotlib, and Seaborn**.

---

## What this project is about

- The dataset had **missing values, inconsistent text formats, wrong date formats**, and even some unrealistic salary values.
- I cleaned the data step-by-step using pandas and also handled missing ages using random values.
- Then, I used **visualizations** to show things like salary distribution, average salary by department, employee count by department, and how experience affects salary.

---

## Tools Used

- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn  
- Excel (`.xlsx`) file reading using openpyxl

---

## What I did (Cleaning Steps)

- Removed rows with missing names or departments  
- Standardized text (like converting names and departments to title case)  
- Removed duplicate records  
- Fixed and converted joining dates to proper datetime format  
- Filled missing salary values with the average salary  
- Removed rows where salary was more than 5 lakhs (outlier filtering)  
- Filled missing age values randomly between 25 and 35  
- Calculated each employee’s **experience in years** from their joining date  

---

## Visualizations Included

These plots were created using Matplotlib and Seaborn and saved as image files:

1. **Salary Distribution** – A histogram showing how salaries are spread  
2. **Average Salary by Department** – Bar chart  
3. **Experience vs Salary** – Scatter plot to see any trend  
4. **Employee Count by Department** – Count plot for department-wise analysis

---

## Files in the Repo

- `messy_employees_big.xlsx` – Raw Excel file (optional to include on GitHub)  
- `cleaned_employees_big.csv` – Final cleaned dataset  
- `clean_employees_analysis.py` – Full Python script for data cleaning and visualization  
- 4 PNG files – Saved plots from the analysis  

---

## What I learned

- How to clean and preprocess data properly using Pandas  
- Handling real-life issues like NaNs, wrong data formats, and text inconsistencies  
- Creating meaningful visualizations from cleaned data  
- Writing Python scripts that can be reused or shared with others  

---

## About Me

I'm currently a BCA student specializing in AI & Machine Learning.  
This project helped me improve my skills in **data cleaning, analysis, and visualization** — key areas in data science.

Feel free to connect with me on [LinkedIn](https://linkedin.com/in/hitarth-wadhwani)!

---

