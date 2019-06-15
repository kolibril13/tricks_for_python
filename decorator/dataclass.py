from dataclasses import dataclass, field

@dataclass(order=True)
class Country:
    name: str  = field( compare=False)
    population: int
    area: float = field(repr=False, compare=False)
    coastline: float = field( compare=False)

    def beach_per_person(self):
        """Meters of coastline per person"""
        return (self.coastline * 1000) / self.population

norway = Country("Norway", 5320045, 323802, 58133)
usa = Country("United States", 326625791, 9833517, 19924)
print(norway < usa)