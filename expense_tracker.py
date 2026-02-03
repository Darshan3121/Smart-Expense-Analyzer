import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


FILE_NAME = "expenses.csv"

# Create CSV file with header if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

# Add a new expense
def add_expense():
    print("\n=== Add New Expense ===")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!")

# View all expenses and total
def view_expenses():
    print("\n=== All Expenses ===")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}")
            total += float(row[2])

    print(f"\n💰 Total Spending: ₹{total}")
# Analyze expenses
def analyze_expenses():
    print("\n=== Expense Analysis ===")

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No expenses to analyze.")
        return

    category_sum = df.groupby("Category")["Amount"].sum()

    print("\n📊 Category-wise Spending:")
    for category, amount in category_sum.items():
        print(f"{category}: ₹{amount}")

    print(f"\n🔥 Highest Spending Category: {category_sum.idxmax()}")

# Budget alert system
def budget_alert():
    print("\n=== Budget Alerts ===")

    budgets = {
        "Food": 3000,
        "Travel": 2000,
        "Shopping": 2500
    }

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No expenses to analyze.")
        return

    category_sum = df.groupby("Category")["Amount"].sum()

    for category, spent in category_sum.items():
        if category in budgets:
            if spent > budgets[category]:
                extra = spent - budgets[category]
                print(f"⚠️ {category} budget exceeded by ₹{extra}")
            else:
                print(f"✅ {category} is within budget")
# Show expense charts
def show_charts():
    print("\n=== Expense Charts ===")

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No data to display.")
        return

    category_sum = df.groupby("Category")["Amount"].sum()

    # Bar chart
    category_sum.plot(kind="bar")
    plt.title("Category-wise Expense")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.tight_layout()
    plt.show()

    # Pie chart
    category_sum.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# Main menu
def main_menu():
    initialize_file()

    while True:
        print("\n===== Smart Expense Analyzer =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Budget Alerts")
        print("5. Show Charts")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            budget_alert()
        elif choice == "5":
            show_charts()    
        elif choice == "6":
                print("👋 Exiting program. Goodbye!")
                break
        else:
            print("❌ Invalid choice. Try again.")
main_menu()

