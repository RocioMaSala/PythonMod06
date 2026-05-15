from dark__validator import validate_ingredients

def dark_spell_allowed_ingredients():
    return "Allowed earth, air, fire, water"

def dark_spell_record(spell_name: str, ingredients: str):
    if validate_ingredients(ingredients) == "VALID":
        return ("Spell recorded")
    else:
        return ("Spell rejected")
