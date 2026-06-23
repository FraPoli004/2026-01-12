from dataclasses import dataclass
import datetime

@dataclass
class Constructor:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str

    def __hash__(self):
        return hash(self.constructorId)

    def __str__(self):
        return f"{self.constructorRef} ({self.name})"

    def __eq__(self, other):
        return self.constructorId == other.constructorId
