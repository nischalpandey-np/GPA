📘 NEB GPA Calculator (Grade 12 – 2082)
This is a command-line Python program to calculate the final GPA for Grade 12 students under the National Examination Board (NEB) of Nepal. It allows students to enter their scores either as GPA or raw marks, processes them based on a weighted credit system, and outputs both individual subject GPAs and the final cumulative GPA.

✅ Features
Supports 6 subjects: English, Nepali, Mathematics, Physics, Chemistry, and Computer Science

Handles credit distribution between theory and internal/practical components

Allows user to input scores as either:

GPA (Grade Point) – e.g., 3.6

Raw marks – e.g., 60 out of 75

Converts raw marks into GPA using NEB’s percentage-to-GPA scale

Calculates:

Theory GPA

Internal/Practical GPA

Weighted Subject GPA

Final GPA based on total credits

Presents results in a clean, tabulated format using the tabulate module

📊 GPA Scale (Based on Percentage)
Percentage Range	GPA
90–100%	4.0
80–89%	3.6
70–79%	3.2
60–69%	2.8
50–59%	2.4
40–49%	2.0
35–39%	1.6
Below 35%	0.0
📦 Requirements
Python 3.x

tabulate library (install using pip install tabulate)

🚀 How to Use
Run the script:

bash
Copy
Edit
python gpa_calculator.py
Choose your input method:

1 for GPA input

2 for Raw Marks input

Enter theory and internal/practical scores for each subject.

View the detailed GPA breakdown and your final GPA.

🧮 Calculation Logic
Each subject has different credit allocations for theory and internal/practical. The final GPA for each subject is calculated as a weighted average:

Subject GPA
=
(
Theory GPA
×
Theory Credits
)
+
(
Internal GPA
×
Internal Credits
)
Total Credits
Subject GPA= 
Total Credits
(Theory GPA×Theory Credits)+(Internal GPA×Internal Credits)
​
 
The final GPA is calculated as:

Final GPA
=
∑
(
Subject GPA
×
Subject Credits
)
Total Credit Hours
Final GPA= 
Total Credit Hours
∑(Subject GPA×Subject Credits)
​
 
📘 Example Output
text
Copy
Edit
=== GPA Summary Table ===
╒════════════════════╤═════════════════════════╤══════════════╤══════════════╕
│ Subject            │ Internal/Practical GPA  │ Theory GPA   │ Overall GPA  │
╞════════════════════╪═════════════════════════╪══════════════╪══════════════╡
│ English            │ 3.60                    │ 3.20         │ 3.30         │
│ Computer Science   │ 4.00                    │ 3.60         │ 3.72         │
│ ...                │ ...                     │ ...          │ ...          │
╘════════════════════╧═════════════════════════╧══════════════╧══════════════╛

=== Final Result ===
Total Credit Hours: 27
Total (Credit × Grade Point): 92.16
🎓 Your Final GPA: 3.41
🧠 Ideal For
NEB Grade 12 Students

Teachers & Academic Institutions

GPA prediction & analysis tools

