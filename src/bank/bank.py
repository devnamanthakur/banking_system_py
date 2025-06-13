# banking_app_python/src/services/bank.py
import json
import os
from typing import Dict, Optional

from src.bank.account import Account

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "accounts.json")


class Bank:
    """Manages all bank accounts and operations."""

    def __init__(self):
        self.accounts: Dict[int, Account] = {}
        self.next_account_number: int = 1
        self._load_accounts()

    def _generate_account_number(self) -> int:
        """Generates a unique next account number."""
        num = self.next_account_number
        while num in self.accounts or num == 0:
            num += 1
            if num >= 2**32 - 1:  # Prevent overflow for u32 equivalent
                print("Warning: Account number range exhausted. Resetting.")
                num = 1
        self.next_account_number = num + 1
        return num

    def create_account(self, owner_name: str) -> Optional[int]:
        """
        Creates a new account with a given owner name.

        Args:
            owner_name: The name of the account owner.

        Returns:
            The new account number on success, None otherwise.
        """
        if not owner_name.strip():
            print("Error: Owner name cannot be empty.")
            return None

        account_number = self._generate_account_number()
        account = Account(account_number, owner_name)
        self.accounts[account_number] = account
        print(
            f"Successfully created account for {owner_name}. "
            f"Account number: {account_number}"
        )
        self._save_accounts()
        return account_number

    def deposit(self, account_number: int, amount: float) -> float:
        """
        Deposits money into a specified account.

        Args:
            account_number: The number of the account to deposit into.
            amount: The amount to deposit.

        Returns:
            The new balance.

        Raises:
            ValueError: If the account is not found or deposit fails.
        """
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError(f"Account {account_number} not found.")
        new_balance = account.deposit(amount)
        self._save_accounts()
        return new_balance

    def withdraw(self, account_number: int, amount: float) -> float:
        """
        Withdraws money from a specified account.

        Args:
            account_number: The number of the account to withdraw from.
            amount: The amount to withdraw.

        Returns:
            The new balance.

        Raises:
            ValueError: If the account is not found or withdrawal fails.
        """
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError(f"Account {account_number} not found.")
        new_balance = account.withdraw(amount)
        self._save_accounts()
        return new_balance

    def transfer(
        self, from_account_num: int, to_account_num: int, amount: float
    ) -> None:
        """
        Transfers money from one account to another.

        Args:
            from_account_num: The source account number.
            to_account_num: The destination account number.
            amount: The amount to transfer.

        Raises:
            ValueError: If accounts are not found, amount is invalid,
                        or funds are insufficient.
        """
        if from_account_num == to_account_num:
            raise ValueError("Cannot transfer to the same account.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        from_account = self.accounts.get(from_account_num)
        to_account = self.accounts.get(to_account_num)

        if not from_account:
            raise ValueError(f"Source account {from_account_num} not found.")
        if not to_account:
            raise ValueError(f"Destination account {to_account_num} not found.")
        if amount > from_account.balance:
            raise ValueError("Insufficient funds in source account.")

        # Perform the actual transfer
        from_account.balance -= amount
        to_account.balance += amount
        self._save_accounts()

    def check_balance(self, account_number: int) -> None:
        """
        Checks and displays the balance of a specific account.

        Args:
            account_number: The account number to check.
        """
        account = self.accounts.get(account_number)
        if account:
            print("\n--- Account Details ---")
            account.display_info()
            print("-----------------------\n")
        else:
            print(f"Error: Account {account_number} not found.")

    def list_all_accounts(self) -> None:
        """Displays details for all accounts currently in the bank."""
        if not self.accounts:
            print("\nNo accounts registered yet.")
            return

        print("\n--- All Accounts ---")
        for account in self.accounts.values():
            account.display_info()
            print("--------------------")
        print("--------------------")

    def _load_accounts(self) -> None:
        """Loads account data from the DATA_FILE."""
        if not os.path.exists(DATA_FILE):
            print("Data file not found. Starting with empty bank.")
            return

        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                loaded_accounts_data = data.get("accounts", [])
                loaded_next_account_number = data.get("next_account_number", 1)

                self.accounts.clear()  # Clear existing in case of reload
                max_account_num = 0
                for acc_data in loaded_accounts_data:
                    account = Account.from_dict(acc_data)
                    self.accounts[account.account_number] = account
                    if account.account_number > max_account_num:
                        max_account_num = account.account_number

                # Ensure next_account_number is always higher than any existing account
                self.next_account_number = max(
                    loaded_next_account_number, max_account_num + 1
                )

                print(f"Accounts loaded successfully from {DATA_FILE}.")

        except json.JSONDecodeError as e:
            print(f"Failed to parse account data from JSON: {e}")
        except IOError as e:
            print(f"Failed to read data file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while loading accounts: {e}")

    def _save_accounts(self) -> None:
        """Saves current account data to the DATA_FILE."""
        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            # Prepare data to save
            data_to_save = {
                "next_account_number": self.next_account_number,
                "accounts": [acc.to_dict() for acc in self.accounts.values()],
            }
            with open(DATA_FILE, "w") as f:
                json.dump(data_to_save, f, indent=4)
            # print(f"Accounts saved successfully to {DATA_FILE}.") # Optional: verbose saving
        except IOError as e:
            print(f"Failed to write data to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving accounts: {e}")
