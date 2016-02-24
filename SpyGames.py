import base64
import random

__author__ = 'Gilad Barak'
__name__ = 'main'


def encrypt1(message, key):
    """
    Takes every char in message and the first number given in key.
    Adds number to every char's unicode value and returns created message.
    """
    return "".join([chr(ord(x) + int(key[0])) for x in message])


def decrypt1(message, key):
    """
    Takes every char in message and the first number given in key.
    Decreases number from every char's unicode value and returns created message.
    """
    return "".join([chr(ord(x) - int(key[0])) for x in message])


def encode2(message, key):
    """
    encode function given in exercise
    Along with message:
    YVxcGVRATVhWXxlOXFhVGUZAWEtBFFZXFWBMXEZQWEAVWVZLW11XXg==
    """
    return base64.encodestring("".join([chr(ord(message[i]) ^ ord(key[i % len(key)])) for i in xrange(len(message))]))


def decrypt2(message, key):
    """
    Decodes message that were encoded with encode2 function.
    Decodes given message with key 5499
    """
    decoded = base64.decodestring(message)
    return "".join([chr(ord(decoded[i]) ^ ord(key[i % len(key)])) for i in xrange(len(decoded))])


def encrypt3(message, key):
    """
    Encode function given in exercise
    Along with message:
    euTtSa:0 kty1h a0  nlradstara  atlot 5wtic
    """
    random.seed(key)
    l = range(len(message))
    random.shuffle(l)
    return "".join([message[x] for x in l])


def decrypt3(message, key):
    """
    Decodes message that was encoded with function 'encode3'
    with 'aBp' as key
    """
    random.seed(key)
    message = list(message)
    order = range(len(message))
    random.shuffle(order)
    decrypt_message = ['']*len(message)
    for index,originalIndex in enumerate(order):
        decrypt_message[originalIndex] = message[index]
    return "".join(decrypt_message)


def main():
    print decrypt3(raw_input("Enter message."), raw_input("Enter key."))


if __name__ == 'main':
    main()
