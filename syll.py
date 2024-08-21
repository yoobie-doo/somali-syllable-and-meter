#@title libraries and imports

# import pandas as pd
# import numpy as np
import io
import sys
import re
import os


#@title consonant and vowel definitions

# orthographic inventory of standard Maxaa dialect Somali

ALL_LETTERS        = ["'", "b", "t", "j", "x", "kh", "d", "r", "s", "sh", 
                      "dh","c", "g", "f", "q", "k", "l", "m", "n", "w", "h", "y", 
                      "a", "i", "u", "e", "o", "aa", "ii", "uu", "ee", "oo", 
                      "ay", "aw", "ey", "oy", "ow", "aay", "aaw", "eey", "ooy", "oow"]

CONSONANTS         = ["'", "b", "t", "j", "x", "kh", "d", "r", "s", "sh", "dh",
                      "c", "g", "f", "q", "k", "l", "m", "n", "w", "h", "y"]

CONS_DIGRAPH       = ["kh", "sh", "dh"]

CONS_BAR_DIGRAPHS  = [["'", "b", "t", "j", "x", "d", "r", "s", "c", "g", 
                       "f", "q", "k", "l", "m", "n", "w", "h", "y"]]

# defining all vowel variations
SHORT_VOWELS       = ["a", "i", "u", "e", "o"]
LONG_VOWELS        = ["aa", "ii", "uu", "ee", "oo"]

VOLATILE_DIPHTH    = ["ay", "aw", "ey", "oy", "ow"]
LONG_DIPHTH        = ["aay", "aaw", "eey", "ooy", "oow"]

# defining vowel short hands
DIPHTHONGS         = ["ay", "aw", "ey", "oy", "ow", "aay", "aaw", "eey", "ooy", "oow"]
VOWELS_BAR_DIPHTH  = ["a", "i", "u", "e", "o", "aa", "ii", "uu", "ee", "oo"]

VOWELS_INCL_DIPHTH = ["a", "i", "u", "e", "o", "aa", "ii", "uu", "ee", "oo", 
                      "ay", "aw", "ey", "oy", "ow", "aay", "aaw", "eey", "ooy", "oow"]

UNKNOWN_LENGTH     = "?"


#@title valid word

def is_valid_word(word):
    if not isalpha(word):
        return false

for x in (ALL_LETTERS):
    print(x, " ")


#@title split_into_syllables

# name:        split_into_syllables
#
# inputs:      a word
#
# return:      a list of the syllables in word
#
# description: create a list of syllables from a given 
#              word in standard Maxaa dialect Somali
#
# notes:       consonant clusters are >=3 consonants are ignored
#              and no error is raised, even though they break 
#              standard Somali orthography

def split_into_syllables(word):

    syllables = []
    curr_char = ""
    i = 0

    index_last_char = len(word)

    while i < len(word):

           
            # check against indexing out of range
            if (i == index_last_char - 1):
                    curr_char += word[i]
                    i += 1

            # Check if current character is a consonant cluster (sh, kh, dh)
            elif word[i:i+2] in CONS_DIGRAPH:  # (shouldn't the check be this then??)
            # elif word[i:i+2] in CONSONANTS:
                curr_char += word[i:i+2]
                i += 2

            elif word[i] in CONSONANTS:
                curr_char += word[i]
                i += 1
            
            elif word[i] not in ALL_LETTERS:
                curr_char += word[i]
                print("error, there seem to be non-Somali letters:", word[i])
                i += 1


            # Check if current character is a vowel
            if word[i:i+3] in VOWELS_BAR_DIPHTH:

            # If the current syllable is not empty
            # and the next character is a vowel
                # add the current syllable to the list and reset it
                if ((curr_char) and (i + 3 < len(word)) and (word[i+3] in VOWELS_BAR_DIPHTH)):
                    syllables.append(curr_char)
                    curr_char = ""
                
                curr_char += word[i:i+3]
                i += 3

            elif word[i:i+2] in VOWELS_BAR_DIPHTH:
                curr_char += word[i:i+2]
                i += 2

            elif (i != index_last_char):
                if (word[i] in VOWELS_BAR_DIPHTH):
                    curr_char += word[i]
                    i += 1

          # Add the current syllable to the list and reset
            if curr_char:  # if curr_char not empty             
                syllables.append(curr_char)
                curr_char = ""

    # correct error coda consonants are incorrectly
    # indexed on their own and trail behind

    corrected_syllables = correct_codas(syllables)
    return syllables



#@title correct_codas

# name:           correct_codas
#
# inputs:         a list of syllables that
#
# return:         the corrected list of syllables
#
# description:    picks up trailing consonants and attaches them
#                 to the previous syllable as its coda

def correct_codas(syllabified_word):

    counter = 0
    new_word = ""

    for i in syllabified_word:
        if i in CONSONANTS:
            if counter == 0:
                #preserve 0th index initial consonant cluster
                new_word = i + syllabified_word[counter + 1]
                syllabified_word[counter + 1] = new_word
        
            else:
                new_word = syllabified_word[counter - 1] + i
                syllabified_word[counter - 1] = new_word

            syllabified_word.remove(i)
            new_word = ""

        counter += 1
    return syllabified_word



#@title parser

# name:           parser
#
# inputs:         string
#
# return:         properly syllabified string
#
# description:    take any string in standard Maxaa-dialect Somali and
#                 parse it into a list of syllables
#

def parser(line):
    line = line.lower()
    # remove all non-alphabet characters
    regex = re.compile('[^a-zA-Z\' ]')
    line = regex.sub(' ', line)

    word_arr = line.split()

    parsed_line = []
    for word in word_arr:
        syllables = split_into_syllables(word)
        parsed_line += syllables

    # unsure why I need to correct here?
    # leave as is for now
    parsed_line = correct_codas(parsed_line)
    return parsed_line



