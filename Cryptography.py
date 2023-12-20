"""
Cryptograpy Functions
"""

# Decrypt a ROT13 encrypted text


def rot13(text):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        else:
            result.append(char)

    return ''.join(result)
