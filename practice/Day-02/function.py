def total_expense(expenses, category=None):
    total = 0 # মোট খরচ জমানোর ভ্যারিয়েবল
    for e in expenses: # check each expense in the list
        # ক্যাটাগরি না দেওয়া থাকলে সব অথবা মিললে নির্দিষ্ট ক্যাটাগরির খরচ যোগ করো
        if category is None or e["category"] == category:
            total += e["amount"]
    return total

expenses = [
    {"title": "Rice", "amount": 120, "category": "food"},
    {"title": "Bus Ticket", "amount": 40, "category": "transportation"},
    {"title": "Tea", "amount": 20, "category": "food"},
]

print(total_expense(expenses))             
print(total_expense(expenses, "food"))     