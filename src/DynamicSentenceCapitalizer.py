def userInput():
    userInput = input('Type in 3 sentences in lowercase, we will do the capitalization for you. ''\n')
    readUserInput(userInput)

#Capitalizes letter when char is the first alphabetical letter of a sentence
def capitalizeLetter(letter):
    capital = letter.capitalize()
    return capital

#Process User Input
def readUserInput(updatedUserInput):
    characterList = []
    alphabet = False
    alphaFound = 0
    i = 0
    indexCapitalize = 0

    #Reads through all characters in userInput to
    #determine what will be capitalized and which will not.
    for char in updatedUserInput:

        #Capitalize first letter of entry
        if indexCapitalize == i:
            characterList.append(capitalizeLetter(char))

        #Capitalizes first found letter after every period
        elif char == '.' or char == '!'or char == '?':
            characterOffset = i + 1 #adds one to i so the period found in the loop before,
                                    #does not appear in the search loop below
            for subChar in updatedUserInput[characterOffset:]:
                #Tests whether character after period is an alphabetical character and
                #if so adds index to periodIndex
                alphaFound = subChar.isalpha()
                if alphaFound == True:
                    indexCapitalize = updatedUserInput.find(subChar,i)
                    break

            #Adds letter to be capitalized to characterList
            characterList.append(char)

        else:
            #Adds letter to characterList
            characterList.append(char)
        i += 1

    #Reads through indexes of the letters to be capitalized
    output(characterList)

def output(updatedCharacterList):
    updatedSentence =''
    updatedSentence = updatedSentence.join(updatedCharacterList)
    print(updatedSentence)

def main():
    userInput()
    exit()

main()
