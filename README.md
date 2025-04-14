# 🎓 NEB GPA Calculator (Grade 12 – 2082)

A command-line Python program to calculate the final GPA for **Grade 12 students under the NEB (National Examination Board), Nepal**. It supports GPA or raw marks input and outputs your GPA breakdown with final GPA based on subject credit weight.

---

## ✅ Features

- Covers 6 major NEB subjects:
  - English
  - Nepali
  - Mathematics
  - Physics
  - Chemistry
  - Computer Science
- Input options:
  - GPA (e.g., 3.6 for A)
  - Raw Marks (e.g., 60 out of 75)
- Converts marks to GPA using NEB percentage scale
- Calculates:
  - Internal/Practical GPA
  - Theory GPA
  - Weighted Subject GPA
  - Final GPA (Credit-based)
- Clean tabulated results using the `tabulate` module

---

## 📊 GPA Scale (Based on Percentage)

| Percentage Range | GPA |
|------------------|-----|
| 90–100%          | 4.0 |
| 80–89%           | 3.6 |
| 70–79%           | 3.2 |
| 60–69%           | 2.8 |
| 50–59%           | 2.4 |
| 40–49%           | 2.0 |
| 35–39%           | 1.6 |
| Below 35%        | 0.0 |

---

## 📦 Requirements

- Python 3.x
- `tabulate` module  
  Install with:
  ```bash
  pip install tabulate
  ```

---

## 🚀 How to Run

1. Clone/download the script.
2. Open terminal or command prompt.
3. Run the program:
   ```bash
   python gpa_calculator.py
   ```
4. Select input type:
   - `1` for GPA
   - `2` for Marks
5. Enter theory and internal/practical scores for each subject.
6. Get your final GPA with a detailed subject-wise summary.

---

## 🧮 How GPA is Calculated

Each subject has a specific credit split between theory and internal/practical. Final GPA per subject is calculated using:

```
Subject GPA = 
((Theory GPA × Theory Credits) + (Internal GPA × Internal Credits)) / Total Credits
```

Then your overall GPA is calculated using:

```
Final GPA = Total of (Subject GPA × Subject Credits) / Total Credit Hours
```

---

## 📘 Sample Output

```
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
```

---

## 🧠 Ideal For

- NEB Grade 12 Students
- Teachers & Schools
- GPA estimation tools
- Final exam preparation

---

## 📄 License

This project is free to use and modify for educational purposes.

---

## 💡 Suggestions or Contributions?

Pull requests, feature suggestions, or improvements are always welcome!

---
```
