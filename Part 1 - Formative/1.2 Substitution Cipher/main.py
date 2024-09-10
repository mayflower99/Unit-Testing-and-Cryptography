# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def validate_input(func):
    def validate_string(string):
        string = string.upper()
        new_string = ""
        for i in string:
            if ord(i) in range(65,91):
                new_string = new_string + i
        return new_string

    def wrapper(*args, **kwargs):
        text = args[0]
        text = validate_string(text)
        codebet = args[1]
        return func(text, codebet)
    return wrapper
@validate_input
def sub_encode(text, codebet):
    return "".join([codebet[alpha.index(x)] for x in text])

@validate_input
def sub_decode(text, codebet):
    return "".join([alpha[codebet.index(x)] for x in text])


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(str(enc), cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
