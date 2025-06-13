# banking_app_python/src/models/account.py
class Account:
    """Represents a single bank account."""

    def __init__(self, account_number: int, owner_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Deposits a specified amount into the account.

        Args:
            amount: The amount to deposit.

        Returns:
            The new balance.

        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws a specified amount from the account.

        Args:
            amount: The amount to withdraw.

        Returns:
            The new balance.

        Raises:
            ValueError: If the amount is not positive or if funds are insufficient.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        """Returns the current balance of the account."""
        return self.balance

    def display_info(self) -> None:
        """Displays account information to the console."""
        print(f"  Account Number: {self.account_number}")
        print(f"  Owner Name: {self.owner_name}")
        print(f"  Balance: ${self.balance:.2f}")

    def to_dict(self) -> dict:
        """Converts the Account object to a dictionary for JSON serialization."""
        return {
            "account_number": self.account_number,
            "owner_name": self.owner_name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data: dict) -> "Account":
        """Creates an Account object from a dictionary (e.g., from JSON deserialization)."""
        return Account(
            account_number=data["account_number"],
            owner_name=data["owner_name"],
            balance=data["balance"],
        )
