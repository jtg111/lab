class Account:
    """
    A class for keeping track of a person's account balance
    """

    def __init__(self, name: str, balance=0):
        """
        Constructor that creates the name of the person and initial balance of the person's account.
        :param name: Person's name.
        :param balance: Person's current account balance.
        """
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount: int):
        """
        Method for adding an amount of money to person's account
        :param amount: The amount being added to the account. Cannot be negative or 0.
        :return: Returns False if deposit fails (negative or 0 amount), True if deposit is successful.
        """
        if amount < 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: int):
        """
        Method for subtracting an amount of money from a person's account.
        :param amount: The amount being withdrawn from the account. Cannot be negative or 0.
        :return: Returns False if withdrawal fails (negative or 0 amount), True if withdrawal is successful.
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        """
        Method for retrieving the current account balance.
        :return: Returns current account balance.
        """
        return self.__account_balance

    def get_name(self):
        """
        Method for retrieving the name of the account.
        :return: Returns account name.
        """
        return self.__account_name
