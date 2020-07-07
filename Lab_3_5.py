alph_string = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alph_string.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
alph_string.extend([chr(i) for i in range(ord('0'), ord('9') + 1)])

print("".join(alph_string))
print(alph_string[0])
print(alph_string[-1])
print(alph_string[0] + alph_string[-1])
print(alph_string[:10])

print(alph_string[::2])

for i in alph_string:
    if i.isdigit():
        print(i, end='')
print()
print(alph_string[-1::-1])
string = "".join(alph_string)
print(string)
