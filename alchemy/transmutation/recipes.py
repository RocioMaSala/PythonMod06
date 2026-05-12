from alchemy.elements import create_air # absoluto
from ..potions import strength_potion # relativo
from elements import create_fire # absoluto


def lead_to_gold():
    return(f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{create_fire()}'")