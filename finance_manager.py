import datetime

class PersonalFinanceManager:
    def __init__(self):
        self.records = {"income": [], "expenses": []}

    def run(self):
        print("Welcome to the Personal Finance Manager!")
        while True:
            action = input("\nChoose an action: (1) Add Income (2) Add Expense (3) View Records (4) View Balance (5) Exit\n")

            if action == '1':
                amount = float(input("Enter income amount: "))
                source = input("Enter income source: ")
                date = input("Enter date (YYYY-MM-DD) or press Enter for today: ") or datetime.datetime.now().strftime("%Y-%m-%d")
                self.records["income"].append({"amount": amount, "source": source, "date": date})
                print(f"Income of {amount} added from {source} on {date}.")

            elif action == '2':
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                description = input("Enter description: ")
                date = input("Enter date (YYYY-MM-DD) or press Enter for today: ") or datetime.datetime.now().strftime("%Y-%m-%d")
                self.records["expenses"].append({"amount": amount, "category": category, "description": description, "date": date})
                print(f"Expense of {amount} added for {category}: {description} on {date}.")

            elif action == '3':
                print("\n--- Income Records ---")
                total_income = sum(item["amount"] for item in self.records["income"])
                if total_income == 0:
                    print("No income records found.")
                else:
                    for item in self.records["income"]:
                        print(f"Date: {item['date']}, Amount: {item['amount']}, Source: {item['source']}")
                print(f"Total Income: {total_income}\n")

                print("\n--- Expense Records ---")
                total_expenses = sum(item["amount"] for item in self.records["expenses"])
                if total_expenses == 0:
                    print("No expense records found.")
                else:
                    for item in self.records["expenses"]:
                        print(f"Date: {item['date']}, Amount: {item['amount']}, Category: {item['category']}, Description: {item['description']}")
                print(f"Total Expenses: {total_expenses}\n")

            elif action == '4':
                total_income = sum(item["amount"] for item in self.records["income"])
                total_expenses = sum(item["amount"] for item in self.records["expenses"])
                balance = total_income - total_expenses
                print(f"\nCurrent Balance: {balance}\n")

            elif action == '5':
                print("Exiting the Personal Finance Manager. See you soon, Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")

# Run the manager
# Run the manager
if __name__ == "__main__":
    finance_manager = PersonalFinanceManager()
    finance_manager.run()
