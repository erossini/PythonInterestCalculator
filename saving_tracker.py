from datetime import datetime

ANNUAL_RATE = 8


def get_valid_amount():
    """Prompt the user until a valid deposit amount is entered."""

    while True:

        try:
            amount = float(
                input("Deposit amount (£): ")
            )

            if amount <= 0:
                print(
                    "❌ Amount must be greater than zero."
                )
                continue

            return amount

        except ValueError:
            print(
                "❌ Please enter a valid number."
            )


def get_valid_date():
    """Prompt the user until a valid date is entered."""

    use_today = input(
        "Use today's date? (y/n): "
    ).strip().lower()

    if use_today == "y":
        return datetime.today().strftime(
            "%Y-%m-%d"
        )

    while True:

        date_str = input(
            "Deposit date (YYYY-MM-DD): "
        ).strip()

        try:

            deposit_date = datetime.strptime(
                date_str,
                "%Y-%m-%d"
            )

            if deposit_date > datetime.today():

                print(
                    "❌ Deposit date cannot "
                    "be in the future."
                )

                continue

            return date_str

        except ValueError:

            print(
                "❌ Invalid date format. "
                "Please use YYYY-MM-DD."
            )


def calculate_interest(
    amount,
    annual_rate,
    deposit_date
):
    """Calculate simple interest earned to date."""

    deposit_datetime = datetime.strptime(
        deposit_date,
        "%Y-%m-%d"
    )

    days = (
        datetime.today() - deposit_datetime
    ).days

    interest = (
        amount
        * (annual_rate / 100)
        * (days / 365)
    )

    return interest


def add_deposit(deposits):

    amount = get_valid_amount()
    date = get_valid_date()

    deposits.append({
        "amount": amount,
        "date": date
    })

    print("\n✅ Deposit added successfully.")


def view_balance(deposits):

    balance = sum(
        deposit["amount"]
        for deposit in deposits
    )

    print(
        f"\nCurrent Balance: "
        f"£{balance:.2f}"
    )


def view_interest(deposits):

    total_interest = 0

    for deposit in deposits:

        total_interest += calculate_interest(
            deposit["amount"],
            ANNUAL_RATE,
            deposit["date"]
        )

    print(
        f"\nEstimated Interest: "
        f"£{total_interest:.2f}"
    )


def view_deposits(deposits):

    if not deposits:

        print(
            "\nNo deposits recorded yet."
        )

        return

    print("\nDeposits")

    print("-" * 30)

    for index, deposit in enumerate(
        deposits,
        start=1
    ):

        print(
            f"{index}. "
            f"£{deposit['amount']:.2f} "
            f"on {deposit['date']}"
        )


def main():

    deposits = []

    while True:

        print("\n=== Savings Tracker ===")

        print("1. Add Deposit")
        print("2. View Deposits")
        print("3. View Balance")
        print("4. View Interest")
        print("5. Exit")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":

            add_deposit(deposits)

        elif choice == "2":

            view_deposits(deposits)

        elif choice == "3":

            view_balance(deposits)

        elif choice == "4":

            view_interest(deposits)

        elif choice == "5":

            print(
                "\nThank you for using "
                "Savings Tracker!"
            )

            break

        else:

            print(
                "\n❌ Invalidoption."
            )


if __name__ == "__main__":
    main()