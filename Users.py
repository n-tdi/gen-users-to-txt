import string
import random
import sys

text_file = open("Users.txt", "w")
for x in range(0, 10):
    # printing lowercase
    letters = string.ascii_lowercase
    n = text_file.write( ''.join(random.choice(letters) for i in range(4)) )
    n = text_file.write('\n')
text_file.close()