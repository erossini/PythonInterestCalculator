def calculate_interest(balance, annual_rate, days):
    return balance * (annual_rate / 100) * (days / 365)

deposit = 200
rate = 0.08

interest = calculate_interest(deposit, 8, 4)

print(f"Interest after one year: £{interest:.2f}")
