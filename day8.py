# #05.12.2023
#Advent Code Challenge Day 8
#Ayse Betul
import re

with open("input8.txt") as f:
    contents = f.readlines()
contents = [line.replace('\n', '') for line in contents]
my_dict = {"first":[],"second":[]}

asd="LRLRLRLLRRLRRLRRRLRRLRLLRRRLRRRLRRLLLLRRRLRLLRRLRRLRRLLLRRRLRRRLRRLRLRRLRLRLRLLRRRLRRRLLRRRLRRRLRRRLRLLLRRLRLRRRLRLRRRLLRRRLRLLRLRRRLRLRRRLRRLLRLRLRRLRLRLRRLRLRLRRRLRRLRLLRRLRRRLRRRLRRLRRRLRRLRLRRRLLRRRLLRRLRLRRRLRRRLLRRRLRLRRLRLRLRRLRLLRRLRLRLRRLRRRLRRRLRLRRLRRLLLRRRLLRLRRRLLRRRR"
liste=[]


for index,content in enumerate(contents):
    splitted=re.split('=',content)
    my_dict["first"].append(splitted[0])
    my_dict["second"].append(splitted[1])
step_counter=0

for j in asd:
    if j=="L":
        liste.append(0)
    elif j=="R":
        liste.append(1)

lookup="AAA"
for index,value in enumerate(my_dict["first"]):
    a=value.find("AAA")
    if a!=-1:
        while not lookup=="ZZZ":
            for j in liste:
                if j ==0:
                    lookup = my_dict["second"][index][2:5]
                elif j==1:
                    lookup = my_dict["second"][index][7:10]
                for index,value in enumerate(my_dict["first"]):
                    a=value.find(lookup)
                    if a!=-1:
                        step_counter+=1
                        break

print(step_counter)

                
