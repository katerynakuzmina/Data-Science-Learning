# def better_than_average(class_points, your_points):
#     # Your code here
#     average_score = your_points
#     for score in class_points:
#         average_score += score

#     return average_score / (len(class_points) + 1) < your_points

# print(better_than_average([2, 3], 5))
# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))
# print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
# print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))

# def maps(a):
#     b = []
#     for num in a:        
#         b.append(num * 2)

#     return b

# def maps(a):
#     new_maps = [num * 2 for num in a]
#     return new_maps

# print(maps([1, 2, 3]))
# print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


# def str_count(strng, letter):
#     # Your code here ;)
#     count_letters = 0
#     for l in strng:
#          if l == letter:
#               count_letters += 1
#     return count_letters

# def str_count(strng, letter):
#     return strng.count(letter)


# print(str_count('hello', 'e'))
# print(str_count('codewars', 'c'))
# print(str_count('ggggg', 'g'))
# print(str_count('hello world', 'o'))
# print(str_count('', 'z'))



# def invert(lst):
#     new_list = []
#     for num in lst:
#         if num < 0:
#             new_list.append(abs(num)) 
#         else:
#             new_list.append(0 - num) 
#     return new_list

# def invert(lst):
#     return [-x for x in lst]

# print(invert([1,2,3,4,5]))
# print(invert([1,-2,3,-4,5]))
# print(invert([]))

# def shortcut(s):
#     shortcut_text = ''
#     for l in s:
#         if l.islower() and ((l == 'a') or (l =='e' ) or (l == 'i') or (l == 'o') or (l =='u')):
#             continue
#         else:
#             shortcut_text += l
#     return shortcut_text

# print(shortcut("hello"))
# print(shortcut("hellooooo"))
# print(shortcut("how are you today?"))
# print(shortcut("complain"))
# print(shortcut("never"))


# def people_with_age_drink(age):
#     drink_for_who = ''
#     if age < 14:
#         drink_for_who = "drink toddy"
#     elif (age >= 14 and age < 18):
#         drink_for_who = "drink coke"
#     elif (age >= 18 and age < 21):
#         drink_for_who = "drink beer"
#     else:
#         drink_for_who = "drink whisky"
#     return drink_for_who

# def people_with_age_drink(age):
#     return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')

# print(people_with_age_drink(13))
# print(people_with_age_drink(17))
# print(people_with_age_drink(20))
# print(people_with_age_drink(21))


# def move(position, roll):
#     # your code here
#     return position + (roll * 2)


# print(move(0, 4))
# print(move(3, 6))
# print(move(2, 5))


# def check(seq, elem):
#     return seq.__contains__(elem)

# def check(seq, elem):
#     return elem in seq

# print(check([66, 101], 66)),
# print(check ([78, 117, 110, 99, 104, 117, 107, 115], 8))
# print(check([101, 45, 75, 105, 99, 107], 107))
# print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
# print(check(['t', 'e', 's', 't'], 'e'))
# print(check (["what", "a", "great", "kata"], "kat"))
# print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))
# print(check (["come", "on", 110, "2500", 10, '!', 7, 15], "Come"))
# print(check(["when's", "the", "next", "Katathon?", 9, 7], "Katathon?"))
# print(check ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45))
# print(check(["anyone", "want", "to", "hire", "me?"], "me?"))



# def other_angle(a, b):
#     return 180 - a - b

# print(other_angle(30, 60))
# print(other_angle(60, 60))
# print(other_angle(43, 78))
# print(other_angle(10, 20))


# def count_sheeps(sheep):
#     return sheep.count(True)

# print(count_sheeps([True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True]))


# def positive_sum(arr):
#     # my_sum = 0
#     # for num in arr:
#     #     if num > 0:
#     #         my_sum += num
#     # return my_sum
#     return sum(x for x in arr if x > 0)
    

# print(positive_sum([-1,-2,-3,-4,-5]))
# print(positive_sum([1,-2,-3,4,-5]))
# print(positive_sum([-1,2,-3,4,5]))


# def find_multiples(integer, limit):
#     new_list = []
#     new_int = integer
#     while new_int <= limit:
#         if new_int % integer == 0:
#             new_list.append(new_int)
#         new_int +=1
#     return new_list  

# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))

# print(find_multiples(5, 25)) #[5, 10, 15, 20, 25]
# print(find_multiples(1, 2)) #[1, 2]


# a = [2, 3, 10]
# print(max(a))

# import itertools


# def expression_matter(a, b, c):
#     list_perm = []
#     for perm in itertools.permutations([a, b, c]):
#         list_perm.append(perm)
#     return max(list_perm)

# print(expression_matter(2, 1, 2)) #6  
# print(expression_matter(2, 1, 1)) #4
# print(expression_matter(2, 1, 2)) #6
# print(expression_matter(2, 2, 4)) #16
# print(expression_matter(3, 3, 3)) #27
# print(expression_matter(1, 1, 1)) #3
# print(expression_matter(1, 2, 3)) #9
# print(expression_matter(1, 3, 1)) #5
# print(expression_matter(10, 5, 6)) #300
# print(expression_matter(1, 10, 1)) #12

