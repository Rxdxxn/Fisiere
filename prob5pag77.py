vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
tot = []
with open('text.txt','w') as f:
    f.write('')

f=open('text.txt')
for i in f.read():
    if i in vocale:
        tot.append(i)

print('Vocale din fisier sunt:',tot)
print('Numarul de vocale este:',len(tot))