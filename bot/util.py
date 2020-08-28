from constants import * 

async def class_details(class_type):
    class_colour = ""
    class_name = ""

    # Warrior
    if class_type == CLASS_WARRIOR:
        class_colour = CLASS_WARRIOR_COLOUR
        class_name = CLASS_WARRIOR_NAME

    # Paladin
    if class_type == CLASS_PALADIN:
        class_colour = CLASS_PALADIN_COLOUR
        class_name = CLASS_PALADIN_NAME

    # Hunter
    if class_type == CLASS_HUNTER:
        class_colour = CLASS_HUNTER_COLOUR
        class_name = CLASS_HUNTER_NAME

    # Rogue
    if class_type == CLASS_ROGUE:
        class_colour = CLASS_ROGUE_COLOUR
        class_name = CLASS_ROGUE_NAME

    # Priest
    if class_type == CLASS_PRIEST:
        class_colour = CLASS_PRIEST_COLOUR
        class_name = CLASS_PRIEST_NAME

    # Dk
    if class_type == CLASS_DEATH_KNIGHT:
        class_colour = CLASS_DEATH_KNIGHT_COLOUR
        class_name = CLASS_DEATH_KNIGHT_NAME

    # Shaman
    if class_type == CLASS_SHAMAN:
        class_colour = CLASS_SHAMAN_COLOUR
        class_name = CLASS_SHAMAN_NAME

    # Mage
    if class_type == CLASS_MAGE:
        class_colour = CLASS_MAGE_COLOUR
        class_name = CLASS_MAGE_NAME

    # Warlock
    if class_type == CLASS_WARLOCK:
        class_colour = CLASS_WARLOCK_COLOUR
        class_name = CLASS_WARLOCK_NAME

    # Monk
    if class_type == CLASS_MONK:
        class_colour = CLASS_MONK_COLOUR
        class_name = CLASS_MONK_NAME

    # Druid 
    if class_type == CLASS_DRUID:
        class_colour = CLASS_DRUID_COLOUR
        class_name = CLASS_DRUID_NAME

    # Demon Hunter
    if class_type == CLASS_DEMON_HUNTER:
        class_colour = CLASS_DEMON_HUNTER_COLOUR
        class_name = CLASS_DEMON_HUNTER_NAME

    class_data = {"colour": class_colour, "name": class_name}

    return class_data