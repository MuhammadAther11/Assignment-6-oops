class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total number of objects created: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()


Counter.get_count()