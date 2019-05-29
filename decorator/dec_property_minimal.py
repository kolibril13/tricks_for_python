class Guitar:
    def __init__(self, string):
        self._strings= string

    @property
    def strings(self):
        return self._strings
    @strings.setter
    def strings(self,value):
        self._strings= value

g=Guitar(string=9)
g.strings=10
print(g.strings)

