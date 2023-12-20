"""
Cryptograpy Functions
"""
import base64

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

# Decode a string from binary, hex, or base64
def decode(cipher, choice):
    if choice == 'bin':
        cipher = cipher.split()
        return ''.join([chr(int(cipher[i],base=2)) for i in range(0, len(cipher))])
    elif choice == 'hex':
        return ''.join([chr(int(cipher[i] + cipher[i+1],base=16)) for i in range(0,len(cipher),2)])
    elif choice == 'b64':
        return base64.b64decode(cipher)
    else:
        return "Invalid choice"
