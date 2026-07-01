# Day 11 - Testing
# Tests for bank.py

import unittest
from unittest.mock import patch
import pytest

import bank
from bank import create_account, deposit, withdraw, check_balance, transfer


def test_deposit_with_assert():
    account = create_account("Krishna", 1000)
    deposit(account, 500)
    assert check_balance(account) == 1500


def test_withdraw_with_assert():
    account = create_account("Krishna", 1000)
    withdraw(account, 300)
    assert check_balance(account) == 700


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = create_account("Mridula", 2000)

    def test_deposit(self):
        deposit(self.account, 500)
        self.assertEqual(check_balance(self.account), 2500)

    def test_withdraw_too_much(self):
        withdraw(self.account, 5000)
        self.assertEqual(check_balance(self.account), 2000)

    def test_transfer(self):
        other_account = create_account("Prasanna", 100)

        transfer(self.account, other_account, 500)

        self.assertEqual(check_balance(self.account), 1500)
        self.assertEqual(check_balance(other_account), 600)


@pytest.fixture
def sample_account():
    return create_account("Krishna", 1000)


def test_deposit_with_fixture(sample_account):
    deposit(sample_account, 200)
    assert check_balance(sample_account) == 1200


def test_withdraw_with_fixture(sample_account):
    withdraw(sample_account, 400)
    assert check_balance(sample_account) == 600


def test_transfer_with_fixture(sample_account):
    receiver = create_account("Guwahati Branch", 0)

    transfer(sample_account, receiver, 1000)

    assert check_balance(sample_account) == 0
    assert check_balance(receiver) == 1000


@patch("bank.get_interest_rate")
def test_interest_rate_is_mocked(mock_rate):
    mock_rate.return_value = 9

    rate = bank.get_interest_rate()

    assert rate == 9
    mock_rate.assert_called_once()


if __name__ == "__main__":
    unittest.main()