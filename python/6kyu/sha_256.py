# Link: https://www.codewars.com/kata/587fb57e12fc6eadf200009b
# Description:
#
# Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.
# sha256("Hello World!") => "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"

from hashlib import sha256


def to_sha256(s):
    s = sha256(s.encode('utf-8'))
    return s.hexdigest()


print(to_sha256('victor'))
