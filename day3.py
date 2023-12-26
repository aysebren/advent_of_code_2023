#03.12.2023
#Advent Code Challenge Day 3
#Ayse Betul

import re
#######
# column-1,index_start-1       column-1,index_start    column-1,index_mid         column-1,index_end        column-1,index_end+1
# column  ,index_start-1       /column,index_start/    /column,index_mid/        /column,index_end/         column,index_end+1 
# column+1,index_start-1       column+1,index_start    column+1,index_mid         column+1,index_end        column+1,index_end+1
#######

with open("input3.txt") as f:
    contents = f.readlines()

contents = ["."+line.replace('\n', '..') for line in contents]

regex = re.compile('[\$\&\+\=\@\/\#\-\*\%\_]')
part_number=[]    


def my_main_fun(start,finish,column,index_list):
    not_part_number=[]
    for index_start, index_end in index_list:
        symbol_exist=False 
        debugger=[]
        for j in range(start,finish):
            a=[]
            for k in range(index_start-1,index_end+1):
                
                a.append(contents[j][k])
                if(regex.search(contents[j][k]) != None):
                    symbol_exist=True
            debugger.append(a)
       
        if not symbol_exist:
            my_digit=contents[column][index_start:index_end]
            symbol_exist=False
            not_part_number.append(int(my_digit))
            
            
    return not_part_number

for column,line in enumerate(contents):
    pattern=r'(\d+)'
    index_list=[(m.start(0), m.end(0)) for m in re.finditer(pattern, line)]
    digit_list=re.findall(r'(\d+)', line)
    not_part_number=[]
    if column!=0 and column!=len(contents)-1:
        start,finish=column-1,column+2
        not_part_number = my_main_fun(start,finish,column,index_list)
    if column==0:
        start,finish=column,column+2
        not_part_number = my_main_fun(start,finish,column,index_list)
    if column==len(contents)-1:
        start,finish=column-1,column+1
        not_part_number = my_main_fun(start,finish,column,index_list)

    set_difference = set(list(map(int, digit_list))) - set(not_part_number)
    
    list_difference_result = list(set_difference)
    part_number.append(sum(list_difference_result))

print(sum(part_number))
##my approach didn't give the correct answer therefore I applied the one below from reddit aoc sub:

import math as m, re

board = list(open('input3.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))
