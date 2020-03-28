import math
import re
import string



#Finds if the number is a perfect square
def is_perfect_square(x):
    return x > -1 and math.sqrt(x) % 1 == 0


#This function gets a string song1 = "AWUBWUBWUBBWUBWUBWUBC"
#removes all WUB WUB-s replases them with " "
#and then removes all space headings, trailing, 
#and extra space created from removing multiple wubs

def decode_song(x):
    y = x.replace("WUB", " ")
    y = re.sub(' +', ' ', y)
    y = y.strip()
    return y
#This is another users submitions, much more cleaver
# does the same thing as the function above       
 
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())


#Given two integers a and b, which can be positive or negative, 
#find the sum of all the numbers between including them too and return it. 
#If the two numbers are equal return a or b.
#Note: a and b are not ordered!

def get_sum(a,b):
    sum = 0
    if a == b:
        return a
    if a > b:
        for x in range(b, a+1):
            print(x)
            sum += x
        return sum
     
    if b > a:
        for x in range(a, b+1):
            sum += x
        return sum

#This is a better, much shorter function than the above
# you can do the same thing if you substitute xrange with range()
# xrange returns an object while range() returns a list            
def better_get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))

#
#arr = [1, 2, 3, 2, 4]
#sub = [2]
#This outputs the first list without the items from the second list
def array_diff(a, b):
    list = [x for x in a if x not in b]
    return list  
#beni = "How can mirrors be real if our eyes aren't real"
#This function capitalises every word in a string
def capitalise_every_word(x):
    message = " ".join([word.capitalize() for word in x.split(" ")])
    return message
#While this is just a tiny bit shorter version than the one on top
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

def is_isogram(word): 
    # Convert the word or sentence in lower case letters. 
    clean_word = word.lower() 
    # Make an empty list to append unique letters 
    letter_list = [] 
    for letter in clean_word: 
        # If letter is an alphabet then only check 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter) 
  
    return True
#much shorter version of the code above
def check_isogram(string):
    return len(string) == len(set(string.lower()))


# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones 
# -- everytime you press the button it sends you an array of one-letter strings representing directions to walk 
# (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction
# and you know it takes you one minute to traverse one city block, 
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
# (you don't want to be early or late!) and will, of course, 
# return you to your starting point. Return false otherwise.

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


#Write a method that takes an array of consecutive (increasing) letters as input and 
# that returns the missing letter in the array.

#You will always get an valid array. And it will be always exactly one letter be missing. 
# The length of the array will always be at least 2.
#The array will always contain letters in only one case.

#Example:

#['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

# ord() gives the unicode for that character, and by going through the letters, if the unicode is not continuos
# we add the next unicode character, which is transformed

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter_v2(chars):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(chars[0])
    for i in range(len(input)):
        if not chars[i] == alphabet[start+i]:
            return alphabet[start+i]

#
#Create a function taking a positive integer as its parameter and returning a string 
# containing the Roman Numeral representation of that integer.
#Modern Roman numerals are written by expressing each digit separately starting with the left most 
# digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 
# 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; 
# or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI
def roman_number(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    # reverse the list
    for key in sorted(roman_numerals.keys(),reverse=True):
        # ex: while 6 > = 1
        while n >= key:
            # empty string is populated with 1
            roman_string += roman_numerals[key]
            # here we perform substraction 6-1 = 5, which will then go again into the loop
            n -= key
    return roman_string

# check if two strings are anagrams
# first argument is a single string, the second argument is a list of strings which we need to check
# which one is an anagram of the first one and put them into an array and return that array
def check_anagram(first, second):
    
    array = []
    for x in second:
        if sorted(first) == sorted(x):
            array.append(x)
    return array
# same function as the one above but shorter, using list compihension
def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]

# checking is a string is a pangram, a sentence which has all the letters of the alphabet
def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    letters = 0
    for x in range(len(alphabet)):
        if alphabet[x] in s.lower():
            letters +=1
    if letters == 26:
        return True
    else:
        return False

# the same function but shorter than the one above
def short_is_pangram(s):
#    return set(string.lower()) <= set(s.lower())
    pass


def is_prime(num):
    if num == 1 or num < 0:
        return False
    i = 2

    while i*i <= num:
        if num % i ==0:
            return False
        i += 1
    return True            

def decending_order(num):
    # Get a number ex. 12345 and returns the larges 
    # possible number with those digits
    return int("".join(sorted(str(num), reverse= True)))


def transform_letters_into_numbers(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) 
