import string

message = input("Enter the text: ")
key = input("Enter the key: ")

result = ""
index = 0

for i in message:
    if i in string.ascii_lowercase:
        offset = ord(key[index]) - ord('a')

        encrypted = chr((ord(i) - ord('a') + offset)%26 + ord('a'))
        result = result + encrypted

        index = (index + 1) % len(key)

    elif i in string.ascii_uppercase:
        offset = ord(key[index]) - ord('A')

        encrypted = chr((ord(i) - ord('A') + offset) % 26 + ord('A'))
        result = result + encrypted

        index = (index + 1) % len(key)

    else:
        result = result + i

print("message: " + message)
print("result:" + result)
