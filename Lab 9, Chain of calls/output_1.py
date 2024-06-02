class Customer:
    def __init__(self, account):
        self._account = account

    def get_account(self):
        return self._account


class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance


class Bank:
    def __init__(self, customer):
        self._customer = customer

    def get_customer(self):
        return self._customer

    def get_customer_balance(self):
        return self._customer.get_account().get_balance()


bank = Bank(Customer(Account(1000)))
balance = bank.get_customer_balance()
print(f"The balance is: {balance}")
