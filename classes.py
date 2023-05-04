from dataclasses import dataclass
from skills import Skill, BloodShot, FuryPunch


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воитель',
    max_health=200.0,
    max_stamina=20.0,
    attack=45.0,
    stamina=0.9,
    armor=100.0,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name='Вор',
    max_health=100.0,
    max_stamina=10.0,
    attack=25.0,
    stamina=0.1,
    armor=150.0,
    skill=BloodShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}