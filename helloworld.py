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

#new app
greeting = 'Hi there'
for i in range(100):
    greeting = greeting + '!'

print(greeting)

#new app
s = input("Enter a String of numbers")

num_list = (int(i) for i in (s.split(' ')))
print (sorted(num_list))
#x = x.sort(key=int)
#s = [int(a) for a in s]
#s = s.sort
#sorted(s, key=int)
s

#new app
a = [1,2,3,4,5,-6]
def keep_positive(a):
    b=[]
    for i in range(len(list(a))):
        if (a[i]>0):
            b.append(a[i])

    return b

b = keep_positive(a)
print (b)
#########################
user_input = input('Please enter a number')
print('Thank you! We’ve just withdrawn $' + user_input + ' from your credit card.')
user_input = input('Please enter a number')
user_input_converted = int(user_input)
print('Thank you! We’ve just withdrawn $' + user_input_converted + ' from your credit card.')
user_input = input('Please enter a number')
print('Thank you! We’ve just withdrawn $' + int(user_input) + ' from your credit card.')
user_input = input('Please enter a number')
print(f'Thank you! We’ve just withdrawn ${user_input} from your credit card.')
user_input = input('Please enter a number')
user_input_converted = int(user_input)
print(f'Thank you! We’ve just withdrawn ${user_input_converted} from your credit card.')


############################################

salary = int(input('Please enter your expected salary after graduation '))
num_languages = int(input('Please enter the number of programming languages you will learn '))
score = salary*num_languages
print(f'Your awesomeness score is {score}')

################################

while True:
    n = input('Please enter a number: ')
    try:
        n=int(n)
    except ValueError:
        print('You have entered something that cannot be converted into a number')
    if n<= 0:
        print('You have entered a number, but not a positive')
        continue
    else:
        break
####################################

while True:
    number = input('Enter a positive number please: ')
    if(int(number)>0):
        break
    else:
        print('No way, you should enter a positive number!')

########################

with open(r'test1.txt','a',encoding = 'utf-8') as output_file:
    for i in range(10):
        output_file.write(f"{i}")
    output_file.write("\n")
output_file.close()


####################################### reading from a file and inputting only names into a new file
with open(r'test1.txt','w',encoding='utf-8') as output_file:
    with open(r'students.csv', 'r', encoding='utf-8') as input_file:
        for i in input_file:
            i = i.split(';')
            i = i.pop(1)
            output_file.write(f"{i}")
#######################################
with open(r'test1.txt','w',encoding='utf-8') as output_file:
    with open(r'students.csv', 'r', encoding='utf-8') as input_file:
        for i in input_file:
            i = i.split(';')
            i = i.pop(0)
            i = i.split(' ')
            i = i.pop(1)
            output_file.write(f"{i}\n")
########################################
with open(r'emails.csv','r', encoding='utf-8') as input_file:
   with open(r'greeting.csv','w', encoding='utf-8') as output_file:
       for x in input_file:
           stripped_line = x.strip()
           str_list = stripped_line.split(';')
           name = str_list[0]
           email = str_list[1]
           output_file.write('Hi, 'f'{name}! We\'ve sent an email to {email} \n')
############################################
calories_file = open('calories_burn.txt', 'r')
activities = []
final_list = []
for i in calories_file:
    activities.append(i.split(' '))
for x in range(len(activities)):
    if (int(activities[x].pop(1))>=500):
        final_list.append(str(activities[x].pop(0)))
final_list = sorted(final_list)
for x in range(len(final_list)):
    print(final_list[x], end="\n")
##############################################
calories_file = open('calories_burn.txt', 'r')
sum=0
for i in calories_file:
    sum += int(i.split(' ').pop(1))
print(str(sum))
############################################
calories_file = open('calories_burn.txt','r')
i = calories_file.readline()
count,sum, space = 0,0, True
for x in range(len(i)):
    if(i[x]==';'):
        count = count+1
        space=False
if(space==False):
    calories_file.seek(0)
    for i in calories_file:
        i = int(i.split(';').pop(count))
        sum += i
elif(space==True):
    calories_file.seek(0)
    for i in calories_file:
        i = int(i.split(' ').pop(len(i.split(' '))-1))
        sum += i
print(sum)
######################################################
t = [1,2,3,4,5,6,21,32,9,10,11,12]
p=[]
for i,n in enumerate(t):
    print (i,n)
    if(i!=0 and i!=1 and i!=len(t)-1 and i!=len(t)-2):
        p.append(n)
