def summarize_sales(sales):
    total = sum(sales)
    avg = round(total / len(sales), 2) if sales else 0
    return {"total": total, "average": avg}

def apply_tax(amount, rate=0.0625):
    return round(amount * (1 + rate), 2)
