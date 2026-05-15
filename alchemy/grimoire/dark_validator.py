def validate_ingredients(ingredients: list):
    valid_elements = {"bats", "frogs", "arsenic", "eyeball"}
    for ingredient in ingredients:
        if ingredient in valid_elements:
            return "VALID"
    return "INVALID"