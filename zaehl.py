# !/usr/bin/env python3

# Aufgabe 8.3 (Textdatei lesen, Dictionaries, sortieren, argv)

import sys

file = open(sys.argv[1], "r")
content = file.read().lower() # Groß- und Kleinschreibung egal
scontent = content.split()
dlength = len(scontent)

def count_words(wordlist):
    wordCounter = {}
    for word in wordlist:
        if word in wordCounter:
            continue
        wordCounter[word] = wordlist.count(word)
    # wordCounter sortieren
    wordCounter = sortCounter(wordCounter)
    return wordCounter

def count_chars(wordlist):
    charCounter = {}
    charList = []
    for word in wordlist:
        charList.extend(list(word))

    for char in charList:
        if char in charCounter:
            continue
        charCounter[char] = charList.count(char)
    # charCounter sortieren
    charCounter = sortCounter(charCounter)

    return charCounter

def sortCounter(counter):
    sorted_Values = sorted(counter.values(), reverse=True)
    sorted_Keys = {}
    for v in sorted_Values:
        for k in counter.keys():
            if counter[k] == v:
                sorted_Keys[k] = counter[k]
                break
    return sorted_Keys


def print25(sortedCounter):
    keys = list(sortedCounter.keys())
    for i in range(25):
        if i > len(keys)-1:
            break
        print(keys[i], " : " ,sortedCounter.get(keys[i]))

print(dlength)
words = count_words(scontent)
chars = count_chars(scontent)
print("häufigste Wörter: ") 
print25(words)
print("häufigste Chars: ")
print25(chars)

