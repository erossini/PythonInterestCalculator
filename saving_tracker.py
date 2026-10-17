from datetime import datetime

ANNUAL_RATE = 8

deposits = []

while True:

    print("\nSavings Tracker")
    print("1. Add deposit")
    print("2. View balance")
    print("3. View interest")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        amount = float(input("Deposit amount: £"))

        use_today = input(
            "Use today's date? (y/n): "
        ).lower()

        if use_today == "y":

            date = datetime.today().strftime("%Y-%m-%d")

        else:

            while True:

                date = input(
                    "Deposit date (YYYY-MM-DD): "
                )

                try:

                    datetime.strptime(
                        date,
                        "%Y-%m-%d"
                    )

                    break

                except ValueError:

                    print(
                        "Invalid date. Please use "
                        "the format YYYY-MM-DD."
                    )

        deposits.append({
            "amount": amount,
            "date": date
        })

        print("Deposit added successfully.")

    elif choice == "2":

        balance = sum(d["amount"] for d in deposits)

        print(f"Balance: £{balance:.2f}")

    elif choice == "3":

        total_interest = 0

        for deposit in deposits:

            deposit_date = datetime.strptime(
                deposit["date"],
                "%Y-%m-%d"
            )

            days = (
                datetime.today() - deposit_date
            ).days

            interest = (
                deposit["amount"]
                * (ANNUAL_RATE / 100)
                * (days / 365)
            )

            total_interest += interest

        print(f"Estimated interest: £{total_interest:.2f}")

    elif choice == "4":

        print("Goodbye!")
        break