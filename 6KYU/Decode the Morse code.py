"""
Morse code decoder, ToDo: Accept dots, dashes and spaces, return human-readable message

"""

def decodeMorse(morse_code):
    morse_code = morse_code.strip().split("   ")  

    decoded_result = []

    for ch in morse_code:
        character = ch.split(" ")
        for j in character:
            decoded_result.append(MORSE_CODE[j])
        decoded_result.append(" ")

    resultword = ''.join(decoded_result).strip()

    return resultword
