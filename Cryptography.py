
# coding: utf-8

# In[1]:


import string
import random
import sys


# In[2]:


WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    #print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    #print("  ", len(wordList), "words loaded.")
    return wordList


# In[3]:


def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


# In[4]:


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lower=string.ascii_lowercase
    #abcdefghijklmnopqrstuvwxyz
    upper=string.ascii_uppercase
    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    shiftdict={}
    for i in range(26):
        shiftdict[upper[i]]=upper[(i+shift)%26]
    for i in range(26):
        shiftdict[lower[i]]=lower[(i+shift)%26]
    return shiftdict
#print(buildCoder(3))


# In[5]:


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newtext=""
    for i in range(len(text)):
        if text[i].isalpha():
            newtext+=coder[text[i]]
        else:
            newtext+=text[i]
    return newtext
#print(applyCoder("Hello, World!",buildCoder(3)))
#print(applyCoder("Khoor, zruog!", buildCoder(23)))


# In[6]:


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### A wrapper function.
    return applyCoder(text,buildCoder(shift))


# In[7]:


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    old_valid_words_count=0
    count=len(text.split(' '))
    shift=0
    while shift<26:
        new_valid_words_count=0
        newtext=applyShift(text,shift)
        words=newtext.split(' ')
        for word in words:
            if isWord(wordList,word):
                new_valid_words_count+=1
        if old_valid_words_count<new_valid_words_count:
            old_valid_words_count=new_valid_words_count
            key=shift
        if old_valid_words_count==count:
            break
        shift+=1
        
    return (key)
#print(findBestShift(wordList, "Pmttw, ewztl!"))


# In[8]:


def decryptStory(text):
    """
    text: encrypted Text
    returns: string - text in plain text
    """
    wordList=loadWords()
    shift=findBestShift(wordList,text)
    return applyShift(text,shift)


# In[10]:


if __name__ == '__main__':
    choice=input("1 for encryption, 2 for decryption, 3 for exit: ")
    if choice=="1":
        text=input("Enter Text to Encrypt: ")
        key=int(input("Enter Shift (Encryption) key (0-25): "))
        s = applyShift(text, key)
        print("\nEncrypted Text:\n",s)
    elif choice=="2":
        text=input("Enter Text to Decrypt: ")
        print("\nDecrypted Text:\n",decryptStory(text))
    elif choice=="3":
        pass

