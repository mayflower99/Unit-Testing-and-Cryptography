import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    """

    :param a: no clue
    :param b: also no clue
    :return: the inverse mod something
    """
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    """

    :param a: the thing you are moding
    :param m: the mod value
    :return: the inverse mod
    """
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """

    :param text: The text to encode
    :param a: the number to multiply by
    :param b: the number to shift by
    :return: the encrypted text
    """
    new_string = ""
    for letter in text:
        cypher_number = (alpha.index(letter) * a)
        cypher_number = (cypher_number + b) % 26
        new_string += alpha[cypher_number]
    return new_string

def affine_decode(text, a, b):
    """

    :param text: The text to decode
    :param a: the number that was multiplyed by
    :param b: the number that was shifted by
    :return: the decoded text
    """
    new_string = ""
    for letter in text:
        cypher_number = (alpha.index(letter) - b)
        cypher_number = (cypher_number * mod_inverse(a,26)) % 26
        new_string += alpha[cypher_number]
    return new_string

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """

    :param ngram: the text to be converted to a number
    :return: the number
    """
    new_number = 0
    for i, letter in enumerate(ngram):
        new_number += alpha.index(letter) * (26 ** i)
    return new_number
def convert_to_text(num, n):
    """

    :param num: the number to converted back to text
    :param n: the length of the string
    :return: the decrypted text
    """
    new_text = ""
    for i in range(n):
        num_temp = num
        num =  num // 26
        new_text += alpha[num_temp % 26]
    return new_text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!

def affine_encode_num(num:int, a:int, b:int, n) -> int:
    """
    :param num: the number to be affine cyphered
    :param a: the number to multiply by
    :param b: the number to shift by
    :param n: the length of the string
    :return: the encrypted text
    """
    cypher_number = num * a
    cypher_number = (cypher_number + b) % 26**n
    return cypher_number

def affine_decode_num(num:int, a:int, b:int,n)-> str:
    """

    :param num: the number to be decrypted
    :param a: the number that was multiplied
    :param b: the number that was shifted by
    :param n: the length of the string
    :return: the decrypted text
    """
    cypher_number = num - b
    cypher_number = (cypher_number * mod_inverse(a,26**n)) % 26**n
    return cypher_number
# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    """

    :param text: the text to be encrypted
    :param n: the length of the engrams
    :param a: the number to multiply by
    :param b: the number to shift by
    :return: the encoded text
    """
    while(len(text) % n != 0):
        text = text + "X"
    new_string = ""
    for i in range(int(len(text) / n)):
        x = text[(i*n):((i+1)*n)]
        x = convert_to_num(x)
        number = affine_encode_num(x, a, b,n)
        new_string += convert_to_text(number, n)
    return new_string


def affine_n_decode(text, n, a, b):
    """

    :param text: the text to be decrypted
    :param n: the length of the engrams
    :param a: the number that was multiplied by
    :param b: the number that was shifted by
    :return: the decrypted text
    """
    new_string = ""
    for i in range(int(len(text) / n)):
        x = text[(i * n):((i + 1) * n)]
        x = convert_to_num(x)
        number = affine_decode_num(x, a, b, n)
        new_string += convert_to_text(number, n)

    return new_string

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!