
#BlackJack
#######################################################################333
import random
user_sum,bot_sum,user_choice = 0,0,0
user_stand,bot_stand=False,False
def validate(tempsum):
    if tempsum==21:
        return True
    elif tempsum>21:
        return False
    return 0

def choose(value):
    if (value==20):
        return False
    elif (value>=17):
        temp = random.uniform(0.0,1.0)
        if temp<0.3:
            return True
        else:
            return False
    else:
        return True
    return False

print("Welcome to BlackJack")
while True:
    print("#################################################################################")
    print(f"Bot's Sum: {bot_sum}")
    print(f"Your Sum: {user_sum}")
    print(f"What will you do? \n 1) Hit \n 2) Stand \n 3) Exit")
    try:
        user_choice = int(input())
        if(user_choice<1 or user_choice>3):
            print("Invalid choice\n \n ")
            continue
    except Exception:
        print("Invalid choice")
        continue
    if user_choice==1:
        print("You chose to hit")
        temp_list = backend.get_card()
        user_sum += int(temp_list[1])
    elif user_choice==2:
        print("You chose to stand")
        user_stand=True
    elif user_choice==3:
        print("Thank you for playing")
        break
    if user_sum>21:
        print(f"User sum: {user_sum}. Game over")
        break
    if user_sum==21:
        print(f"User sum: {user_sum}. Blackjack! You win!")
        break
    hit_check = choose(bot_sum)
    if hit_check==True:
        print("Bot chose hit")
        bot_card = backend.get_card()
        bot_sum += int(bot_card[1])
    else:
        print("Bot chose to stand")
        bot_stand=True

    if user_stand and bot_stand ==True:
        if user_sum>bot_sum:
            print(f"User_sum: {user_sum}. You win!")
            break
        elif user_sum==bot_sum:
            print("Both sums equal, draw!")
            break
        else:
            print(f"Bot_sum = {bot_sum}. Bot wins!")
            break

    if validate(bot_sum)==True:
        print("Bot_sum = {bot_sum}. Bot wins!\nResetting Game...")
        break
    elif validate(bot_sum)==0:
        continue
    elif validate(bot_sum)==False:
        print("Sum of cards over 21, game over\n Resetting Game...")
        break
