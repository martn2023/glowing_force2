import characters_manager
import map_manager

class GameInstance:
    def __init__(self):
        self.player_name = "Martin"
        ##self.player_name = input("DUNGEON MASTER: What is your name?: ")
        print(f"DUNGEON MASTER: Welcome, {self.player_name}.")
        print("\n")
        import characters_manager
        self.playable_characters = characters_manager.CharacterLibrary()
        self.build_team_of_chars()
        self.active_maps = []
        self.load_main_menu()

    def build_team_of_chars(self):
        print("DUNGEON MASTER: It's time to build your team.")
        import characters_manager
        char_1 = characters_manager.Characters("Thor","warrior","\u2656",1,17,2,4,1,1,0,0)
        char_2 = characters_manager.Characters("Black Widow","rogue","\u2659",11,8,1, 3,3,1,0,0)
        char_3 = characters_manager.Characters("Hawkeye","hunter","\u2657",12,8,1,3,2,2,0,0)

        char_1.playable = True
        char_2.playable = True
        char_3.playable = True

        self.playable_characters.playable_characters.add(char_1)
        self.playable_characters.playable_characters.add(char_2)
        self.playable_characters.playable_characters.add(char_3)

        print(f"DUNGEON MASTER: Your team now has {self.playable_characters.show_playable_char_names() }")

    def load_main_menu(self):
        print("\n",)

        print("DUNGEON MASTER: ---------Welcome to the MAIN MENU.")
        self.count_stages_completed()
        print("DUNGEON MASTER: What do you want to do?", "\n")
        print("\t","1: Enter next map")
        print("\t","2: See who's on my team")
        print("\t","3: Quit", "\n") ## we should get in the habit of adding line breaks at end of prompt

        decision = int(input(""))  # int converter or else numbers will be in string format

        if decision == 3:
            self.game_over("you quit at the Main Menu.")
        elif decision == 2:
            print(self.playable_characters.show_playable_char_names())
        elif decision == 1:
            self.try_next_map()
        else:
            pass

        self.load_main_menu()

    def try_next_map(self):

        if len(self.active_maps) >0 and self.active_maps[-1].status != "complete":
            print(f"DUNGEON MASTER: You haven't completed {self.active_maps[-1].map_name} yet, so we are going back there.")
            map_number = len(self.active_maps)
            del self.active_maps[-1] ##need to remove last instance of the map so we don't get multiple attempts of same map
        else:
            map_number = 1+len(self.active_maps)


        if map_number ==1:
            first_map = map_manager.MapIndividual("Awakened Forrest", 3,5, self.playable_characters, map_number)
            first_map.print_map_backend()
            self.active_maps.append(first_map)

        elif map_number == 2:
            second_map = map_manager.MapIndividual("Broken Plains", 5, 6, self.playable_characters, map_number)
            second_map.print_map_backend()
            self.active_maps.append(second_map)

        else:
            self.game_over("the game developers ran out of maps.")


    def enter_stage(self):
        print("Stage entered")


    def game_over(self, reason: str):
        print("\n","\n","----------------GAME OVER----------------", "\n", "The game ended because", reason)
        exit() # take note that is the first time I used the exit command

    def count_stages_completed(self):
        count_stages_completed = 0
        for active_map in self.active_maps:
            if active_map.status == "complete":
                count_stages_completed += 1

        print(f"DUNGEON MASTER: You have seen {len(self.active_maps)} map(s) and completed {count_stages_completed} of them.")