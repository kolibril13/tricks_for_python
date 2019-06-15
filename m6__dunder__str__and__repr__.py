class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")

print(new_comedian)
print(str(new_comedian))
print(repr(new_comedian))
print(f"{new_comedian}")
print(f"{new_comedian!r}")

#__str__ -> gives an easy representation
#__repr__ -> should be unambiguous