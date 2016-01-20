import base64

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
    return base64.encodestring("".join([chr(ord(message[i]) ^ ord(key[i % len(key)])) for i in xrange(len(message))]))


def main():
    print decrypt1(raw_input("Enter message."), raw_input("Enter key."))

if __name__ == 'main':
    main()
