# Data Collection Drills

# PART A: Lists

my_list = ['p','y','t','h','o','n']
print(my_list)
# ['p','y','t','h','o','n']

my_list.append('!')
print(my_list)
# added ! to the end

print(len(my_list))
# 7

print(my_list[2:6])
# ['t','h','o','n']

print(my_list[4:])
# ['o','n','!'] prints values at index 4 and on

print(my_list[-2:])
# ['n','!'] prints from index 2 from the right

my_list.remove('h')
print(my_list)
# ['p','y','t','o','n','!']

my_list.insert(3, 'h')
print(my_list)
# ['p','y','t','h','o','n','!']

del my_list[0]
print(my_list)
# ['y','t','h','o','n','!'] removed the first letter/index/value

last_item = my_list.pop()
print(last_item)
print(my_list)
# ! ['y','t','h','o','n'] saved last index and printed without it

print(my_list[2])
# h

print('!' in my_list)
# false, because the ! was already removed

my_list.sort(reverse=True)
print(my_list)
# moved h to the end, sort() returned but didn't print

print(sorted(my_list))
print(my_list)
# sorted flips it and my list is still normal


# PART B: Tuples

my_tuple = ('salt','sugar','pepper')
print(my_tuple)
# 'salt', 'sugar', 'pepper'

print(my_tuple[0])
print(my_tuple[-1])
# salt, pepper. works starting at index 0 then going to the other side of list

# my_tuple[1] = 'garlic'
# 'tuple' object does not support item assignment

one_item = ('hello',)
print(one_item)
# has comma after and still works

colors = ('red','blue','red','green','red')
print(colors.count('red'))
# 3

print(colors.index('green'))
# 3


# PART C: Sets

my_set = {'anteater', 'beluga', 'cheetah'}
print(my_set)
# doesn't match the order I typed, goes last->first->second

my_set.add('ocelot')
print(my_set)
# added new value to the end

my_set.add('beluga')
print(my_set)
# nothing changed, because beluga was already a value in the set

my_set.remove('anteater')
print(my_set)
# 'anteater' was removed

my_set.discard('panther')
# no error, nothing happens

fish = {'beluga','manta ray','piranha'}
all_animals = my_set.union(fish)
print(all_animals)
# result: 'ocelot', 'manta ray', 'beluga', 'piranha', 'cheetah'
# no duplicates, condensed two 'beluga' values to one


# PART D: Dictionaries

my_dict = {'name': 'Natalie', 'age': 17, 'grade': '11th'}
print(my_dict)
# name, age, grade and all their values

print(my_dict['age'])
# 17

# print(my_dict['school'])
# I didn't get any error message, just "KeyError"

my_dict['grade'] = '12th'
print(my_dict)
# yes, the value updated

my_dict['school'] = 'Central High'
print(my_dict)
# school: Central High

del my_dict['age']
print(my_dict)
# key and value is missing for age

print(my_dict.get('locker'))
# "None" and no error message

for key, value in my_dict.items():
 print(key,'->',value)
# everything got printed, but with a line between each key+value and an arrow pointing from key to value