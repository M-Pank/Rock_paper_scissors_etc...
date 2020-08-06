import random
print("Enter your name:", end="")
name = input()
print(f'Hello, {name}')

#scores
result = open('rating.txt', "r")
user_score = 0
for results in result:
    if name == results.split()[0]:
        user_score = int(results.split()[1])
        break
result.close()

#OPTIONS


print("Enter options:", end="")
p_options = input().split(",")
if len(p_options) < 2:
    if str(*p_options) == "":
        options = ["rock", "paper", "scissors"]
    else:
        options = p_options
else:
    options = p_options
print("Okay, let's start")


#Body
vvod = input().split()
z = 0
while True:
    for chose in vvod:
        choose = str(chose).replace(" ", '')
        if chose == "!exit":
            print("Bye!")
            z = 1
            break
        elif choose == "!rating":
            print(f"You rating: {user_score}")
        elif chose not in options:
            print("Invalid input")
        elif chose in options:
            comp_chose = random.choice(options)


            #win/lose and results dict
            win = f'Well done. Computer chose {comp_chose} and failed'
            lose = f'Sorry, but computer chose {comp_chose}'
            results_list = ['rock', 'gun', 'lightning', 'devil', 'dragon',
           'water', 'air', 'paper', 'sponge', 'wolf',
           'tree', 'human', 'snake', 'scissors', 'fire']
            ind = results_list.index(str(*vvod))

            #win or lose mechanic
            if chose == comp_chose:
                print(f"There is a draw ({chose})")
                user_score += 50
            else:
                if ind <= 7:
                    if comp_chose in results_list[ind+1:ind+8]:
                        final = lose
                    else:
                        final = win
                elif ind >= 8:
                    if comp_chose in results_list[ind-1:ind-8:-1]:
                        final = win
                    else:
                        final = lose
                print(final)
                if final == win:
                    user_score += 100
    if z != 1:
        vvod = input().split()
    else:
        break
if vvod == "!exit":
    print('Bye!')
