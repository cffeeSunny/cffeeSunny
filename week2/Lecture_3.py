#look up live coding, there are some things you missed
from multiprocessing.forkserver import set_forkserver_preload

my_tuple_of_lists = (['ben','stock'],['jonas','schmitt'])
for i,entry in enumerate (my_tuple_of_lists):
    print(f"{i}-th student: {entry}")

#entry is (first,last)

for i, (first,last) in enumerate(my_tuple_of_lists):
    print (f"{i}-th student: First name: {first}, last name: {last}")



for i,entry in enumerate (my_tuple_of_lists[::2]):
    print(f"{i}-th student: {entry}")

student_pets = ['cat','horse','cat','dog','bunny']
tutor_pets = ['cat','horse','elephant']
both_pets = []
for sp in student_pets:
    if sp in tutor_pets and sp not in both_pets:
        both_pets.append(sp)
print(both_pets)
set(student_pets)
set (student_pets) & set(tutor_pets)
{'cat'}


s= set(student_pets)
t = set(tutor_pets)
print('only in students', s-t)
print('only in tutors', t-s)
print('intersection of tut and stud', t & s)
print('in students union in tutors', t|s) #if you use + its not supported
print ('Not in both', t^s)
#the order is not the same in the answer as in the given
# lists and sets are different, you need to specify in jupyter that you want set(a), when a is a list first
for anmila in t^s:
    print(anmila)


#tuples cannot be updated
#emails is a dict
emails = {'ben': 'stock@cispa.de','jonas':'jonas@jonas'}
#ben and jonas are key, with wich you find
#you find the in the key
emails['ben']
#emails['nicolas']
#gives error, see in live coding how to return false if

emails.get('nicolas','doesnotexist')
#if no second gets None
for entry in emails:
    print(entry) #gets you the keys only

for entry in emails.keys():
    print(entry)

for entry in emails.values():
    print(entry)

for entry in emails.items():
    print(entry)

for first, email in emails.items():
    print(f"{first}: has {email}")


#def print_my_height(height_in_cm, unit: str = 'cm'):
 #   if unit == 'cm' then...

#can be print_my_height(183, unit = 'cm')
#can be (unit = 'cm', height_in_cm = 183)
#CANNOT BE print...(

def add_to_my(value: str, my_set: set = set()) -> set():
    my_set.add(value)
    return my_set

add_to_my('foo')
add_to_my('bar')



#makes the above my_set to foo, and then adds bar

def add_to_my (value: str, my_set: set = None) -> set():
    if my_set is None:
        my_set = set()
    my_set.add(value)
    return my_set

add_to_my('foo')
add_to_my('bar')

#keeps my_set immutable