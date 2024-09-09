# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def int_array_from_char(string):
    return [ord(x) for x in string]
def caesar_encode(text, n):
    """

    :param text:
    :param n:
    :return: encoded text
    """
    return "".join([chr((ord(x) + abs(n))%256) for x in str(text)])


def caesar_decode(text, n):
    """
    :param text:
    :param n:
    :return: decoded text
    """
    return "".join(chr((ord(x) - abs(n)) % 256) if ((ord(x) - abs(n)) % 256) >= 0 else chr(256 + (ord(x) - abs(n)) % 256) for x in str(text))
print (ord("\\"))




# def caesar_encode(text, n):
#     """
#
#     :param text:
#     :param n:
#     :return: encoded text
#     """
#     return "".join([alpha[(alpha.index(x)+5)%26] for x in text])
#
#
# def caesar_decode(text, n):
#     """
#     :param text:
#     :param n:
#     :return: decoded text
#     """
#     return "".join([alpha[(alpha.index(x)-5)%26] for x in text])



test = "HELLOWORLD"
shift = 5
enc = caesar_encode("\\!@#$%^&*()_+-={}[]:;<>,.?/|\"'~`", 50)
print(int_array_from_char(enc))
dec = caesar_decode(enc, 50)
print(enc)
print(dec)
# If this worked, dec should be the same as test!

