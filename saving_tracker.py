def calculate_interest(balance, annual_rate, days):
    return balance * (annual_rate / 100) * (days / 365)

deposit = 200
rate = 0.08

deposits = []

deposits.append(200)
deposits.append(50)
deposits.append(100)

print(deposits)

balance = sum(deposits)
print(f"Current balance: £{balance:.2f}")

interest = calculate_interest(deposit, 8, 4)

print(f"Interest after one year: £{interest:.2f}")
