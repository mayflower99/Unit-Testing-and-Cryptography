import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    new_string = ""
    for letter in text:
        cypher_number = (alpha.index(letter) * a) % 26
        cypher_number = (cypher_number + b) % 26
        new_string += alpha[cypher_number]
    return new_string

def affine_decode(text, a, b):
    new_string = ""
    for letter in text:
        cypher_number = (alpha.index(letter) - b) % 26
        cypher_number = (cypher_number * 9) % 26
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
    new_number = 0
    for i, letter in enumerate(ngram):
        new_number += alpha.index(letter) * (26 ** i)
    return new_number
def convert_to_text(num, n):
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

def affine_encode_num(num:int, a:int, b:int) -> int:
    cypher_number = (num * a) % 26
    cypher_number = (cypher_number + b) % 26
    return cypher_number

def affine_decode_num(num:int, a:int, b:int)-> str:
    cypher_number = (num - b) % 26
    cypher_number = (cypher_number * mod_inverse(a,26)) % 26
    return cypher_number
# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    while(len(text) % n != 0):
        text = text + "X"
    new_string = ""
    for i in range(int(len(text) / n)):

        x = text[(i*n):((i+1)*n)]
        x = convert_to_num(x)
        number = affine_encode_num(x, a, b)
        number = number % 26 ** n
        new_string += convert_to_text(number, n)


def affine_n_decode(text, n, a, b):
    new_string = ""
    for i in range(int(len(text) / n)):
        x = convert_to_num(text[(i * n):((i + 1) * n)])
        number = affine_decode_num(x, a, b)
        new_string += convert_to_text(number, n)

    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!