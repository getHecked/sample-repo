[f'Printout for person #{x}' for x in range(10)]

participants = ['Alex', 'Bob', 'Claudia', 'Bob', 'Daniel', 'Alex', 'Alex']

s = sorted(list(set(participants)))
s

for i in range(len(s)):
    print(f"{s[i]}", end=', ')
    if (i==len(s)-1):
        print(f'and {s[i]}', end='.')

#enumerate(<list>) --> returns a pair of data (index,value)

#new app
email = {
    'Leo': 'leo@gmail.com',
    'Catalina': 'catalin@gmail.com',
    'Ben': 'benedikt.corkill@is-ostrava.cz'
}

#prints the pair
for name in email.items():
    print(name)

#prints values
for name in email.values():
    print(name)

#prints keys
for name in email.keys():
    print(name)
