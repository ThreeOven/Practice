def calculate_discount(price, discount_percentage):
   discount_amount = price * (discount_percentage / 100)
   final_price = price - discount_amount
   return final_price

print(calculate_discount(100, 30))  # Example usage: calculates the final price after a 20% discount on $100