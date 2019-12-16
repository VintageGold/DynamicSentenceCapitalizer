def user_input():
    user_text = input('Type in 3 sentences in lowercase, we will do the capitalization for you. ''\n')
    read_user_input(user_text)


# Capitalize letter when char is the first alphabetical letter of a sentence
def capitalize_letter(letter):
    capital = letter.capitalize()
    return capital


# Process User Input
def read_user_input(updated_user_input):
    character_list = []
    alpha_found = 0
    i = 0
    index_capitalize = 0

    # Read through all characters in userInput to
    # determine what will be capitalized and which will not.
    for char in updated_user_input:

        # Capitalize first letter of entry
        if index_capitalize == i:
            character_list.append(capitalize_letter(char))

        # Capitalize first found letter after punctuation
        elif char in ('.', '!', '?'):
            character_offset = i + 1  # adds one to i so the period found in the loop before,
                                      # does not appear in the search loop below
            for sub_char in updated_user_input[character_offset:]:
                # Tests whether character after period is an alphabetical character and
                # if so adds index to periodIndex
                alpha_found = sub_char.isalpha()
                if alpha_found:
                    index_capitalize = updated_user_input.find(sub_char, i)
                    break

            # Add letter to be capitalized to characterList
            character_list.append(char)

        else:
            # Add letter to characterList
            character_list.append(char)
        i += 1

    # Read through indexes of the letters to be capitalized
    output(character_list)


def output(updated_characterlist):
    updated_sentence = ''
    updated_sentence = updated_sentence.join(updated_characterlist)
    print(updated_sentence)


def main():
    user_input()


main()
