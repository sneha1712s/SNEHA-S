p="mango\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\ s city - use double slashes inside double qts"
print(p)

p="mango\\\\\\\\ s city - use double slashes inside double qts"
print(p)




ui=input('enter the string')
print([w for w in ui.split() if 's' in w])

