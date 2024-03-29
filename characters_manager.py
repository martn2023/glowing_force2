class Characters:
    def __init__(self, display_name: str, char_class: str, map_icon, maximum_health: int, attack_power: int, physical_armor: int, initiative: int, mobility: int, physical_attack_range: int, row_index: int, col_index: int):
        self.display_name = display_name
        self.char_class = char_class
        self.map_icon = map_icon
        self.maximum_health = maximum_health
        self.current_health = maximum_health
        self.attack_power = attack_power
        self.physical_armor = physical_armor ## this will mitigate an attacker's Attack Power
        self.initiative = initiative  # for now, assume the player does not have choice of order
        self.mobility = mobility
        self.physical_attack_range = physical_attack_range
        self.row_index = row_index
        self.col_index = col_index
        self.playable = False ##assumes all chars are NPCs until told otherwise

        print("DUNGEON MASTER:","*",f"{self.display_name} ({self.char_class}) has been spotted: {self.map_icon}")


class CharacterLibrary: #for now, this only holds PLAYABLE characters, because the NPCs are created and stored within the map
    def __init__(self):
        #print(f"BACKEND: Char library created")
        self.playable_characters = set()  ##this might come back to bite you bc the rest of the system assumes lists, not sets

    def show_playable_char_keys(self): ##converting from a set to an array
        list_of_character_keys = []
        for object_id in self.playable_characters:
            list_of_character_keys.append(object_id)
        return list_of_character_keys

    def show_playable_char_names(self):
        list_of_character_names = []
        for each_object in self.playable_characters:
            list_of_character_names.append(each_object.display_name + " " + each_object.map_icon )
        return list_of_character_names

    def show_playable_char_icons(self):
        list_of_character_icons = []
        for each_object in self.playable_characters:
            list_of_character_icons.append(each_object.map_icon)
        return list_of_character_icons
