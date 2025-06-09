
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        self.current -= 1
        return self.current
    
cd = Countdown(10)

for number in cd:
    print(number)
