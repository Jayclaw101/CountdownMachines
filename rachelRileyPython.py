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
"""

def main():
    userOption = input("Select a game:/nAnagrams: A/nNumbers: N/nConundrum: C/nFull Episode: E/nQuit: Q").upper()
    match userOption:
        case "A":
            print("TBC")
        case "N":
            print("TBC")
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

print("Welcome to Countdown!/n")
main()
