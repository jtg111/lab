from account import *


class Test:
    def setup(self):
        self.a_1 = Account("John", 0)
        self.a_2 = Account("Jane")
        self.a_3 = Account("John", 100)

    def test_init(self):
        assert self.a_1.get_name() == "John"
        assert self.a_1.get_balance() == 0
        assert self.a_2.get_name() == "Jane"
        assert self.a_2.get_balance() == 0

    def test_deposit(self):
        assert self.a_1.deposit(-100) is False
        assert self.a_1.get_balance() == 0
        assert self.a_1.deposit(0) is False
        assert self.a_1.get_balance() == 0
        assert self.a_1.deposit(100) is True
        assert self.a_1.get_balance() == 100

    def test_withdraw(self):
        assert self.a_3.withdraw(-100) is False
        assert self.a_3.get_balance() == 100
        assert self.a_3.withdraw(0) is False
        assert self.a_3.get_balance() == 100
        assert self.a_3.withdraw(200) is False
        assert self.a_3.get_balance() == 100
        assert self.a_3.withdraw(50) is True
        assert self.a_3.get_balance() == 50

