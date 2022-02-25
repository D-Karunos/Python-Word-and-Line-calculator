import string

while True:
    # File input
    print("To quit type 'exit'")
    filename = input("Add file location:")
    print()

    #Adding an option to close application with code
    if filename == 'exit':
        break

    # The translator function is used to remove all punctuation from the file, so character length won't be compromised
    translator = str.maketrans('', '', string.punctuation)

    # setting up variables for counting the number of words, characters and lines in the file
    wordsCount = 0
    linesCount = 0
    charCount = 0
    try:
        with open(filename, 'r') as file:

            # Using for loop to scan every line in code
            for line in file:
                linesCount += 1

                line = line.translate(translator)
                wordsList = line.split()

                wordsCount += len(wordsList)

                # removing \n line from line, because it would be counted as a character
                line = line.rstrip("\n")

                # counting amount of characters in line without spaces
                charCount += len(line.replace(" ", ""))

        # formatting output to present Word length, line length and Mean word length with 2 decimal digits. %i/%f is position of variable (integer/float)
        print("Your file is containing: \n%i Words \n%i Lines \n%0.2f  Mean word length" % (
        wordsCount, linesCount, charCount / wordsCount))
        print()

        input("press enter to continue")

# In case file name is provided wrong it will be keeping application open and will allow you to try again
    except FileNotFoundError:
        print("Wrong file or file path, try again!")
        print()
