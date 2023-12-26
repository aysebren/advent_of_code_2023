#01.12.2023
#Advent Code Challenge Day 1
#Ayse Betul

digit_list=[]
digit_list2=[]

look_up_table={"one"   :1,
               "two"   :2,
               "three" :3,
               "four"  :4,
               "five"  :5,
               "six"   :6,
               "seven" :7,
               "eight" :8,
               "nine"  :9 }


with open("input.txt") as f:
    contents = f.readlines()

def get_digit_and_index(text):
    return [(index, cha) for index, cha in enumerate(text) if cha.isdigit()]

for content in contents:
    digi=get_digit_and_index(content)
    my_num= int(digi[0][1])*10+int(digi[-1][1])
    digit_list.append(my_num)
answer_for_first_question=sum(digit_list)
print(answer_for_first_question)

for content in contents:
    digi=get_digit_and_index(content)
    for i in look_up_table:
        first_index=-1
        next_index=len(content)

        while first_index+1 < len(content):
                     
            if content.find(i,first_index+1) != -1:
                next_index=content.find(i,first_index+1)
                digi.append((next_index, str(look_up_table[i])))              
            else:
                 break
            first_index= next_index 
            
    digi.sort(key=lambda a: a[0])        
    my_num2= int(digi[0][1])*10+int(digi[-1][1])
    digit_list2.append(my_num2)

answer_for_second_question=sum(digit_list2)
print(answer_for_second_question)
