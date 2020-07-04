alph_string = [chr(i) for i in range(ord('a'), ord('z')+1)]
alph_string.extend([chr(i) for i in range(ord('A'), ord('Z')+1)])
alph_string.extend([chr(i) for i in range(ord('0'), ord('9')+1)])
string = "".join(alph_string)
print(string)
print(string[0])
print(string[-1])
print(string[2] + string[-3])
print(string[:8])

for t in range(len(string)) :
    if t % 3 == 0 :
        print(string[t], end='')
print()

for t in range(0,len(string),3) : # more faster then previous
    print(string[t], end='')
print()