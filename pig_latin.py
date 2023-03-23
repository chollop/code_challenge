import re

#Function that translates to Pig Latin
def translate(words):

    #Loop through the list of words
    for i, word in enumerate(words):
        #If the word starts with a vowel or 'y', append 'ay'
        if word[0] in 'aeiouy':
            words[i] = words[i]+ "ay"
        else:
            no_vowels = True
            #Check if any vowel is present in the word
            for j, letter in enumerate(word):
                if letter in 'aeiouy':
                    #Get the index position of the first vowel in the word and move the consonants in front to the end + append 'way'
                    words[i] = word[j:] + word[:j] + "way"
                    no_vowels = False
                    break

            #The word doesn't contain any vowel, simply append 'way'
            if(no_vowels == True):
                words[i] = words[i]+ "way"
    return words

#Read a string and convert all letters to lower
input_string = input('Enter a few words: ').lower() 

#Remove all punctuation from the previous string using regex
no_punctuation_input_string = re.sub(r'[^\w\s]', '', input_string)

#Split the string into a list of words 
english_words = no_punctuation_input_string.split()

#Translate string
pig_latin_words = translate(english_words)

#Capitalize each word in the returned list and join into a sentence
pig_latin = ' '.join(word.capitalize() for word in pig_latin_words)

print("Translation to Pig Latin: ",pig_latin)
