# Read the instructions to see what you need to do here!
from validate import validate_input
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def vig_encode(text, keyword):

  return [chr((ord(x) + ord(keyword[i % keyword.length()]) % 255)) for i,x in enumerate(text)]


def vig_decode(text, keyword):
  return [chr((ord(x) + ord(keyword[i % keyword.length()]) % 255)) if ((ord(x) - abs(n)) % 256) >= 0 else chr(256 + (ord(x) - abs(n)) % 256) for i,x in enumerate(text)]

 return "".join(chr((ord(x) - abs(n)) % 256) if ((ord(x) - abs(n)) % 256) >= 0 else chr(256 + (ord(x) - abs(n)) % 256) for x in str(text))
test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!