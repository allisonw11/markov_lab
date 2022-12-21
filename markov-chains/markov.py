"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
 #Within the skeleton provided, 
 # finish the function that opens the file_path for our green-eggs.txt file and spits out its contents as a string.
    #pseudocode:
        #create a container variable that holds the opened information from the given file 
        # and uses the read method in order to create the entire contents as a single string
    
    contents = open(file_path).read()

    return contents

#===============================================================================================================
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

input: given text distilled down as one long string
output: dictionary of markhov chains

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]

    1. use string.split() to separate it by whitespace. words = contents.split() x
    2. loop over each word pair - loop over the list by index, rather than item directly x
    3. print out each word pair. But we also need to keep track of every word that follows each pair of words, 
        wherever the pair appears in the text.

        1. Make an empty dictionary. ( DO WE NEED TO HAVE A SECOND DICTIONARY VARIABLE AFTER THE CHAINS?) x

        2. Loop over the words in the list of words, making sure you can access the
            word at i, i+1, and i+2 without bumping up against an IndexError at the end. x
        
        3. Modify the loop so that you’re putting the words at i and i+1 in a tuple, 
                    words = [('i', 'i + 1'), (x), (y)...] -> becomes the key to a dictionary
                    fruit = ('ripe', 'Red Delicious')
                >>> fruit[0]
                'ripe'

                >>> for attribute in fruit:
            ...     print(attribute)
            
            and then use that tuple as a key in your dictionary. x

        4. If we assign the word at i+2 as the value to our key, we’ll overwrite
            the value every time we find another instance of that word pair in our text. 
            So instead, let’s create a list as the value and append words into it. -> so we're throwing stuff into a list so we can pull from it

        5. But when do you make an empty list and when do you append into it? x
            Check to see if the key is in the dictionary already. 
                if

            If it’s not, make sure you initialize that list and put your word into it. 
            If the key is already in the dictionary, append your word to the list that’s already there.

            To append an element to an existing dictionary, 
                you have to use the dictionary name followed by square brackets 
                with the key name and assign a value to it.

Example from Bethany:
chains = {}
for i in range(len(text_string) - 2): #gets rid of last items
        green_eggs = (text_string[i], text_string[i + 1]) #made into tuple - set to this variable 
        if green_eggs in chains: # Appending the value to an existing key 
            chains[green_eggs].append(text_string[i+2])
        else: # Creating a new key 
            chains[green_eggs] = [text_string[i+2]] #tuple became key (green_eggs), value set to word after tuple
        #dict[key] = [string[value]] means key and value
        #had an error because - 2 had to match +2 so that it didnt loop farther than the list

    """

#can't call split on a functio want to call on the string that is passed in
    words = text_string.split()
    #i -> the number of words within words
    #range will print from index 0 through to however many number of words there are 
        #the -1 is the stop sign, cant go beyond
        #print the first word (i) and then the next word (i + 1)
    #loop again to the next 2 words
        
    chains = {}
    print(words)
    for i in range(len(words) - 2):
        #in the instructions there were no () after print but then we used them to get rid of the red squiggly line of death

        chains[(words[i], words[i+1])]= [(words[i+2])]
        # fruits = {'a':1, 'b':2, 'c':3}
        # fruits['c'] = 4
    return chains
#when looping over an index, don't use "word", better to use i to understand the indexes, 
# go from 0 - 1 before last index in list
    
#===============================================================================================================
def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
# 

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)
