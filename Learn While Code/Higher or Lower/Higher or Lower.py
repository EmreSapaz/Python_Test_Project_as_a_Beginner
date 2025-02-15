import game_data
import art
import random
import time

is_playing = True
count = 0
first = random.choice(game_data.data)

while is_playing:

    print(art.logo)

    f_name = first["name"]
    f_description = first["description"]
    f_country = first["country"]
    f_follower = first["follower_count"]

    print(f"Compare A :{f_name} is {f_description} from {f_country}")

    print(art.vs)

    second = random.choice(game_data.data)

    while first == second:
        second = random.choice(game_data.data)

    s_name = second["name"]
    s_description = second["description"]
    s_country = second["country"]
    s_follower = second["follower_count"]


    print(f"Against B : {s_name} is {s_description} from {s_country}")


    compare = input("Who has more followers?\nA or B:")

    if (compare.upper() == "A" and s_follower<f_follower) or (compare.upper() == "B" and f_follower<s_follower):
        count += 1
        print(f"Correct !! Your Score : {count}")
        time.sleep(.5)
        first = second

    else:
        print(f"Wrong !! Your Final Score : {count}")
        is_playing = False