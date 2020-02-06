#from sys import argv

#HOMEWORK NO:1
# def calcul():
#
#  name_of_file,output_in_hours , rate_per_hour, premium = argv
#  result = (int(output_in_hours)*int(rate_per_hour))+ int(premium)
#  print(name_of_file,result)
#
# calcul()
#
#HOMEWORK N0:2
# couldnt find the solution.
# my_list =[12,2,3,4,45,67,8,9,0]
#
# new_list = [i for i in my_list  ]
#
# print(new_list[2:-1:2])

#HOMEWORK NO: 3
# new = [num for num in range(20,240) if num == 20 or num == 21]
# print(new)

#HOMEWORK NO:4
# my_list = [2,3,2,4,5,5,6,12,12,3,1]
# new_list = [i for i in my_list if  my_list.count(i)<2]
# print(new_list)

#HOMEWORK NO:5
# new = [i for i in range(100,1000) if i % 2 ==0]
# print(sum(new)

#HOMEWORK NO:6

# from itertools import count,cycle
#
#  for num in count(1):
#     if num % 2 == 0:
#         print(num)
#
# for sentence in cycle("what's up"):
#     if sentence:
#         print(sentence)

#HOMEWORK NO:7
# this one is a bit complicated.

# def generator():
#     fact = [n for n in range(5)]
#     n =1
#     for el in fact(int(n)):
#         yield el
#
# gen =  generator()
# print(gen)
#
# for el in gen:
#     print(el)