# my_str = 'kaTya'
# new_str = ''
# for l in my_str:
#     new_str += l
#     print(l.isupper)
# print(new_str)

# def is_isogram(string):
#     string = string.upper()
#     if len(string) == 0:
#         return True
#     new_str = ''
#     for letter in string:
#         if string.count(letter) == 1:
#             new_str += letter
#     print(new_str)
#     return string == new_str
# print(is_isogram("Dermatoglyphics")) #True
# print(is_isogram("isogram")) #True
# print(is_isogram("aba")) #False "same chars may not be adjacent" 
# print(is_isogram("moOse")) #False "same chars may not be same case"
# print(is_isogram("isIsogram")) #False
# print(is_isogram("")) #True "an empty string is a valid isogram"


# def open_or_senior(data):
#     my_list = []
#     for item in data:
#         if item[0] >= 55 and item[1] > 7:
#             my_list.append('Senior')
#         else:
#             my_list.append('Open')
#     return my_list

# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
# print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))


# def printer_error(s):
#     a = 0
#     # liters = 'abcdefghijklm'
#     for i in s:
#         if not 'abcdefghijklm'.__contains__(i):
#             a +=1 
#     return f"{a} / {len(s)}"
# from re import sub
# def printer_error(s):
#     return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
# # s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# # print(printer_error(s))#"3/56"
# # s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# # print(printer_error(s)) #"6/60"
# s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
# print(printer_error(s)) #"11/65"


# def how_much_i_love_you(nb_petals):
#     # your code
#     result = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
#     if nb_petals <= 6:
#         return result[nb_petals - 1]
#     while (nb_petals - 6) > 6:            
#         nb_petals -= 6
#     return result[(nb_petals - 6) - 1]

# def how_much_i_love_you(nb_petals):
#     return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

# print(how_much_i_love_you(7)) #"I love you"
# print(how_much_i_love_you(4)) #"I love you"
# print(how_much_i_love_you(8)) #"I love you"
# print(how_much_i_love_you(3)) #"a lot"
# print(how_much_i_love_you(6))  # "not at all"
# print(how_much_i_love_you(12))  # "not at all"
# print(how_much_i_love_you(13))  # "I love you"

# a = 'abc'
# b = reversed(a)
# print(''.join(b))

# a = 'The quick brown fox jumps over the lazy dog.'
# print(a.split())

# import re
# def reverse_words(text):
#     parts = re.split(r'(\s+)', text)
#     reversed_words = [part[::-1] if not part.isspace() else part for part in parts]
#     return ''.join(reversed_words)

# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))


# print(reverse_words('The quick brown fox jumps over the lazy dog.'))
# print(reverse_words('apple'))
# print(reverse_words('a b c d'))
# print(reverse_words('  double  spaced  words  '))

# def nb_dig(n, d):
#     i = 0
#     my_list = []
#     while i <= n:
#         k = i * i        
#         my_list.append(k)
#         i += 1
#     value_count = 0
#     for num in my_list:
#         value_count += int(str(num).count(str(d)))
#     return value_count

# def nb_dig(n, d):
#     return sum(str(i*i).count(str(d)) for i in range(n+1))

# print(nb_dig(5750, 0))
# print(nb_dig(11011, 2))
# print(nb_dig(12224, 8))
# print(nb_dig(11549, 1))

# def rental_car_cost(d):
#     if d  >= 7:
#         return (d*40)-50    
#     if d >= 4:
#         return (d*40)-20
#     return d*40

# print(rental_car_cost(1))
# print(rental_car_cost(4))
# print(rental_car_cost(7))
# print(rental_car_cost(8))


# def double_char(s):
#     # new_str = ''
#     # for l in s:
#     #     new_str += l + l
#     # return new_str
#     return ''.join(l + l for l in s)
# print(double_char("String"))


# def grow(arr):
#     num = 1
#     for i in arr:
#         num *= i
#     return num

# print(grow([1, 2, 3]))


# def calculate_years(principal, interest, tax, desired):  
#     qty_years = 0

#     if principal == desired:
#         return qty_years

#     while principal < desired:
#         principal += ((principal * interest) - ((principal * interest) * tax))
#         qty_years +=1
#     return qty_years

# print(calculate_years(1000, 0.05, 0.18, 1100))
# print(calculate_years(1000,0.01625,0.18,1200))
# print(calculate_years(1000,0.05,0.18,1000))


# def is_anagram(test, original):
#     test1 = sorted(test.lower())
#     original1 = sorted(original.lower())

#     if test1 == original1:
#         return (True, f'The word {test} is an anagram of {original}')

#     if set(test1) == set(original1):
#         return (False, "Same letters, but different count")
    
#     return (False, f'Missing characters for test case {test}, {original}')

# def is_anagram(test, original):
#     return sorted(test.lower()) == sorted(original.lower())

        
# print(is_anagram("foefet", "toffee"))  #, True, 'The word foefet is an anagram of toffee'
# print(is_anagram("Buckethead", "DeathCubeK")) #  , True, 'The word Buckethead is an anagram of DeathCubeK'
# print(is_anagram("Twoo", "WooT")) #, True, 'The word Twoo is an anagram of WooT'
# print(is_anagram("dumble", "bumble")) #, False, 'Characters do not match for test case dumble, bumble'
# print(is_anagram("ound", "round")) #, False, 'Missing characters for test case ound, round'
# print(is_anagram("apple", "pale")) #, False, 'Same letters, but different count'


