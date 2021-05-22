import string
import argparse

program = argparse.ArgumentParser(description="Vigenere Cipher Encryption")

program.add_argument("-m", "--message", type = str, help = "Enter the text that you want to encrypt")
program.add_argument("-k", "--key", type = str, help = "Enter the key")

args = program.parse_args()

result = ""
index = 0

for i in args.message:
    if i in string.ascii_lowercase:
        offset = ord(args.key[index]) - ord('a')

        encrypted = chr((ord(i) - ord('a') + offset) % 26 + ord('a'))
        result = result + encrypted

        index = (index + 1) % len(args.key)

    elif i in string.ascii_uppercase:
        offset = ord(args.key[index]) - ord('A')

        encrypted = chr((ord(i) - ord('A') + offset) % 26 + ord('A'))
        result = result + encrypted

        index = (index + 1) % len(args.key)

    else:
        result = result + i

print("message: " + args.message)
print("result:" + result)
