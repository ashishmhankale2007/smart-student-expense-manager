"""
Smart Student Expense Manager
Python Mini Project

Educational project demonstrating:
- Variables, conditions, loops
- Lists and dictionaries
- Functions
- String operations and validation
- random and datetime modules
- JSON file handling
- Simple rule-based "AI-style" spending insights
"""

import json
import random
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expense_data.json")


def load_data():
    if not DATA_FILE.exists():
        return {"profile": {}, "expenses": [], "budget": 0.0}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Saved data could not be read. Starting fresh.")
        return {"profile": {}, "expenses": [], "budget": 0.0}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def create_profile(data):
    print("\n========== CREATE PROFILE ==========")
    name = input("Enter student name: ").strip()
    course = input("Enter course/branch: ").strip()

    if len(name) < 2 or len(course) < 2:
        print("Please enter valid details.")
        return

    student_id = "STD" + str(random.randint(1000, 9999))
    data["profile"] = {
        "student_id": student_id,
        "name": name,
        "course": course
    }
    save_data(data)

    print("\nProfile created successfully!")
    print("Student ID:", student_id)


def add_expense(data):
    print("\n========== ADD EXPENSE ==========")

    category = input(
        "Category (Food/Travel/Study/Shopping/Other): "
    ).strip().title()

    try:
        amount = float(input("Enter amount: ₹").strip())
    except ValueError:
        print("Enter a valid numeric amount.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    note = input("Enter short note: ").strip()

    expense = {
        "date_time": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "category": category,
        "amount": round(amount, 2),
        "note": note
    }

    data["expenses"].append(expense)
    save_data(data)

    print(f"₹{amount:.2f} expense added successfully.")


def set_budget(data):
    print("\n========== SET MONTHLY BUDGET ==========")

    try:
        budget = float(input("Enter monthly budget: ₹").strip())
    except ValueError:
        print("Enter a valid amount.")
        return

    if budget <= 0:
        print("Budget must be greater than zero.")
        return

    data["budget"] = round(budget, 2)
    save_data(data)
    print(f"Monthly budget set to ₹{budget:.2f}.")


def show_expenses(data):
    print("\n========== EXPENSE HISTORY ==========")

    expenses = data["expenses"]
    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['date_time']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['note']}"
        )


def calculate_summary(data):
    expenses = data["expenses"]
    total = sum(item["amount"] for item in expenses)

    categories = {}
    for item in expenses:
        category = item["category"]
        categories[category] = categories.get(category, 0) + item["amount"]

    return total, categories


def show_summary(data):
    print("\n========== SPENDING SUMMARY ==========")

    total, categories = calculate_summary(data)

    print(f"Total Spending: ₹{total:.2f}")

    if data["budget"] > 0:
        remaining = data["budget"] - total
        print(f"Monthly Budget: ₹{data['budget']:.2f}")
        print(f"Remaining: ₹{remaining:.2f}")

        if remaining < 0:
            print("Status: Budget exceeded.")
        else:
            print("Status: Within budget.")

    print("\nCategory-wise spending:")
    if not categories:
        print("No category data available.")
    else:
        for category, amount in sorted(
            categories.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"- {category}: ₹{amount:.2f}")


def smart_insights(data):
    """
    Simple rule-based AI-style analysis.
    It identifies the highest spending category and budget condition.
    """
    print("\n========== SMART SPENDING INSIGHTS ==========")

    total, categories = calculate_summary(data)

    if total == 0:
        print("No spending data yet. Add some expenses to receive insights.")
        return

    highest_category = max(categories, key=categories.get)
    highest_amount = categories[highest_category]
    percentage = (highest_amount / total) * 100

    print(
        f"Highest spending category: {highest_category} "
        f"({percentage:.1f}% of total spending)."
    )

    if percentage >= 50:
        print(
            f"Insight: More than half of your recorded spending is in "
            f"{highest_category}. Review this category first."
        )
    elif percentage >= 30:
        print(
            f"Insight: {highest_category} is a major spending category. "
            "Consider monitoring it regularly."
        )
    else:
        print("Insight: Your spending is distributed across categories.")

    if data["budget"] > 0:
        remaining = data["budget"] - total
        if remaining < 0:
            print(
                f"Alert: You are ₹{abs(remaining):.2f} over the current budget."
            )
        elif remaining <= data["budget"] * 0.20:
            print(
                f"Alert: Only ₹{remaining:.2f} remains in the current budget."
            )
        else:
            print("Budget insight: Spending is currently within a comfortable range.")


def search_category(data):
    print("\n========== SEARCH BY CATEGORY ==========")
    keyword = input("Enter category to search: ").strip().lower()

    found = [
        item for item in data["expenses"]
        if keyword in item["category"].lower()
    ]

    if not found:
        print("No matching expenses found.")
        return

    total = 0
    for item in found:
        total += item["amount"]
        print(
            f"{item['date_time']} | {item['category']} | "
            f"₹{item['amount']:.2f} | {item['note']}"
        )

    print(f"\nCategory total: ₹{total:.2f}")


def main():
    data = load_data()

    while True:
        print("\n")
        print("==============================================")
        print("       SMART STUDENT EXPENSE MANAGER")
        print("==============================================")
        print("1. Create / Update Student Profile")
        print("2. Set Monthly Budget")
        print("3. Add Expense")
        print("4. View Expense History")
        print("5. View Spending Summary")
        print("6. Smart Spending Insights")
        print("7. Search Expenses by Category")
        print("8. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            create_profile(data)
        elif choice == "2":
            set_budget(data)
        elif choice == "3":
            add_expense(data)
        elif choice == "4":
            show_expenses(data)
        elif choice == "5":
            show_summary(data)
        elif choice == "6":
            smart_insights(data)
        elif choice == "7":
            search_category(data)
        elif choice == "8":
            print("Thank you for using Smart Student Expense Manager!")
            break
        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
