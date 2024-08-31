import sys
import re
import braille_map as bmap
import english_map as emap

def toBraille(words):
    result = ""
    numWords = len(words)
    counter = 0
    numflag = 0
    for i in words:
        if counter == 0: #does not print space before a work or if there is only one word
            pass
        elif counter == numWords: #does not print space after the last word 
            pass
        else: #only prints space between two words
            result+= emap.Eng_to_braille[" "]
        for j in i:
            if j.isupper():
                result += emap.Eng_to_braille["capital"]
                result += emap.Eng_to_braille[j.lower()]
                continue
            elif j.isnumeric():
                if(numflag == 0):
                    result += emap.Eng_to_braille["number"]
            
            result += emap.Eng_to_braille[j]
            numflag = 1 
        counter += 1
        numflag = 0 #next space symbol encountered
    return result

def toEnglish(word):
    braille = re.findall('......', word[0])
    result = ""
    capitalFlag = 0
    numFlag = 0
    for i in braille:
        temp = bmap.Braille_to_eng[i]
        print(temp)
        if temp == "capital":
            capitalFlag = 1
        elif capitalFlag == 1:
            letter = bmap.Braille_to_eng[i][0]
            result += letter.upper()
            capitalFlag = 0
        elif temp == "number":
            numFlag = 1
        elif temp == " ":
            numFlag = 0
            result += bmap.Braille_to_eng[i]
        elif numFlag == 1:
            letter = bmap.Braille_to_eng[i][1]
            result += letter
        
        else:
            result += bmap.Braille_to_eng[i][0]
    return result        

arguments = []  #list to keep all the command line arguments+
for arg in sys.argv[1:]:
    arguments.append(arg)

lenght_arg = len(arguments)

if lenght_arg > 1: #if there is more than one argument, the input has to be english
    print(toBraille(arguments))

elif re.findall("[^.O]", arguments[0]): #if only one argument, checks if the string has anything other that "O" or ".", i.e., its in english
    print(toBraille(arguments))

else: #determines its in braille and converts to english
    print(toEnglish(arguments))
