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


    def play_games():
        while True:
            def guess_the_number():
                while True:
                    your_number = input("\nWelcome to 'guess the number' game!\n\tЕry to guess the number that I guessed "
                                        "from 0 to 10\nFor exit write:Exit")
                    num_1 = random.randint(0, 11)
                    if num_1 == int(your_number):
                        print("Сongratulations!!!! you have a good intuition")
                    elif your_number == "Exit":
                        break
                    else:
                        print("Нou were close try again")

            def rock_paper_scissors():
                print("Welcome to rock paper scissors")
                your_count = 0
                my_count = 0
                while True:
                    user = input("Please write rock, paper or scissors\nFor exit write: Exit\n")
                    list_movements = ["rock", "paper", "scissors"]
                    computer_choose = random.choice(list_movements)
                    if user == "rock":
                        if user == computer_choose:
                            print("draw")
                        elif computer_choose == "paper":
                            my_count += 1
                            print(f"I won, our account me {my_count} and your {your_count}")
                        elif computer_choose == "scissors":
                            your_count += 1
                            print(f"You won, our account me {my_count} and your {your_count}")
                        else:
                            print("Please choose version from menu")

                    if user == "paper":
                        if user == computer_choose:
                            print("draw")
                        elif computer_choose == "scissors":
                            my_count += 1
                            print(f"I won, our account me {my_count} and your {your_count}")
                        elif computer_choose == "rock":
                            your_count += 1
                            print(f"You won, our account me {my_count} and your {your_count}")
                        else:
                            print("Please choose version from menu")
                    if user == "scissors":
                        if user == computer_choose:
                            print("draw")
                        elif computer_choose == "rock":
                            my_count += 1
                            print(f"I won, our account me {my_count} and your {your_count}")
                        elif computer_choose == "paper":
                            your_count += 1
                            print(f"You won, our account me {my_count} and your {your_count}")
                        else:
                            print("Please choose version from menu")


            def field_of_miracles():
                count = 0
                print('Welcome to field_of_miracles')
                answer = input("What is the highest mountain in the world?\na)Everest\tb)Hoverla\nc)Elbrus\td)Anconghaua"
                               "\nPlease write just letter")
                if answer == "a":
                    count += 1
                    print("You're right")
                else:
                    print("Unfortunately, no, the answer is Everest")
                answer = input("how many years does it take to watch all videos on YouTube?\na)100\tb)1000\nc)200\td)500"
                               "\nPlease write just letter")
                if answer == "b":
                    count += 1
                    print("You're right")
                else:
                    print("Unfortunately, no, the answer is 1000")
                answer = input("How many on average questions does a 4-year-old child ask per day?\na)40\tb)100\nc)200"
                               "\td)400\nPlease write just letter")
                if answer == "d":
                    count += 1
                    print("You're right")
                else:
                    print("Unfortunately, no, the answer is 400")
                answer = input("what is the strongest muscle in the human body?\na)biceps\tb)triceps\nc)tongue\td)calf"
                               "\nPlease write just letter")
                if answer == "c":
                    count += 1
                    print("You're right")
                else:
                    print("Unfortunately, no, the answer is tongue")
                answer = input("What is the best-selling product in the world\n?a)ruby cube\tb)iphone\nc)charging"
                               "\td)refrigerator\nPlease write just letter")
                if answer == "a":
                    count += 1
                    print("You're right")
                else:
                    print("Unfortunately, no, the answer is ruby cube")
                print("Congratulations, you scored ", count, "out of 5 points\nIf you want to improve the result, "
                                                             "you can read interesting facts\n")


            chosse_game = input("Which game you choose?\n\tGuess the number\n\tRock-paper-scissors\n\tField of miracles"
                                "\nFor exit write: Exite")
            if chosse_game == "Guess the number":
                guess_the_number()
            elif chosse_game == "Rock-paper-scissors":
                rock_paper_scissors()
            elif chosse_game == "Field of miracles":
                field_of_miracles()
            else:
                print("Please choose version from menu")


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
