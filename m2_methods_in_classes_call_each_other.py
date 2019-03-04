class Functions:
    def f(self, x):
        return x*2

    def g(self, x):
        y= self.f(x)+2
        return y
var =1
print(Functions().g(var))
#or:
new_instance=Functions()
print(new_instance.g(var))
