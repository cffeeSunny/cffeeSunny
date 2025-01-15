def is_lecturer(name):
    return name == 'Ben'

print(is_lecturer('Ben'))

def welcome_with_time (name, time_of_day):
    if time_of_day == 'am':
        print(f'Good morning {name}!')
    elif time_of_day == 'pm':
        print(f'Good afternoon {name}!')
    elif time_of_day == 'noon':
        print(f'Good night {name}!')
    else :
        print(f'Hello ')


result = 1
i = 5
while i > 0:
    result *= i
    i -= 1

print(result
      )

for i in range(5):
    print (i)
    0
    1
    2
    3
    4

for i in range(1,5):
    print (i)
    1
    2
    3
    4

for i in range(1,5,2):
    print (i)
    1
    3

result =1
for i in range(2,6):
    result *= i
    print(result)

for i in range (2,6,-1):
    print(i)

for i in range(6,2,-1):
    6
    5
    4
    3
my_str = 'Hellllllllllo'
for c in my_str:
    print (c)

for c in my_str:
    print(c)
    if c == 'l':
        print('Found an l')
        break

for c in my_str:
    if c == 'l':
        continue
    print(c)



letters = ['abc', 'bcd', 'cde']
print(letters[0])

letters [0]

letters [-1]

#letters [-4] or [3 ]is impossible because there is no such in this list letters


alphabet = list('abcdef')
print(alphabet)

alphabet.append('z')
print(alphabet)

#letter. shows all
# dir(letter)
print(dir(letters))

my_list = list('Hello world')
my_list[0]= 'h'


print('<sep>'.join(my_list))

''.join(my_list) #makes a string out of list
print(''.join(my_list))

'foo' in 'foofighters' #true

1 in 123 # false

'1' in '123' #true

'h' in 'foo' # false

1 in '123' #false


def duv_by_two_numbers (n,m):
    for i in range (1,100):
        if i % n == 0 and i % m == 0:
            print(f'{i} is divisible by {n} and {m}')
print(duv_by_two_numbers(3,9))


def ascii_to_string(some_list):
    return print(''.join(chr(list(some_list)))
ascii_to_string([123]))

def digit_sum_it (n):
    result = 0
    while n != 0:
        result += n % 10
        n //= 10
        return result

def digit_sum_rec (n:int) -> int : # n is integer 
    if not isinstance(n, int):
            return 'Must be integer'
        if n < 10:
        return n
    return n % 10 + digit_sum_rec(n // 10)      #!!! still gonna turn it into a float Ducktype