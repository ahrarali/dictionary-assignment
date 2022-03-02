#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question  1
number_of_products = eval(input('Enter the num of products: '))
dictionary = {}

for i in range(number_of_products):
    name_of_products = input('Enter_the_name_of_product: ')
    price_of_products = eval(input('Enter_the_price: '))
    dictionary[name_of_products] = price_of_products

for i in range(number_of_products):
    name_of_product = input('Enter_the_name_of_product: ')
    if name_of_product in dictionary:
        print('The price is: ',dictionary[name_of_products])
    else:
        print('Product not in dictionary')
    


# In[6]:


# Question 2
Dictionary = {'coke':20, 'biscuit':40 ,'chips':100,'choclate':50}

price_of_product = eval(input('Enter the price: '))
for key ,values in Dictionary.items():
    if values < price_of_product:
        print('Product: ',key)


# In[12]:


# Question 3
days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}

month = input('Enter name of month: ')
print(days[month])

items = list(days)
items.sort()
for i in days:
    print(i)

for values,keys in days.items():
    if values == 31:
        print(keys)
    


# In[21]:


# Question 4
Dictionary = {'ahrar':224, 'mohtadi':568 ,'haroon':567 ,'rehman':876 ,'sadain':567}


def Check_identification(user_name,password):
    for keys ,values in Dictionary.items():
        if keys == user_name  and password == Dictionary[keys]:
            return ("you are succesfully logged in",keys,Dictionary[keys])
        else:
            return  ("Please do check your login details")

        
user_name = input("Enter Username: ")    
password = input("Enter Your Password ")       
print(Check_identification(user_name,password))


# In[24]:


# Question 5
def teamwin():
    number_of_Teams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(number_of_Teams):
        team_name = input("Enter Team Name: ")
        team_winning_score = eval(input("Team score Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)






print(teamwin())


# In[25]:


# Question 6
def teamInfo():
   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter number of Wins: "))
       losses = int(input("Enter number of losses Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(teamInfo())


# In[26]:


# Question 7
matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())


# In[28]:


# Question 8
import random
all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))
    c2= random.choice(list(all_card.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))


# In[34]:


# Question 9
def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise (TypeError,"expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise (ValueError, "Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
        #print(result,"result")
        #print(input,"Input")
    return ''.join(result)


print(int_to_roman(22))


# In[35]:


# Question 10

from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def validate_num(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nEnter a huge number for how many hands to play.')
        except ValueError:
            print('\nEnter a valid integer.')
    return user_input

def flush(COUNT, num):
    for i in range(num):
        hand = get_cards()
        if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
            COUNT += 1
        else:
            pass
    return COUNT

def get_cards():
    rand_cards = sample(Cards.DECK.value, 5)
    return rand_cards

def main():
    COUNT = 0
    message = 'Enter the number of hands to play: '
    num = validate_num(message)
    prob = flush(COUNT, num)
    print(f'\n{prob} hand(s) had a flush.\n')
    print(f'The probability to get a flush from {num} hands is {round((prob/num)*100, 3)}%.')

if __name__ == '__main__':
    main()


# In[ ]:




