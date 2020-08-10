'''
https: //www.codewars.com/kata/530e15517bc88ac656000716/python

5 kyu Rot13

ROT13 is a simple letter substitution cipher that replaces a letter with the
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar
cipher.

Create a function that takes a string and returns the string ciphered with
Rot13. If there are numbers or special characters included in the string,  they
should be returned as they are. Only letters from the latin/english alphabet
should be shifted,  like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''


def rot13(message):
    dic = {'a': 'n', 'A': 'N', 'b': 'o', 'B': 'O', 'c': 'p', 'C': 'P',
           'd': 'q', 'D': 'Q', 'e': 'r', 'E': 'R', 'f': 's', 'F': 'S',
           'g': 't', 'G': 'T', 'h': 'u', 'H': 'U', 'i': 'v', 'I': 'V',
           'j': 'w', 'J': 'W', 'k': 'x', 'K': 'X', 'l': 'y', 'L': 'Y',
           'm': 'z', 'M': 'Z', 'n': 'a', 'N': 'A', 'o': 'b', 'O': 'B',
           'p': 'c', 'P': 'C', 'q': 'd', 'Q': 'D', 'r': 'e', 'R': 'E',
           's': 'f', 'S': 'F', 't': 'g', 'T': 'G', 'u': 'h', 'U': 'H',
           'v': 'i', 'V': 'I', 'w': 'j', 'W': 'J', 'x': 'k', 'X': 'K',
           'y': 'l', 'Y': 'L', 'z': 'm', 'Z': 'M'}
    return ''.join([dic[d] if d in dic else d for d in message])


print(rot13("test"))  # "grfg")
print(rot13("Test"))  # "Grfg")
print(rot13("Test Test"))  # "Grfg Grfg")
