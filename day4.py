# #04.12.2023
#Advent Code Challenge Day 4
#Ayse Betul
import re


with open("input4.txt") as f:
    contents = f.readlines()
contents = [line.replace('\n', '') for line in contents]


def remove(string):
    ns=""
    for i in string:
        if(not i.isspace()):
            ns+=i
    return ns    


first_question=[]
for content in contents:
    splitted=re.split(':|, |\|',content)

    ref_list=re.findall(r'(\d+)', splitted[1])
    my_list=re.findall(r'(\d+)', splitted[2])

    S1 = set(list(map(int,my_list)))
    S2 = set(list(map(int,ref_list))) 

    n=len(S1.intersection(S2))
    if n!=0:
        cards_worth=pow(2,n-1)
        first_question.append(cards_worth)
       
print(sum(first_question))


second_question=[]
for index,content in enumerate(contents):
    splitted=re.split(':|, |\|',content)

    ref_list=re.findall(r'(\d+)', splitted[1])
    my_list=re.findall(r'(\d+)', splitted[2])

    S1 = set(list(map(int,my_list)))
    S2 = set(list(map(int,ref_list))) 

    n=len(S1.intersection(S2))
    without_space=remove(splitted[0])


    second_question.append(without_space)
    if n!=0:     
        for i in range(n):
            final_str = "Card%s" % (index+2+i)
 
            prev_str =without_space
            is_my_card_entered_before=  second_question.count(prev_str)

            if  is_my_card_entered_before!=0:
                second_question.extend([final_str for i in range(is_my_card_entered_before)])

print(len(second_question))
