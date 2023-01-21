import random

while True:
    def choose_film():
        while True:
            choose_a_genre = input("What genre of movie do you want?\n\tComedy, Horror, Thriller, Cartoon, Historical"
                                    " or Documentary?\n\tFro exit write: Exit\nPlease print your answer here:")
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
        while True:
            choose_a_genre_music = input("What genre of music do you want?\n\tPop-music, Rock, Hip Hop, Rap\n\tFor exit "
                                         "write: Exit")
            dict_music = {
                "Pop music": ["Welcome to the Show", "Good", "Smak Tvij", "Dr Feel Good", "Eye of Heaven"],
                "Rock": ["Seven Odd Years", "Bucket, Forks, Pock", "Get It Together" "Young Trip", "Sport Rock"],
                "Hip Hop": ["Empire State of Mind", "Paper Planes", "Slow Down", "Tha Crossroads", "The Rain"],
                "Rap": ["JUNGLE", "Get Jumped", "New Bottega", "Slut Him Out Again", "Sincerely Face"]
            }
            if choose_a_genre_music == "Pop-music":
                music_value = dict_music["Pop music"]
                music = random.choice(music_value)
                print("You can listen this song:", music)
            elif choose_a_genre_music == "Rock":
                music_value = dict_music["Rock"]
                music = random.choice(music_value)
                print("You can listen this song:", music)
            elif choose_a_genre_music == "Hip Hop":
                music_value = dict_music["Hip Hop"]
                music = random.choice(music_value)
                print("You can listen this song:", music)
            elif choose_a_genre_music == "Pap":
                music_value = dict_music["Pap"]
                music = random.choice(music_value)
                print("You can listen this song:", music)
            elif choose_a_genre_music == "Exit":
                break
            else:
                print("Please choose version from menu!!!")


    def choose_play_game():
        while True:
            choose_a_genre_game = input("What genre of game do you want?\n\tStrategies, Arcadia, logical, Simulator\n\t"
                                        "For exit write: Exit\nWrite here:")
            dict_game = {
                "Strategies": ["Crusader Kings 3", "Europa Universalis 4", "Old World", "Civilization 6", "Stellaris"],
                "Arcadia": ["Block Champ", "Trizzle", "8 ball pool", "Cudoku", "Arkadium's Bubble Shooter"],
                "logical": ['Chess', "Reverse the Discs", "Liquid Sort", "Checkers", "Brixx"],
                "Simulator": ["Railway Empire", "Thief Simulator", "Planet Coaster", "Cooking Simulator", "Two Point Campus"]
            }
            if choose_a_genre_game == "Strategies":
                game_value = dict_game["Strategies"]
                game = random.choice(game_value)
                print("you can play this game:", game)
            elif choose_a_genre_game == "Arcadia":
                game_value = dict_game["Arcadia"]
                game = random.choice(game_value)
                print("you can play this game:", game)
            elif choose_a_genre_game == "logical":
                game_value = dict_game["logical"]
                game = random.choice(game_value)
                print("you can play this game:", game)
            elif choose_a_genre_game == "Simulator":
                game_value = dict_game["Simulator"]
                game = random.choice(game_value)
                print("you can play this game:", game)
            elif choose_a_genre_game == "Exit":
                break
            else:
                print("Please choose version from menu!!!")


    def read_anecdote():
        while True:
            choose_a_genre_anecdote = input("You want anecdote?\n\tYes or No\nWrite here")
            anecdote_list = ["If mirrors are used in telescopes, how do we know that there are no vampires in space?",
                             "I want to learn how to pass through walls, but something keeps stopping me.",
                             "The only way to make a good morning is to put your ego to sleep!",
                             "If you start the day with a positive attitude, you won't be sober by lunchtime",
                             "The main role of the little toe is to make sure that all the furniture in the house is in place."]
            if choose_a_genre_anecdote == "Yes":
                print(random.choice(anecdote_list))
            elif choose_a_genre_anecdote == "No":
                break
            else:
                print("Please choose version from menu!!!")


    def read_interesting_fact():
        while True:
            choose_a_genre_story = input("You want interesting fact?\n\tYes or No\nWrite here")
            fact_list = ["Half of the world's population (and by some estimates even two-thirds) have never seen snow.",
                        "The Rubik's Cube is the most sold product in the world. In second place is the iPhone.",
                        "It would take 1000 years to watch all the videos on YouTube.",
                        "The strongest muscle of the human body is the tongue.",
                        "A man is 6 times more likely to be struck by lightning than a woman.",
                        "If no dye was added to Coca-Cola, it would be green.",
                        "A four-year-old child asks an average of 400 questions a day.",
                        "Everest is not the highest mountain on the planet."]
            if choose_a_genre_story == "Yes":
                print(random.choice(fact_list))
            elif choose_a_genre_story == "No":
                break
            else:
                print("Please choose version from menu!!!")


    answer = input("Welcome to entertaining chatbot\nHow do you want have fun?\n\t1)Choose film\n\t2)Choose music\n\t"
                   "3)Choose play game\n\t4)Read anecdote\n\t5)Read interesting fact\n\t6)Play games\n\t7)Exit from bot"
                   "\n\tPlease write here:\n")
    if answer == "Choose film":
        choose_film()
    elif answer == "Choose music":
        choose_music()
    elif answer == "Choose play game":
        choose_play_game()
    elif answer == "Read anecdote":
        read_anecdote()
    elif answer == "Read interesting fact":
        read_interesting_fact()
    elif answer == "Play games":
        play_games()
    elif answer == "Exit from bot":
        print("Thank you for choosing our bot)")
        break
    else:
        print("Please choose version from menu")

    def play_games():
        pass



