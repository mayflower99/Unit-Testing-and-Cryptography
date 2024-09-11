# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def validate_input(func):
    """
    The decorator that validates the inputs for both the encode and decode functions.
    :param func: the function to have inputs validated
    :return wrapper function:
    """
    def validate_string(string):
        """
        removes special characters and numbers from string
        :param string: the string to be validated
        :return new_string = a edited string without special characters and numbers
        """
        string = string.upper()
        new_string = ""
        for i in string:
            if ord(i) in range(65,91):
                new_string = new_string + i
        return new_string

    def wrapper(*args, **kwargs):
        """
        THe wrapper function
        :param args:
        :param kwargs:
        :return:
        """
        text = args[0]
        text = validate_string(text)
        codebet = args[1]
        return func(text, codebet)
    return wrapper
@validate_input
def sub_encode(text, codebet):
    """
    encodes the text using text and a encoded alphabet
    :param text: the text to be encoded
    :param codebet: the cipher alphabet
    :return: encoded text
    """
    return "".join([codebet[alpha.index(x)] for x in text])

@validate_input
def sub_decode(text, codebet):
    """
    decodes the text using text and a cipher alphabet
    :param text: the text to be decoded
    :param codebet: the cipher alphabet
    :return: decoded text
    """
    return "".join([alpha[codebet.index(x)] for x in text])


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(str(enc), cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
