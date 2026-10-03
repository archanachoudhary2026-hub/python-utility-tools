def calculate_total(prices):
    total_bill = sum(prices)
    return total_bill

def apply_tax(amount,tax=5):
    final_amount = amount+(amount*(tax/100))
    return final_amount