# def min_max(lst):
    # return [sorted(lst)[0], sorted(lst)[-1]]

# def min_max(lst):
#     return [min(lst), max(lst)]

# print(min_max([1,2,3,4,5])) #, [1, 5]
# print(min_max([2334454,5])) #, [5, 2334454]



# def paperwork(n, m):
#     if n <= 0 or m <= 0:
#         return 0

#     return n * m

# print(paperwork(5,5))
# print(paperwork(1,2))
# print(paperwork(-5,5))
# print(paperwork(5,-5))
# print(paperwork(-5,-5))
# print(paperwork(5,0))


# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]

# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

# print(sum_two_smallest_numbers([5, 8, 12, 18, 22])) #13
# print(sum_two_smallest_numbers([7, 15, 12, 18, 22])) #19
# print(sum_two_smallest_numbers([25, 42, 12, 18, 22])) #30

# a = [4, 1, 7, 2, 3]
# a.sort()
# print(a)
# print(a[0])
# print(a[0] + a[1])



#Two fighters, one winner
# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.
# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
# Your function also receives a third argument, a string, with the name of the fighter that attacks first.
# class Fighter(object):
#     def __init__(self, name, health, damage_per_attack):
#         self.name = name
#         self.health = health
#         self.damage_per_attack = damage_per_attack
        
#     def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#     __repr__=__str__

# def declare_winner(fighter1, fighter2, first_attacker):
#     def fight(first_attacker, second_attacker):
#         while first_attacker.health > 0 and second_attacker.health > 0:
#            second_attacker.health -= first_attacker.damage_per_attack
#            if second_attacker.health <= 0:
#                 return first_attacker.name
#            first_attacker.health -= second_attacker.damage_per_attack
#            if first_attacker.health <= 0:
#                 return second_attacker.name
#     if first_attacker == fighter1.name:
#         return fight(fighter1, fighter2)
#     else:
#         return fight(fighter2, fighter1)
            
        
# print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")) #Lew
# print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")) #Harald
# print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry")) #Harald        
# print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald")) #Harald        
# print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry")) #Harald            
# print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald")) #Harald


# def unusual_five():
#     return len('aaaaa')

# print(unusual_five())


# def friend(x):
#     def check_friend(elem):
#         return len(elem) == 4
#     return list(filter(check_friend, x))

# print(friend(["Ryan", "Kieran", "Mark",]))#, ["Ryan", "Mark"]
# print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))#, ["Ryan"]
# print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))#, ["Jimm", "Cari", "aret"]


# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

# def to_alternating_case(string):
#     return ''.join(l.upper() if l.islower() else l.lower() for l in string)

# def to_alternating_case(string):
#     return string.swapcase()


# print(to_alternating_case("hello world"))
# print(to_alternating_case("hello WORLD"))
# print(to_alternating_case("HELLO WORLD"))
# print(to_alternating_case("HeLLo WoRLD"))
# print(to_alternating_case("12345"))
# print(to_alternating_case("1a2b3c4d5e"))
# print(to_alternating_case("String.prototype.toAlternatingCase"))
# print(to_alternating_case(to_alternating_case("Hello World")))



# Twice as old
# Your function takes two arguments:
# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

# def twice_as_old(dad_years_old, son_years_old):
#     return dad_years_old - 2*son_years_old
         
    
# print(twice_as_old(36,7)) #22
# print(twice_as_old(55,30)) #5
# print(twice_as_old(42,21)) #0
# print(twice_as_old(22,1)) #20
# print(twice_as_old(29,0)) #29


# Summing a number's digits
# Description:
# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

# For example: (Input --> Output)
# 10 --> 1
# 99 --> 18
# -32 --> 5

# a = 542
# for n in str(a):
#     print(int(n))
#     print(type(int(n)))

# def sum_digits(number):
#     count = 0
#     for num in str(abs(number)):
#         count += int(num)
#     return count

# def sum_digits(number):
#     return sum(int(num) for num in str(abs(number)))

# print(sum_digits(10))
# print(sum_digits(99))
# print(sum_digits(-32))
# print(sum_digits(1234567890))
# print(sum_digits(0))
# print(sum_digits(666))
# print(sum_digits(100000002))
# print(sum_digits(800000009))


# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# def even_or_odd(number):
#     return ('Even' if number % 2 == 0 else 'Odd')

# print(even_or_odd(1))
# print(even_or_odd(-1))
# print(even_or_odd(2))
# print(even_or_odd(-2))
# print(even_or_odd(7))
# print(even_or_odd(8))
# print(even_or_odd(10))

# Highest and Lowest
# Description:
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5") # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    new_list = list(int(n) for n in numbers.split())
    return (f"{max(new_list)} {min(new_list)}")

print(high_and_low('5 -3 1 8 0'))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))