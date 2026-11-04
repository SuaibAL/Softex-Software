expense = {"title": "Rice", "amount": 120, "category": "food"}

print(expense["amount"])           # 120
print(expense.get("note", "N/A"))   # key না থাকলে error না দিয়ে default দেয়
expense["amount"] = 150            # update
expense["date"] = "2026-11-01"     # নতুন key

for key, value in expense.items():
    print(key, "→", value)