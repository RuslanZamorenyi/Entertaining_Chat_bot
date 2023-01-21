import random

while True:
    def choose_film():
        while True:
            choose_a_genre = input("What genre of movie do you want?\n\tComedy, Horror, Thriller, Cartoon, Historical"
                                    "or Documentary?\n\tFro exit write: Exit\nPlease print your answer here:")
            dict_film = {
                "comedy": ["HOT ROD", "GAME NIGHT", "THE FIRST WIVES CLUB", "SCARY MOVIE", "BLOCKERS"],
                "horror": ["BRAM STOKER'S DRACULA", "HELLRAISER", "IT'S ALIVE!", "OPEN WATER", "THE RING"],
                "thriller": ["Psycho", "The Departed", "The Prestige", "Parasite", "Se7en"],
                "cartoon": ["REDLINE", "MONSTER HOUSE", "ANASTASIA", "PARANORMAN", "TOWER"],
                "historical": ["The Vikings", "Ben Hur", "Spartacus", "Braveheart", "Gladiator"],
                "documentary": ["Food is Heaven", "Before Pangaea", "Slave to the Algorithm", "Beer Culture", "Death by China"]
            }
            if choose_a_genre == "Comedy":
                comedy_value = dict_film["comedy"]
                film = random.choice(comedy_value)
                print("Нou can watch this comedy:", film)
            elif choose_a_genre == "Horror":
                horror_value = dict_film["Horror"]
                film = random.choice(horror_value)
                print("Нou can watch this horror:", film)
            elif choose_a_genre == "Thriller":
                thriller_value = dict_film["thriller"]
                film = random.choice(thriller_value)
                print("Нou can watch this thriller:", film)
            elif choose_a_genre == "Cartoon":
                cartoon_value = dict_film["cartoon"]
                film = random.choice(cartoon_value)
                print("Нou can watch this cartoon:", film)
            elif choose_a_genre == "Historical":
                historical_value = dict_film["historical"]
                film = random.choice(historical_value)
                print("Нou can watch this cartoon:", film)
            elif choose_a_genre == "Documentary":
                documentary_value = dict_film["documentary"]
                film = random.choice(documentary_value)
                print("Нou can watch this cartoon:", film)
            elif choose_a_genre == "Exit":
                break
            else:
                print("Please choose version from menu!!!")


    def choose_music():
        
        pass










    answer = input("Welcome to entertaining chatbot\nHow do you want have fun?\n\t1)Choose film\n\t2)Choose music\n\t"
                   "3)Choose play game\n\t4)Read anecdote\n\t5)Read interesting story\n\t6)Play games\n\t7)Exit from bot"
                   "\n\tPlease write here:\n")
    if answer == "Choose film":
        choose_film()
    elif answer == "Choose music":
        choose_music()
    elif answer == "Choose play game":
        choose_play_game()
    elif answer == "Read anecdote":
        read_anecdote()
    elif answer == "Read interesting story":
        read_interesting_story()
    elif answer == "Play games":
        play_games()
    elif answer == "Exit from bot":
        print("Thank you for choosing our bot)")
        break
    else:
        print("Please choose version from menu")


    def choose_play_game():
        pass


    def read_anecdote():
        pass


    def read_interesting_story():
        pass


    def play_games():
        pass



