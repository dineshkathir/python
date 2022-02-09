letters = "abcdefghijklmnopqrstuvwxyz1234567890?!.,;:+-= "
morseCode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','..--..','-.-.--','.-.-.-','--..--','-.-.-.','---...','.-.-.','-....-','-...-','/']

def wordToMorse(word):
    word = word.lower()
    changed = []
    for letter in word:
        changed.append(morseCode[letters.find(letter)])
    return " ".join(changed)

def morseToWord(morseInput):
    morseInput = morseInput.lower()
    morseInput = morseInput.split()
    changed = []
    for mor in morseInput:
        changed.append(letters[morseCode.index(mor)])
    return ''.join(changed)