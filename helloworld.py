weekdays = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
leave=input('Leaving day: ')
d=int(input('Days gone: '))
l = weekdays.index(leave)
# l is the numeric version of which day
# d is the number of days until return
num = d%7
r = l+num
if (r>7):
    r = r-7

print("If you leave on",leave,"and return",d,"days later, you will return on",weekdays[r],".")

#key value system
email = {
    'Leo': 'leo@gmail.com',
    'Catalina': 'catalin@gmail.com',
    'Ben': 'benedikt.corkill@is-ostrava.cz'
}


print (f"Hi Ben! I've sent you an email at {email['Ben']}")


#new app
x = ['Leo','Catalina','Tessa','Kolya','Alex','Animesh','Jeremy']
print("Attendence: ", end=' ')
for i in range(len(x)):
    if i==len(x) - 1:
        print("and", x[i])
    else:
        print(x[i], end=', ')
    if (i%2==0):
        print("emm", end=' ')

#new app

x=[1984,1994,1812,2000]
y = [ ('old' if x[number]<1985 else 'young') for number in range(len(x))]
y

#new app
x = ['Leo','Catalina','Tessa','Kolya','Alex','Animesh','Jeremy']
greetings = [(f'Hi {x[number]}!') for number in range(len(x))]
print(greetings)
