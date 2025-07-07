'''  
@author: 22000409 Kaushal Ramoliya  
@description: 18. - Write a program in Python for calculating conditional probability for following data in CSV 
file. The input columns are light blue coloured, remaining are calculative.
'''  
import pandas as pd

# Step 1: Load Excel file
df = pd.read_excel("Program_18_excel.xlsx")  # replace with your file name

# Step 2: Debug - Show column names
print("Original columns:", df.columns.tolist())

# Step 3: Rename columns safely
df = df.rename(columns={
    df.columns[1]: "Job",
    df.columns[3]: "Python",
    df.columns[5]: "Both"
})

# Step 4: Total number of students (as per your table structure)
total_students = 50

# Step 5: Perform calculations
df["P(Job)"] = df["Job"] / total_students
df["P(Py)"] = df["Python"] / total_students
df["P(job^py)"] = df["Both"] / total_students
df["Conp(Py|Job)"] = df["P(job^py)"] / df["P(Job)"]
df["Conp(Job|Py)"] = df["P(job^py)"] / df["P(Py)"]  # 🔧 FIXED LINE

# Step 6: Save output to Excel
output_file = "Program_18_excel_output.xlsx"
df.to_excel(output_file, index=False)

print(f"Output saved to {output_file}")
