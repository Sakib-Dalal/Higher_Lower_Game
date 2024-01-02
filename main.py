import random
from art import logo, vs
from gamedata import data


def chose_function():
    rand_num = random.randint(0, 49)
    name = data[rand_num]['name']
    follower_count = data[rand_num]['follower_count']
    description = data[rand_num]['description']
    country_of_origin = data[rand_num]['country']
    return [name, follower_count, description, country_of_origin]


def highest_follower_checker(l1, l2):
    highest_follower = ""
    if l1[1] > l2[1]:
        highest_follower += l1[0]
        return highest_follower
    else:
        highest_follower += l2[0]
        return highest_follower


def my_game():
    print(logo)
    old_list = []
    current_score = 0

    def my_fun(lst, score):
        if not lst:
            lst1 = chose_function()
        else:
            lst1 = lst

        lst2 = chose_function()

        if lst1 == lst2:
            lst2 = chose_function()

        highest_follower_name = highest_follower_checker(lst1, lst2)

        print(f"🟧 Compare A: {lst1[0]}, a {lst1[2]} from {lst1[3]}")
        print(vs)
        print(f"🟥 Against B: {lst2[0]}, a {lst2[2]} from {lst2[3]}")
        user_input = input("🤨 Who has more followers? Type A or B 👉 ").upper()

        user_ans = []
        if user_input == 'A':
            user_ans = lst1
        elif user_input == 'B':
            user_ans = lst2
        else:
            print("Wrong input ☠️")

        final_score = score

        if user_ans[0] == highest_follower_name:
            print()
            print("🟢 You Won 🥳")
            print(highest_follower_name + " is the correct answer 👍.")
            print()
            final_score += 1
            my_fun(user_ans, final_score)
        else:
            print()
            print("🔴 You lose 😭")
            print("👉" + highest_follower_name + " have the highest followers.")
            print(f"📜 Your final Score is: {final_score}")

    my_fun(old_list, current_score)


my_game()
