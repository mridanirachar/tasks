# Day 11 - Testing
# Bank Application


def create_account(name, balance=0):
    account = {"name": name, "balance": balance}
    return account


def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be positive")
        return account

    account["balance"] = account["balance"] + amount
    return account


def withdraw(account, amount):
    if amount <= 0:
        print("Withdraw amount must be positive")
        return account

    if amount > account["balance"]:
        print("Not enough balance")
        return account

    account["balance"] = account["balance"] - amount
    return account


def check_balance(account):
    return account["balance"]


def transfer(from_account, to_account, amount):
    if amount <= 0:
        print("Transfer amount must be positive")
        return False

    if amount > from_account["balance"]:
        print("Transfer failed, not enough balance")
        return False

    withdraw(from_account, amount)
    deposit(to_account, amount)
    return True


def get_interest_rate():
    return 5