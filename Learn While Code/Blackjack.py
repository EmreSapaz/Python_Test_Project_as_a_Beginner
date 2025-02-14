import random
import time

def main():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    computer = []
    player = []
    player.append(random.choices(cards, k=2))
    sum_player : int = 0

    computer.append(random.choices(cards, k=2))
    sum_comp : int = 0
    for i in player:
        for j in i:
            print(f"You got : {j}")
            sum_player += j

    for i in computer:
        for j in i:
            print(f"Computer got : {j}")
            sum_comp +=j

    print("*******************************")
    print(f"Your Total : {sum_player}")
    print("*******************************")

    print(f"Computer Total : {sum_comp}")
    print("*******************************")

    is_playing = True

    while is_playing:
        if sum_player>21:
            print(f"Your Total : {sum_player}")
            print("You Lose!!")
            print("***************New Game***************")
            again = input("Wanna play again?\nY or N:")
            if again.upper() == "Y" and is_playing:
                print("***************New Game***************")
                main()
            else:
                is_playing = False

        else:
            if sum_player == 21:
                print("Blackjack!!! You Win!!")
                print("***************New Game***************")
                again = input("Wanna play again?\nY or N:")
                if again.upper() == "Y" and is_playing:
                    print("***************New Game***************")
                    main()
                else:
                    is_playing = False

            elif sum_comp == 21 and not sum_comp == sum_player:
                print("You Lose!!")
                print("***************New Game***************")
                again = input("Wanna play again?\nY or N:")
                if again.upper() == "Y" and is_playing:
                    print("***************New Game***************")
                    main()
                else:
                    is_playing = False

            elif is_playing:
                while sum_player < 21 and is_playing:
                    ask = input("Wanna get another card?\nY or N:")
                    if ask.upper() == "Y":
                        new_card : int = random.choice(cards)
                        time.sleep(0.4)
                        print(f"You got : {new_card}")
                        sum_player += new_card
                        print(f"Your Total : {sum_player}")
                        if sum_player>21:
                            print("You Lose!!")
                            print("***************New Game***************")
                            again = input("Wanna play again?\nY or N:")
                            if again.upper() == "Y" and is_playing:
                                print("***************New Game***************")
                                main()
                            else:
                                is_playing = False
                        elif sum_player == 21:
                            print("You Win!!")
                            print("***************New Game***************")
                            again = input("Wanna play again?\nY or N:")
                            if again.upper() == "Y" and is_playing:
                                print("***************New Game***************")
                                main()
                            else:
                                is_playing = False
                    else:
                        while is_playing:
                            if sum_comp > 21:
                                print("You Win!!")
                                print("***************New Game***************")
                                again = input("Wanna play again?\nY or N:")
                                if again.upper() == "Y" and is_playing:
                                    print("***************New Game***************")
                                    main()
                                else:
                                    is_playing = False
                            elif sum_comp < 17:
                                while sum_comp<17 and is_playing:
                                    new_comp: int = random.choice(cards)
                                    time.sleep(0.4)
                                    print(f"Computer got : {new_comp}")
                                    time.sleep(.4)
                                    sum_comp += new_comp
                                    print(f"Computer Total : {sum_comp}")
                                    if sum_comp == 21 and sum_player != sum_comp:
                                        print("You Lose!!!")
                                        print("***************New Game***************")
                                        again = input("Wanna play again?\nY or N:")
                                        if again.upper() == "Y" and is_playing:
                                            print("***************New Game***************")
                                            main()
                                        else:
                                            is_playing = False
                            while sum_comp >= 17 and is_playing:
                                if sum_comp<sum_player:
                                    print("You Win!!")
                                    print("***************New Game***************")
                                    again = input("Wanna play again?\nY or N:")
                                    if again.upper() == "Y" and is_playing:
                                        print("***************New Game***************")
                                        main()
                                    else:
                                        is_playing = False

                                elif sum_player<sum_comp and not sum_comp>21:
                                    print("You Lose!!")
                                    print("***************New Game***************")
                                    again = input("Wanna play again?\nY or N:")
                                    if again.upper() == "Y" and is_playing:
                                        print("***************New Game***************")
                                        main()
                                    else:
                                        is_playing = False

                                elif sum_player<sum_comp and sum_comp>21:
                                    print("You Win!!")
                                    print("***************New Game***************")
                                    again = input("Wanna play again?\nY or N:")
                                    if again.upper() == "Y" and is_playing:
                                        print("***************New Game***************")
                                        main()
                                    else:
                                        is_playing = False

                                elif sum_comp == sum_player and not sum_comp>21:
                                    print("Draw!!")
                                    print("***************New Game***************")
                                    again = input("Wanna play again?\nY or N:")
                                    if again.upper() == "Y" and is_playing:
                                        print("***************New Game***************")
                                        main()
                                    else:
                                        is_playing = False


main()