class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
x= Restaurant()

print(x.bankrupt)
#The above command is same as:
print(Restaurant().bankrupt)


