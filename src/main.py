# banking_app_python/src/main.py
from src.bank import Bank
from src.io import (
    clear_screen,
    get_input_float,
    get_input_int,
    get_input_string,
    press_enter_to_continue,
)


def main():
    """Main function to run the banking application."""
    bank = Bank()

    while True:
        clear_screen()
        print("------------------------------------")
        print("  Python Terminal Banking System")
        print("------------------------------------")
        print("1. Create New Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Transfer Funds")
        print("5. Check Account Balance")
        print("6. List All Accounts")
        print("7. Delete Accounts")
        print("8. Export Data")
        print("9. Exit")
        print("------------------------------------")

        choice = get_input_int("Enter your choice: ")

        if choice == 1:
            create_account_menu(bank)
        elif choice == 2:
            deposit_menu(bank)
        elif choice == 3:
            withdraw_menu(bank)
        elif choice == 4:
            transfer_menu(bank)
        elif choice == 5:
            check_balance_menu(bank)
        elif choice == 6:
            list_all_accounts_menu(bank)
        elif choice == 7:
            delete_account_menu(bank)
        elif choice == 8:
            export_data_menu(bank)
        elif choice == 9:
            print("Exiting banking system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")
            press_enter_to_continue()


# --- Menu Handlers ---


def create_account_menu(bank: Bank) -> None:
    """Handles the create account menu option."""
    clear_screen()
    print("--- Create New Account ---")
    owner_name = get_input_string("Enter account owner name: ")
    bank.create_account(owner_name)
    press_enter_to_continue()


def deposit_menu(bank: Bank) -> None:
    """Handles the deposit funds menu option."""
    clear_screen()
    print("--- Deposit Funds ---")
    account_number = get_input_int("Enter account number: ")
    if account_number is None:
        print("Invalid account number.")
        press_enter_to_continue()
        return

    amount = get_input_float("Enter amount to deposit: $")
    if amount is None:
        print("Invalid amount.")
        press_enter_to_continue()
        return

    try:
        new_balance = bank.deposit(account_number, amount)
        print(
            f"Successfully deposited ${amount:.2f} into account {account_number}. "
            f"New balance: ${new_balance:.2f}"
        )
    except ValueError as e:
        print(f"Error: {e}")
    
    press_enter_to_continue()


def withdraw_menu(bank: Bank) -> None:
    """Handles the withdraw funds menu option."""
    clear_screen()
    print("--- Withdraw Funds ---")
    account_number = get_input_int("Enter account number: ")
    if account_number is None:
        print("Invalid account number.")
        press_enter_to_continue()
        return

    amount = get_input_float("Enter amount to withdraw: $")
    if amount is None:
        print("Invalid amount.")
        press_enter_to_continue()
        return

    try:
        new_balance = bank.withdraw(account_number, amount)
        print(
            f"Successfully withdrew ${amount:.2f} from account {account_number}. "
            f"New balance: ${new_balance:.2f}"
        )
    except ValueError as e:
        print(f"Error: {e}")
    press_enter_to_continue()


def transfer_menu(bank: Bank) -> None:
    """Handles the transfer funds menu option."""
    clear_screen()
    print("--- Transfer Funds ---")
    from_account = get_input_int("Enter source account number: ")
    if from_account is None:
        print("Invalid source account number.")
        press_enter_to_continue()
        return

    to_account = get_input_int("Enter destination account number: ")
    if to_account is None:
        print("Invalid destination account number.")
        press_enter_to_continue()
        return

    amount = get_input_float("Enter amount to transfer: $")
    if amount is None:
        print("Invalid amount.")
        press_enter_to_continue()
        return

    try:
        bank.transfer(from_account, to_account, amount)
        print(
            f"Successfully transferred ${amount:.2f} from account {from_account} "
            f"to account {to_account}."
        )
    except ValueError as e:
        print(f"Error: {e}")
    press_enter_to_continue()


def check_balance_menu(bank: Bank) -> None:
    """Handles the check balance menu option."""
    clear_screen()
    print("--- Check Account Balance ---")
    account_number = get_input_int("Enter account number: ")
    if account_number is None:
        print("Invalid account number.")
        press_enter_to_continue()
        return
    bank.check_balance(account_number)
    press_enter_to_continue()


def list_all_accounts_menu(bank: Bank) -> None:
    """Handles the list all accounts menu option."""
    clear_screen()
    print("--- List All Accounts ---")
    bank.list_all_accounts()
    press_enter_to_continue()


def delete_account_menu(bank: Bank) -> None:
    num = int(input("Enter the Account number"))
    Bank._delete_accounts(bank, num)
    press_enter_to_continue()

def export_data_menu(bank:Bank)->None:
    Bank._export_data(bank)
    press_enter_to_continue()


if __name__ == "__main__":
    main()
