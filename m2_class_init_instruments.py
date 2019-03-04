class Instruments_class:
    def __init__(self, strings):
        self.strings=  strings
    model = "Fender"
    def Guitar(self):
        model = self.model
        print( model )


if __name__ == "__main__":
    g1= Instruments_class(strings="guten")
    print(g1.strings)

