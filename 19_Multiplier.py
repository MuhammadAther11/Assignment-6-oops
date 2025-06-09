
class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
m2 = Multiplier(2)
print(callable(m2))

result = m2(10)
print(result)