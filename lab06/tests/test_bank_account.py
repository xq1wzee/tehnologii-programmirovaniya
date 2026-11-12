import unittest
from unittest.mock import MagicMock
from bank_account import BankAccount
from transaction_logger import TransactionLogger

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.mock_logger = MagicMock(spec=TransactionLogger)
        self.account = BankAccount("123456789", 100.0)
        self.account.set_logger(self.mock_logger)
    def test_create_account_with_balance(self):
        account = BankAccount("123456789", 100.0)
        self.assertEqual(account.getBalance(), 100.0)
    def test_create_account_with_default_balance(self):
        account = BankAccount("123456789")
        self.assertEqual(account.getBalance(), 0.0)
    def test_create_account_with_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("123456789", -100.0)
    def test_deposit_success(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.getBalance(), 150.0)
        self.mock_logger.log_transaction.assert_called_once_with(
            "123456789", "deposit", 50.0
        )
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        self.assertEqual(self.account.getBalance(), 100.0)
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50.0)
        self.assertEqual(self.account.getBalance(), 100.0)
    def test_withdraw_success(self):
        self.account.withdraw(30.0)
        self.assertEqual(self.account.getBalance(), 70.0)
        self.mock_logger.log_transaction.assert_called_once_with(
            "123456789", "withdraw", 30.0
        )
    def test_withdraw_all_balance(self):
        self.account.withdraw(100.0)
        self.assertEqual(self.account.getBalance(), 0.0)
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(150.0)
        self.assertEqual(str(context.exception), "Insufficient funds")
        self.assertEqual(self.account.getBalance(), 100.0)
    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        self.assertEqual(self.account.getBalance(), 100.0)
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-30.0)
        self.assertEqual(self.account.getBalance(), 100.0)
    def test_balance_after_multiple_operations(self):
        self.account.deposit(50.0)
        self.account.withdraw(30.0)
        self.account.deposit(20.0)
        self.assertEqual(self.account.getBalance(), 140.0)
    def test_logger_not_called_after_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(200.0)
        self.mock_logger.log_transaction.assert_not_called()

if __name__ == "__main__":
    unittest.main()