#@title count_morae

# name:           count_morae
#
# inputs:         list of syllables
#
# return:         list of their moraic length
#
# description:    take a list of syllables and return their
#                 length (short: 1) or (long: 2)
#
# note:           diphthongs unimplemented and so they're
#                 rendered as '?' since they can very in
#                 length depending on several factors

def count_morae(parsed_line):
    morae_list = []
    index = 0
    for syl in parsed_line:
        # if LONG_DIPHTH in syl:
        if any(s in syl for s in LONG_DIPHTH):
            morae_list.append(2)


        # if VOLATILE_DIPHTH in syl:
        elif any(s in syl for s in VOLATILE_DIPHTH):

          # TODO: implement function to identify diphthong lengths
            morae_list.append(UNKNOWN_LENGTH)


        # if LONG_VOWELS in syl:
        elif any(s in syl for s in LONG_VOWELS):
            morae_list.append(2)


        # if SHORT_VOWELS in syl:
        elif any(s in syl for s in SHORT_VOWELS):
            morae_list.append(1)

    return morae_list






#@title sum_morae

# name:           sum_morae
#
# inputs:         list of morae
#
# return:         number of unknown morae and sum of the list
#
# description:    sums the total length of syllables in a line
#                 and indentify number of unknown syllables
#
def sum_morae(morae_list):
    sum = 0
    unknown_morae = 0
    for mora in morae_list:
        if mora == UNKNOWN_LENGTH:
            unknown_morae += 1
        else:
            sum += mora
    return unknown_morae, sum






#@title has_onset

# name:           has_onset
#
# inputs:         a syllable
#
# return:         true if syllable has a consonant onset, false othewise
#
# description:    checks if a syllable has a consonant onset
#
# note:           prints error if onset undetermined

def has_onset(syllable):

    syl_len = len(syllable)
    if syl_len in [0, 1]:
        return False

    if syl_len >= 3:
        if (syllable[0] in CONSONANTS or
           (syllable[:1]) in CONS_DIGRAPH):
           return True

    elif syl_len == 2:
        if (syllable[0] in CONSONANTS):
            return True

    print("Error: [", syllable, "] onset not deterimined")
    return False





#@title has_coda

# name:           has_coda
#
# inputs:         a syllable
#
# return:         true if syllable has a consonant coda, false othewise
#
# description:    checks if a syllable has a consonant coda
#
# note:           prints error if coda undetermined

def has_coda(syllable):
    syl_len = len(syllable)

    if syl_len in [0, 1]:
        return False

    if syl_len > 2 and syllable[-2:-1] in VOLATILE_DIPHTH:
        return False

    elif syllable[-1] in CONSONANTS:
        return True

    elif syl_len > 2 and syllable[-2:-1] in CONS_DIGRAPH:
        return True

    print("Error: [", syllable, "] coda not deterimined")
    return False




def toArr(num):
    new_num = str(num)
    num_arr = []
    for digit in new_num:
        num_arr.append(digit)
    return num_arr





#@title scan_line

# name:           scan_line
#
# inputs:         a line of poetry
#
# return:         true if syllable has a consonant coda, false othewise
#
# description:    runs all scansion calls and prints output
#
# note:           list of syllables and list of morae printer per line
#                 morae summing is commented out

def scan_line(line):
    list_of_syllables = parser(line)
    print(list_of_syllables)
    print("\n")
    list_of_morae = count_morae(list_of_syllables)
    print(list_of_morae)

    #give an option later
    # unknown, known = sum_morae(list_of_morae)
    # print("\n")
    # print("sum of known morae:      ", known)
    # print("number of unknown morae: ", unknown)
    




#@title scan_ifof

# name:           scan_ifof
#
# inputs:         a line of poetry, output file
#
# return:         true if syllable has a consonant coda, false othewise
#
# description:    runs all scansion calls and prints to outfile
#
# note:           list of syllables and list of morae printer per line
#                 morae summing is commented out

def scan_ifof(line, outFile):
    list_of_syllables = parser(line)
    outFile.write(' '.join(list_of_syllables))
    outFile.write("   ")
    list_of_morae = count_morae(list_of_syllables)
    outFile.write(' '.join(map(str, list_of_morae)))
    outFile.write("\n")
    
    # syllable_width = 12  # Adjust this value as needed
    # for syllables, morae in zip(list_of_syllables, (map(str, list_of_morae))):
    #     formatted_syllables = ''.join([syllable.ljust(syllable_width) for syllable in syllables])
    #     formatted_morae = ' '.join(morae)
    #     outFile.write(f"{formatted_syllables}{formatted_morae}\n")


    #give an option later
    # unknown, known = sum_morae(list_of_morae)
    # print("\n")
    # print("sum of known morae:      ", known)
    # print("number of unknown morae: ", unknown)


#@title main
# input_type = input("would you like to enter 1 line or a file?")
# print('\n')
 
num_args = len(sys.argv)




if num_args > 1:
    try:
        in_file  = sys.argv[1]
    
        poetry_file = open(in_file,  'r')

        if (num_args >= 2):
            out_file   = sys.argv[2]
            write_file = open(out_file, 'w')
        else:
             write_file = open("output.txt", 'wt')
        

        for line in poetry_file:
            scan_ifof(line, write_file)

        poetry_file.close()
        write_file.close()
    except IOError as err:
        print(err)

else:
    line = input("Enter one line: ")
    print('\n')
    scan_line(line)

