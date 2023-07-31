morse_code_table = {
 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
 '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..', '9': '----.',
 ' ': '/'
}


def invert_dictionary(morse_code_dict):
    inverted_dict = {value: key for key, value in morse_code_dict.items()}
    return inverted_dict


def text_to_morse_gen(input_string):
    for letter in input_string.upper():
        if letter in morse_code_table:
            input_letter = letter
            yield morse_code_table[input_letter]


def morse_to_text_gen(morse_text):
    inverted_dict = invert_dictionary(morse_code_table)
    letters = morse_text.split(' ')
    for character in letters:
        try:
            inverted_character = inverted_dict[character]
        except KeyError:
            print('')
        yield inverted_character


def return_translation_into_morse(my_message):
    my_translation = ''
    for code in text_to_morse_gen(my_message):
        my_translation = my_translation + code + ' '
    return my_translation.strip()


def return_translation_into_text(my_message):
    my_plaintext = ''
    for letter in morse_to_text_gen(my_message):
        my_plaintext = my_plaintext + letter
    return my_plaintext.strip()


# main
if __name__ == '__main__':
    my_selection_string = input('Bitte wählen Sie zwischen Morse-Code- (M) und Fließtext-Eingabe (F): ').lower()
    my_input_message = input('Bitte geben Sie eine Nachricht ein: ')
    print('User selection: ' + my_selection_string)
    print('User message: ' + my_input_message)
    if my_selection_string == 'm':
        print(return_translation_into_text(my_input_message))
    else:
        print(return_translation_into_morse(my_input_message))
