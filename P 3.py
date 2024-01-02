class PowerOfTwoIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = 2 ** self.current
            self.current += 1
            return result

power_of_two_iterator = PowerOfTwoIterator(0, 5)

for power in power_of_two_iterator:
    print(power)
