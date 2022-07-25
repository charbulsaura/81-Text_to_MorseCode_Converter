# Assignment: Text to Morse Code Converter
# A text-based Python program to convert Strings into Morse Code.
"""
You will use what you've learnt to create a text-based (command line) program
that takes any String input and converts it into Morse Code

You've created plenty of text-based programs in Days 1 -10,
so look back at some of those projects if you don't remember what a text-base program looks like

Wikipedia Entry for Morse Code
The design, functionality, code style is all up to you
You're wearing the big-girl/big-boy pants now
So you get to decide
"""
"""
Questions for this assignment
Reflection Time:
This is a place to journal your experience of completing this project
This will help you figure out how to improve as a developer
Write down how you approached the project
What was hard, what was easy
How might you improve for the next project?
What was your biggest learning from today?
What would you do differently if you were to tackle this project again?
"""

# Approach/Steps to take
"""
-Store a database of all the morse code alphabets --> key value pairs for comparison
-Read user text input
-Convert input string to individual characters --> then convert to morse code & output/switch back to morse code string
- Assign 's' as space
- Add 3 's' after every character except last character 
(last character and space; total add to 10 's'; check for 10 's' in morse string, then replace 10 's' with 7 's'
problem is " " also has 3 's' added to the end; also have to remove)
- Add 7 's' after every word

Morse Code rules: 
Length of dot = 1 unit
Dash = 3 units
Space bet parts of same letter = 1 unit
Space bet letters = 3 units
Space bet words = 7 units

References used:
https://www.w3schools.com/python/python_dictionaries.asp
https://stackoverflow.com/questions/37377389/convert-list-into-string-in-python3
https://www.w3schools.com/python/ref_string_replace.asp
https://www.w3schools.com/python/python_try_except.asp
"""
morse_code_characters = {"A": "0 ---",
                         "B": "--- 0 0 0",
                         "C": "--- 0 --- 0",
                         "D": "--- 0 0",
                         "E": "0",
                         "F": "0 0 --- 0",
                         "G": "--- --- 0",
                         "H": "0 0 0 0",
                         "I": "0 0",
                         "J": "0 --- --- ---",
                         "K": "--- 0 ---",
                         "L": "0 --- 0 0",
                         "M": "--- ---",
                         "N": "--- 0",
                         "O": "--- --- ---",
                         "P": "0 --- --- 0",
                         "Q": "--- --- 0 ---",
                         "R": "0 --- 0",
                         "S": "0 0 0",
                         "T": "---",
                         "U": "0 0 ---",
                         "V": "0 0 0 ---",
                         "W": "0 --- ---",
                         "X": "---",
                         "Y": "--- 0 --- ---",
                         "Z": "--- --- 0 0",
                         "1": "0 --- --- --- ---",
                         "2": "0 0 --- --- ---",
                         "3": "0 0 0 --- ---",
                         "4": "0 0 0 0 ---",
                         "5": "0 0 0 0 0",
                         "6": "--- 0 0 0 0",
                         "7": "--- --- 0 0 0",
                         "8": "--- --- --- 0 0",
                         "9": "--- --- --- --- 0",
                         "0": "--- --- --- --- ---",
                         " ": "sssssss"
                         }

while True:
    try:
        # print("LOOP START")
        text = input("Please enter text to convert to morse code:")
        print(text)

        morse_input = []
        for character in text:
            morse_input.append(character.upper())
        print(morse_input)

        morse_output = []
        for i in range(len(morse_input)):
            morse_character = morse_code_characters[morse_input[i]]
            # print(i)
            # print(morse_character)
            if i == len(morse_input)-1:
                morse_output.append(f"{morse_character}")
            elif morse_character != "sssssss":
                morse_output.append(f"{morse_character}sss")
            elif morse_character == "sssssss":
                morse_output.append(f"{morse_character}")
        print(morse_output)

    #Invalid input, ask for user input again
    #How to check for error and repeat above morse conversion without having to repeat code again?
    # -- exit loop and rerun from top
    except KeyError:
        print("Please input a valid text string!")
        # print("LOOP END")
        continue

    # If no key error; proceed to parse morse string
    else:
        # print("ENTERED ELSE")

        morse_string = ''.join(str(character) for character in morse_output)
        print(morse_string)
        morse_string_remove_duplicate_s = morse_string.replace("ssssssssss", "sssssss")
        print(morse_string_remove_duplicate_s)
