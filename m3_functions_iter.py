# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

    # Cosntructor
    def __init__(self, limit):
        self.limit = limit

        # Called when iteration is initialized

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

            # Else increment and return old value
        self.x = x + 1;
        return x

    # Prints numbers from 10 to 15


printNumIter = iter(Test(15))
print(next(printNumIter))
