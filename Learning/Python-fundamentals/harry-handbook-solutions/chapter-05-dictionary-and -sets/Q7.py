'''Q7:- If the names of 2 friends are same; what will happen to the program in problem 6 ?'''

"""
Summary :- In this program we will see what will happen if two friends have the same name
"""

l1=input("mr anubhav enter your favourite language as value for dictionary :-  ")
l2=input("mr krishna enter your favourite language as value for dictionary :-  ")
l3=input("miss radha enter your favourite language as value for dictionary :-  ")
l4=input("mr krishna enter your favourite language as value for dictionary :-  ")

dic={}#created an empty dictionary

dic.update({"anubhav":l1})
dic.update({"krishna":l2})
dic.update({"radha":l3})
dic.update({"krishna":l4})

# here both the keys are same i.e krishna
print(dic)
# in the output we can see that the value of first krishna is replaced by the value of second krishna
# because dictionary keys are unique and immutable 
# whole dictionary is mutable means we can make changes in the original dictionary
# but keys are unique and immutable
# but value can be same for two different keys like in real dictionary