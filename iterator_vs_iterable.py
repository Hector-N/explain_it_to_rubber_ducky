
class Iterator(object):
    """
    Create iterator for looping over sequential data type object.
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.index:
            raise StopIteration
        else:
            self.counter += 1
            return self.data[self.counter - 1]


it = Iterator('magic in the air')
for word in it:
    print(word)
