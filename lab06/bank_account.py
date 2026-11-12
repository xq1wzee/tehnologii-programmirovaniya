from transaction_logger import TransactionLogger

class BankAccount:
    def __init__(self, accountNumber, balance=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.accountNumber = accountNumber
        self.balance = balance
        self.logger = None
    def set_logger(self, logger):
        self.logger = logger
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        if self.logger is not None:
            self.logger.log_transaction(
                self.accountNumber, "deposit", amount
            )
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        if self.logger is not None:
            self.logger.log_transaction(
                self.accountNumber, "withdraw", amount
            )
    def getBalance(self) -> float:
        return self.balance