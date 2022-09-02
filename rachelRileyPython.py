# ------------------------------------- Program Information


"""
Author: Johanna Swirski
See README for project description

--- Code Overview ---

In main, introduce program, send user to each game

For Anagrams:
    Let user choose cosonants and vowels
    Set Timer (if possible play sound?)
    (Do we let user input their answers? Just their longest? Do we include a point system in that case?)
    Work out all possible words (give user the option to see all words?)
    Display 1 longest possible word
    Replay or back to menu

For Numbers Game:
    Let user choose small and large numbers
    Pick random three digit number
    Work out closest solution
    Set Timer (same as before)
    (Let user input their answer? With solution?)
    Display closest solution
    Replay or back to menu

For Conundrum:
    Randomly choose 1 nine letter word and shuffle it
    Set Timer (same as before)
    (Let user interrupt timer to input answer, if timer ends they don't get points - would point system reset?)
    Display answer
    Replay or back to menu

For Point System:
    Could select the option to play for a full episode
    Go through the games as if it was an episode and track points
    High score system (Two player?)

Notes:
    Consider adding probability for different letters (q is not nearly as common as s)
        Base off of statistics for how often letters appear in english?
    Get rid of all traces of recursion
    Give credit to github https://github.com/dwyl/english-words for json dictionary
    Make lists of numbers more programmatical
"""


# ------------------------------------- Program Initialisation


import random
import json

# Main function - allow user to select a game to play
def main():
    userOption = input("Select a game:\nAnagrams: A\nNumbers: N\nConundrum: C\nFull Episode: E\nQuit: Q\n").upper()
    match userOption:
        case "A":
            anagramGame()
        case "N":
            numbersGame()
        case "C":
            print("TBC")
        case "E":
            print("TBC")
        case "Q":
            print("Thanks for playing!")
            return
        case other:
            print("Please input a valid option")
            main()

# Generate a random consonant
def randomConsonant():
    consonants = "bcdfghjklmnpqrstvwxyz"
    #consonants = string.ascii_lowercase.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    letter = random.choice(consonants)
    return letter

# Generate a random vowel
def randomVowel():
    vowels = "aeiou"
    letter = random.choice(vowels)
    return letter

# Find the longest word length in the set
def longestWord(allAnagrams):
    longestWord = allAnagrams[0]

    for i in allAnagrams:
        if len(longestWord) < i:
            longestWord = i

    longestWordLength = len(longestWord)
    return longestWordLength

# Print all words of the maxium length
def allLongestWords(allAnagrams, longestWordLength):
    allLongestWordsList = []

    for i in allAnagrams:
        if len(i) == longestWordLength:
            allLongestWordsList.append(i)

    return allLongestWordsList


# Solve all possible words from the anagrams
def anagramSolver():
    print("Anagram solver to come")
    # Find all anagrams, send them to a method to track the largest
    """
    Set for all anagrams
    Empty set that will copy each letter
    Set that will have all anagram letters
    Remove letters from "empty set" as they are located in the "anagram set"
    If the set is empty after a full iteration of the anagram set, add dictionary.item (i) to the "set for all anagrams"
    """
    return

# Anagram Game function - logic handling overarching plot for the anagram game
def anagramGame():
    print("Please select the 9 types of letter you want:\nVowel: V\nConsonants: C\n")
    anagram = ""
    x = 1
    while x < 10:
        choice = input(f"{x}/9:  ").upper()
        letter = ""
        match choice:
            case "V":
                letter = randomVowel()
                x += 1
            case "C":
                letter = randomConsonant()
                x += 1
            case other:
                print("Please input a valid option")
        if letter != "":
            anagram = anagram + letter
            print(anagram)
    print("\nThe final anagram is: ", anagram, "\n")
    anagramSolver()
    return

# Generate a random large numbers and track which numbers are left
def largeNumbers(largeNumbersList):
    # Limited 4 numbers - choose one and there are three left
    return

# Generate a random small numbers and track which numbers are left
def smallNumbers(smallNumbersList):
    # Two of each number, 1 - 10
    return

# Calculate the solution (best possible answer) to the numbers problem
def numbersSolver():
    return

# Numbers Game function - logic handling overarching plot for the numbers game
def numbersGame():
    print("Please select the 6 numbers you want:\nLarge: L\nSmall: S\n")
    numbersList = ""
    largeNumbersList = "25", "50", "75", "100"
    smallNumbersList = "1", "1", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "8", "8", "9", "9", "10", "10",
    x = 1
    while x < 7:
        choice = input(f"{x}/6:  ").upper()
        number = ""
        match choice:
            case "L":
                number = largeNumbers(largeNumbersList = largeNumbersList)
                x += 1
            case "S":
                number = smallNumbers(smallNumbersList = smallNumbersList)
                x += 1
            case other:
                print("Please input a valid option")
        if number != "":
            numbersList = numbersList + number
            print(numbersList)
    print("\nThe final numbers are: ", numbersList, "\n")
    numbersSolver()
    return


# ------------------------------------- Program Start


print("Welcome to Countdown!\n")
main()
