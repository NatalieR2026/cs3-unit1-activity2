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

print("!" in my_list)
my_list.sort(reverse=True)
print(my_list)
print(sorted(my_list))
print(my_list)

# PART B: Tuples

# PART C: Sets

# PART D: Dictionaries