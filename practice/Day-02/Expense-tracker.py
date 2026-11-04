def category_summary(expenses):
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]
        return summary
expenses = [
    {"title": "ভাত", "amount": 120, "category": "food"},
    {"title": "রিকশা", "amount": 40, "category": "transportation"},
    {"title": "চা", "amount": 20, "category": "food"},
    {"title": "বাস ভাড়া", "amount": 50, "category": "transportation"}
]

for cat, total in category_summary(expenses).items():
    print(f"{cat}: {total} Taka")