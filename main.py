"""Budget Tracker CLI - Personal budget tracker."""
import json, os
from datetime import datetime

DATA_FILE = "budget.json"

def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"transactions": []}

def save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(data, amount, category, note=""):
    data["transactions"].append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "note": note
    })
    save(data)
    print(f"Added: {'Income' if amount > 0 else 'Expense'} ${abs(amount):.2f} [{category}]")

def report(data):
    txns = data["transactions"]
    if not txns:
        print("No transactions yet."); return
    total = sum(t["amount"] for t in txns)
    income = sum(t["amount"] for t in txns if t["amount"] > 0)
    expense = sum(t["amount"] for t in txns if t["amount"] < 0)
    print(f"\n{'='*35}")
    print(f" Total Income : ${income:.2f}")
    print(f" Total Expense: ${abs(expense):.2f}")
    print(f" Net Balance  : ${total:.2f}")
    print(f"{'='*35}")
    for t in txns[-5:]:
        sign = "+" if t["amount"] > 0 else ""
        print(f" {t['date']} | {sign}{t['amount']:.2f} | {t['category']} | {t['note']}")

def main():
    data = load()
    while True:
        print("\n[1] Add Income  [2] Add Expense  [3] Report  [4] Quit")
        c = input("> ").strip()
        if c == "1":
            amt = float(input("Amount: "))
            cat = input("Category: ")
            add(data, abs(amt), cat)
        elif c == "2":
            amt = float(input("Amount: "))
            cat = input("Category: ")
            add(data, -abs(amt), cat)
        elif c == "3":
            report(data)
        elif c == "4":
            break

if __name__ == "__main__":
    main()
