"""
Cryptograpy Functions
"""
import base64
import binascii


# Decrypt a ROT13 encrypted text
def rot13(text):
    result = []

    for char in text:
        if "a" <= char <= "z":
            offset = ord("a")
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        elif "A" <= char <= "Z":
            offset = ord("A")
            result.append(chr(((ord(char) - offset + 13) % 26) + offset))
        else:
            result.append(char)

    return "".join(result)


# Decode a string from binary
def binary_decode(text):
    text = text.split()
    print("".join([chr(int(text[i], base=2)) for i in range(0, len(text))]))

# Decode a string from hex
def hex_decode(text):
    print(''.join([chr(int(text[i] + text[i+1],base=16)) for i in range(0,len(text),2)]))

# Decode a string from base64
def base64_decode(text):
    b = base64.b64decode(text)
    binascii.b2a_base64(b)
    print(b.decode("utf-8"))
    
