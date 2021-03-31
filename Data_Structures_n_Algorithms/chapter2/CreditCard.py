class CreditCard:
    def __init__(self, customer, bank, account, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance
    
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        
        Return True if Charge was processed; False if charge was denied"""
        while(True):
            try:
                if price + self._balance > self._limit:
                    return False
                else:
                    self._balance += price
                    return True
            except ValueError:
                print('That is invalid price')
                price = float(input('Please re-enter price: '))
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        while(True):
            try:
                if (amount < 0):
                    raise ValueError
                else:
                    self._balance -= amount
                    break
            except ValueError:
                print('That is invalid amount')
                price = float(input('Please re-enter amount: '))