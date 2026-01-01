import random
import string

def obfuscate(payload: str) -> str:
    result = ""
    for char in payload:
        result += char
        if random.random() > 0.7:
            result += random.choice(string.ascii_letters)
    return result
