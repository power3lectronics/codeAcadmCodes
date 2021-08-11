# Python v2.0 - 2014

print "Welcome to the English to Pig Latin translator!\n"
original = raw_input("Original word: ")
if len(original) != 0 and original.isalpha():
    print original
else:
    print "empty/non alphabetical"
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha(): #verify if isnt an empty string and if it has only letters
    original = original.lower()
    word = original
    first = word[0]
    if first == "a" or first == "A" or first == "i" or first == "I" or first == "u" or first == "U" or first == "e" or first == "E" or first == "o" or first == "O":
        print "vowel"
        new_word = word + pyg 
        print new_word
    else:
        print "consoant"
        new_word = word[1:] + first + pyg
        print new_word
else:
    print 'empty'
 
 
word[1:] -> get from the second character til the final
 
------------------
 
def hotelCost(days):
    return 140*days
def planeRideCost(city):
    if city == "Charlotte":
        return 183 
    if city == "Tampa":
        return 220 
    if city == "Pittsburgh": 
        return 222
    if city == "Los Angeles":
        return 475
def rentalCarCost(days):
    cost = days*40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost 
def tripCost(city,days,spendingMoney):
    return rentalCarCost(days) + hotelCost(days) + planeRideCost(city) + spendingMoney
print tripCost("Los Angeles",5,600)
 
------------------
 
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, and your favorite color is %s." % (name, quest, color)
 
------------------
 
from datetime import datetime
now = datetime.now()
print now
year = now.year
month = now.month
day = now.day
print day
print month 
print year
print str(day) + "/" + str(month) + "/" + str(year) 
print str(now.hour)+":"+str(now.minute)+":"+str(now.second)
 
------------------
 
import math
everything = dir(math)
print everything
 
------------------
 
def biggest_number(*args):
    print max(args)
    return max(args)
def smallest_number(*args):
    print min(args)
    return min(args)
def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)
biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
 
------------------
 
def shut_down():
    entry = raw_input("Entry: ")
    entry1 = "Yes"
    entry2 = "No"
    if entry == entry1 or entry == entry1.upper() or entry == entry2.lower():
        answer = "Shutting down..."
        return answer
    elif entry == entry2 or entry == entry2.upper() or entry == entry2.lower():
        answer == "Shutdown aborted!"
        return answer
    else:
        msg = "Sorry, I didn't understand you."
        return msg
 
 
def distance_from_zero(param):
    if type(param) == int or type(param) == float:
        return abs(param)
    else:
        msg = "This isn't an integer or a float!"
        return msg
distance_from_zero(100)
 
------------------
 
def favorite_actors(*args):
    """Prints out your favorite actorS (plural!)"""
    print "Your favorite actors are:" , args    
favorite_actors("Michael Palin", "John Cleese", "Graham Chapman")
 
------------------
 
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("swimming googles")
suitcase.append("watch")
suitcase.append("underwear")
#suitcase.append("nintendoDS")
# Your code here
list_length = len(suitcase)# length of `suitcase`
print "There are " + str(list_length) + " items in the suitcase."
print suitcase
 
------------------
 
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2] # the first two items
middle = suitcase[2:4] # third and fourth items
last = suitcase[len(suitcase)-2:len(suitcase)] # the last two items
 
------------------
 
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# `index()` to find "duck"
# Your code here
animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation
 
------------------
 
my_list = [1,9,3,8,5,7]
for number in my_list:
    # Your code here
    print number * 2
 
------------------
 
start_list = [5, 3, 1, 2, 4]
square_list = []
for elem1 in start_list:
    elem = elem1 ** 2
    square_list.append(elem)
    
square_list.sort()
# Your code here
print square_list
 
------------------
 
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']
# Your code here: Add some dish-price pairs to 'menu'
menu['teste1'] = 10.34
menu["teste2"] = 30.45
menu["teste3"] = 203.40
print menu["teste1"]
print "There are " + str(len(menu)) + " items on the menu."
print menu
 
------------------
 
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
# Your code here
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "testando"
print zoo_animals
 
------------------
 
inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 
# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50
 
------------------
 
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for z in names:
    print z
 
------------------
 
# vai printar o valor referente a key especificada no dicionario webster
Webster = {
     "Aardvark" : "A star of a popular children's cartoon show.",
     "Baa" : "The sound a goat makes.",
     "Carpet": "Goes on the Floor.",
     "Dab": "A small amount."
    }
for y in Webster:
    print Webster[y]   
 
------------------
 
_list = ["fizz" , "fizz", "fizz", "buzz"]
def fizzCount(x):
    count = 0
    for k in x:
        if k == "fizz":
            count = count + 1
    print count
    return count    
fizzCount(_list)
 
------------------
 
# strings sao como listas de caracteres
for c in "Codecademy":
    print c  
# Empty lines to make the output pretty
print
print
word = "Programming is fun!"
for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
 
------------------
 
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
for k in prices.keys():
    print k 
    print "price: " + str(prices[k])
    print "stock: " + str(stock[k])
 
------------------
 
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}   
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for key in prices:
    total = total + (prices[key] * stock[key])
print str(total)
 
------------------
 
groceries = ["banana", "orange", "apple"]
stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}   
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Write your code below!
def compute_bill(food):
    total = 0
    for each in food:
        if stock[each] > 0:
            total = total +  prices[each]
            stock[each] = stock[each] - 1
    #print "total = " + str(total)
    return total
 
#compute_bill(groceries)
 
------------------
 
def hotel_cost(nights):
    return nights * 140
 
bill = hotel_cost(5)
 
def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))
 
def make_payment(payment, balance):
    new_balance = payment - balance + add_monthly_interest(balance)
    return "You still owe: " + str(new_balance)
 
------------------
 
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
 
# Add your function below!
def average(list):
    return sum(list)/len(list)
    
def get_average(dic):
    return average(dic["homework"]) * 0.1 + average(dic["quizzes"]) * 0.3 + average(dic["tests"]) * 0.6
    
def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80 and score < 90: return "B"
    elif score >= 70 and score < 80: return "C"
    elif score >= 60 and score < 70: return "D"
    elif score < 60: return "F"
    
print get_letter_grade(get_average(lloyd))
 
------------------
 
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
 
# Add your function below!
def average(_list):
    return float(sum(_list))/len(_list)
    
def get_average(dic):
    return average(dic["homework"]) * 0.1 + average(dic["quizzes"]) * 0.3 + average(dic["tests"]) * 0.6
    
def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80 and score < 90: return "B"
    elif score >= 70 and score < 80: return "C"
    elif score >= 60 and score < 70: return "D"
    elif score < 60: return "F"
 
 
def get_class_average(class_list):
    aux = 0
    for dic in class_list:
        aux = aux + get_average(dic)
    return float(aux)/len(class_list)
    
students = [lloyd, alice, tyler]
 
print get_letter_grade(get_average(lloyd))
 
print get_class_average(students)
 
------------------
 
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]
 
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
 
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]
 
------------------
 
m = 5
n = 13
# Add add_function here!
def add_function(*args):
    return sum(args)
print add_function(m, n)
 
------------------
 
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print x[i]
    return
 
------------------
 
Method 1 - for item in list:
 
for item in list:
    print item
Method 2 - iterate through indexes:
 
for i in range(len(list)):
    print list[i]
Method 1 is a little easier, but can cause problems when trying to modify the list. Method 2 is much safer.
 
------------------
 
m = [1, 2, 3]
n = [4, 5, 6]
 
# Add your code here!
 
def join_lists(x, y):
    aux = []
    for i in range(0, len(x)):
        aux.append(x[i])
        if i == (len(x) - 1):
            for j in range(0, len(y)):
                aux.append(y[j])
    return aux
 
print join_lists(m, n)
 
------------------
 
m = [1, 2, 3]
n = [4, 5, 6]
o = [7, 8, 9]
 
# Update the below function to take
# an arbitrary number of arguments
def join_lists(*args):
    aux = []
    for i in range(0, len(args)):
        aux += args[i]
    return aux
 
print join_lists(m, n, o)
