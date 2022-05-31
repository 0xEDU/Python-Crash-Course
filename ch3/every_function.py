# Exercise 3.10
musicians = ['vivaldi', 'beethoven','brahms','mozart']

musicians.append('dvorak')
print(musicians)

musicians.insert(2, 'dvorak')
print(musicians)

del musicians[2]
print(musicians)

musicians.append('bach')
popped_musician = musicians.pop()
print(musicians, popped_musician)
musicians.append(popped_musician)
musicians.append('vivaldi')
print(musicians)

musicians.remove('vivaldi')
print(sorted(musicians))
print(musicians)

musicians.sort()
print(musicians)

musicians.reverse()
print(musicians)

print(len(musicians))