from dataclasses import dataclass

@dataclass
class Team:
    year: int
    teamCode: str
    name: str



    def __str__(self):
        return f"{self.teamCode}"

    def __hash__(self):
        return hash(self.teamCode)