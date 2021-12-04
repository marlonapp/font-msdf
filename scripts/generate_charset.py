a = 0
z = 255

s = ''

for i in range(a, z):
    if chr(i) == ' ':
        print('Empty')
    else:
        s += chr(i)

with open('charset.txt', 'w', encoding='utf-8') as file:
    file.write(s)
