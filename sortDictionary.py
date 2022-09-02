# ------------------------------------- Program Information


"""
Author: Johanna Swirski
See README for project description

--- Code Overview ---

This is the python file that is used to process the JSON dictionary.
All words that are more than 9 letters long are removed.

Original JSON file is provided by the following Github repo:
https://github.com/dwyl/english-words
"""


# ------------------------------------- Program Initialisation and Start


import json

# Open the JSON dictionary and load in the data
originalFile = open('words_dictionary.json')
completeDictionaryOfWords = json.load(originalFile)
useableDictionaryOfWords = []

# Cycle through the JSON data and save words less than 9 letters long to a new list
for i in completeDictionaryOfWords.keys():
    if len(i) < 10 :
        useableDictionaryOfWords.append(i)
originalFile.close

# Convert recovered data to JSON and save it to a new file
newDictionary = json.dumps(useableDictionaryOfWords)
newFile = open("newDictionary.json", "x")
newFile.write(newDictionary)
newFile.close