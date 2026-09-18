Complete Smart Student Expense Manager project
# Smart Student Expense Manager – Python Mini Project

## Project Overview
Smart Student Expense Manager is a console-based Python mini project designed for students to record expenses, manage a monthly budget and receive simple rule-based spending insights.

It is a different project from the Banking System while following the same internship requirement of combining Python concepts into one functional application.

## Main Features
- Create/update student profile
- Automatically generate a student ID using `random`
- Set monthly budget
- Add expenses
- Store date and time using `datetime`
- View complete expense history
- Calculate total spending
- Calculate category-wise spending
- Search expenses by category
- Compare spending with monthly budget
- Smart spending insights using simple rule-based analysis
- Save data locally using JSON

## Python Concepts Used
- Variables and data types
- Input/output
- `if/elif/else`
- `while` loops
- Lists
- Dictionaries
- String operations
- Functions
- File handling
- JSON
- Modules:
  - `random` → student ID generation
  - `datetime` → expense date/time
  - `pathlib` → file management

## AI Connection
The project includes a small **rule-based smart insight module**. It analyzes recorded expenses and identifies the highest spending category, its percentage of total spending and budget alerts.

This is an educational AI-style decision system, not a machine-learning model or online generative AI system.

## How to Run

Install Python 3.9 or newer.

Open the project folder in VS Code and run:

```bash
python main.py
```

No external packages are required.

## Suggested Demo
1. Create a student profile.
2. Set a monthly budget such as ₹5000.
3. Add Food, Travel and Study expenses.
4. View expense history.
5. View spending summary.
6. Run Smart Spending Insights.
7. Search for a category such as Food.
8. Restart the program and verify that saved data remains.

## Project Flow
```text
START
  |
  v
MAIN MENU
  |
  +--> Student Profile
  |
  +--> Set Budget
  |
  +--> Add Expense
  |
  +--> View History
  |
  +--> Spending Summary
  |
  +--> Smart Insights
  |
  +--> Search Category
  |
  v
EXIT
```

## GitHub Submission
Recommended repository name:

`smart-student-expense-manager`

Recommended description:

`Python mini project for student expense tracking, budgeting and rule-based smart spending insights.`

Before submitting the GitHub URL:
- Make the repository public if the internship requires the evaluator to access it.
- Test the program.
- Upload `main.py`, `README.md`, `PROJECT_REPORT.md`, `requirements.txt`, `.gitignore` and `LICENSE`.
- Do not upload `expense_data.json` if it contains personal information.
- Open the GitHub URL in an incognito/private browser window to verify that it is accessible.

## Educational Note
This project is for learning and internship evaluation. It is not intended to provide financial advice or manage real financial accounts.
