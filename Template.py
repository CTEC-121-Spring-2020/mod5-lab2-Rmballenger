"""
CTEC 121
Robert Ballenger
Module 5 Lab 2
The wierd finger song.
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

'''
# Practice 1

def main():
    weirdSong("Daddy")
    weirdSong("Mommy")
    weirdSong("Brother")
    weirdSong("Sister")
    weirdSong("Baby")

def weirdSong(name):
    print(name, "finger,", name, "finger, where are you?\nHere I am, here I am. How do you do?\n")
    
main() 
'''
# Practice 2

def testAge(age):
    if age >= 0 and age <= 1:
        classification = "I"
        meaning = "Infant."
    if age > 1 and age < 13:
        classification = "C"
        meaning = "Child."
    if age >= 13 and age < 18:
        classification = "T"
        meaning = "Teenager."
    if age >= 18 and age < 120:
        classification = "A"
        meaning = "Adult."
    if age < 0 or age >= 120:
        classification = "U"
        meaning = "Unknown."
    
    resultAge(classification, meaning, age)

def resultAge(classification, meaning, age):
    print("Your age of", age, "is classified as", classification, "which means", meaning)

def unitTest():
    for i in range (20):
        testAge(i)
    testAge(-1)
    testAge(150)

def main():
    unitTest()

    '''
    ageGiven = int(input("What is your age? "))
    testAge(ageGiven)
    '''
    
main()

