#02.12.2023
#Advent Code Challenge Day 2
#Ayse Betul

import re
game_list=[]
look_up_table={"red"   :12,
               "green" :13,
               "blue"  :14 }
reference=list(range(1, 100))
with open("input2.txt") as f:
    contents = f.readlines()

split_list = [item.split(':') for item in contents]
for line in split_list:
    match_list=re.findall(r'(\d+) (\w+)', line[1])
    line_detected=False
    for num,color in match_list:
        for i in look_up_table:
            if color == i and not line_detected:
                if int(num) > look_up_table[i]:
                   which_game=(int(line[0].split("Game")[1]))
                   game_list.append(which_game)
                   line_detected=True          
                        
set_difference = set(reference) - set(game_list)
list_difference_result = list(set_difference)
print(sum(list_difference_result))


game_list=[]
for line in split_list:
    match_list=re.findall(r'(\d+) (\w+)', line[1])
    big_red=0
    big_green=0
    big_blue=0
    power=0
    for num,color in match_list:
        if color == "red":
            if int(num) > big_red:
               big_red=int(num)
        if color == "green":
            if int(num) > big_green:
               big_green=int(num)
        if color == "blue":
            if int(num) > big_blue:
               big_blue=int(num)
    power=big_red*big_green*big_blue
    game_list.append(power)
                
print(sum(game_list))              