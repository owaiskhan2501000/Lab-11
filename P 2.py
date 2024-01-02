class StringIterator:
    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.input_string):
            result = self.input_string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_string = "Hello, World!"
string_iterator = StringIterator(my_string)

for char in string_iterator:
    print(char)
