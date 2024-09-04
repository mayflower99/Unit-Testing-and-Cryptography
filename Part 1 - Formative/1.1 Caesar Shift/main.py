# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print()
def caesar_encode(text, n):
    return "".join([alpha[(alpha.index(x)+5)%26] for x in text])


def caesar_decode(text, n):
    return "".join([alpha[(alpha.index(x)-5)%26] for x in text])



test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
