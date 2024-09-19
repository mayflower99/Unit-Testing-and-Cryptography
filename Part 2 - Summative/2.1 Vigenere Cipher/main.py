# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vig_encode(text: str, keyword: str) -> str:
    """

    :param text: is the text you wish to encode
    :param keyword: is the keyword to use as a key
    :return:
    """

    return "".join([chr(ord(x) + ord(keyword[i % len(keyword)]) % 256) for i, x in enumerate(text)])


def vig_decode(text: str, keyword: str) -> str:
    return "".join([chr(ord(x) - ord(keyword[i % len(keyword)]) % 256) if ord(x) - ord(keyword[i % len(keyword)]) % 256
                    >= 0 else chr(256 + (ord(x) - ord(keyword[i % len(keyword)]) % 256)) for i, x in enumerate(text)])


test = "THEQUICKBROWNFOXJUMPEDOVERTHE *&@*($Q()@*$()#(@*)LAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
