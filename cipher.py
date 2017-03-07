def encode_cipher(data, shift):
    encoded_data = ''
    for c in data:
        ascii_code = ord(c)
        if ascii_code >= 65 and ascii_code <= 90:
            ascii_code += shift
            ascii_code %= 91
            ascii_code += (ascii_code < 65)*65
        elif ascii_code >= 97 and ascii_code <= 122:
            ascii_code += shift
            ascii_code %= 123
            ascii_code += (ascii_code < 97)*97
        encoded_data += chr(ascii_code)
    return encoded_data

phrase = raw_input("Enter sentence to encrypt: ")
shift = raw_input("Enter shift value: ")
print "The encoded phrase is: " + encode_cipher(phrase, int(shift))
