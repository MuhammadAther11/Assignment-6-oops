

class Bank:
    bank_name = "Bank of Python"

    @classmethod
    def change_bank_name(cls , new_name):
     cls.bank_name = new_name
     

b1 = Bank()

print(b1.bank_name) 
Bank.change_bank_name("New Bank of Python")
print(b1.bank_name)