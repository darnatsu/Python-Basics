# Python Exercises

# 1. Create a function that will group the list of persons.
def group_list():

    new_dict = {}

    new_dict['A'] = ['Jay', 'Ana']
    new_dict['B'] = ['Kim', 'Kc']

    return new_dict

print(group_list())
        

# 2. Write a script that will insert data inside a list without using append.
countries = ['Philippines', 'Korea', 'Japan', 'Thailand', 'USA'];

def insert_data(list, value):
    list2 = list + [value]
    return list2

print insert_data(countries, 'Singapore')


# 3. Write a script that will return a list of odd numbers

def odd_numbers():
    odd = []
    for x in range(20):
        if x % 2 == 0:
            continue
        odd.append(x)

    return odd

print("Odd Numbers", odd_numbers())

# 4. Convert list of integer into single integer.
def convert_list_to_single(list):
    
    result = int("".join(map(str, list)))
    return result


print("List of integer to Single integer", convert_list_to_single(odd_numbers()))


# 5. Sort the numbers from smallest to largest
def sort_list(list):

    list.sort()
    return list

list_example = [9,7,4,6,11,15,8];
print("Sort Ascending", sort_list(list_example))

# 6. Check a list if it's empty
def is_list_empty(list):
    if len(list) == 0:
        return True
    else:
        return False

# list_example = [];
print("List is Empty", is_list_empty(list_example))


# 7. create a function that will convert arrays into dictionary.
def convert_arr_dict(array_keys, array_val):
    # result = {array_keys[i]: array_val[i] for i in range(len(array_keys))} 
    result = dict(zip(array_keys, array_val))
    return result


arr = ['moe', 'larry', 'curly']
arr1 = [30, 40, 50]

print("Convert Array", convert_arr_dict(arr, arr1))

# 8. create a function that will remove duplicate.
dup_list = [1,3,2,3,2,6,2]

def remove_duplicates(mylist):
    result = list(dict.fromkeys(mylist))
    return result

print("Remove duplicates", remove_duplicates(dup_list))

# 9. create a function that will return list of unique.
list1 = [1,2,3,1,3]

def unique_list(myList):
    result = []

    for x in myList:
        if myList.count(x) == 1:
            result.append(x)
    
    return result

print("Unique List", unique_list(list1))

# 10. create a function  that will find the index number from the list

def get_index(myList, value):
    return myList.index(value)

print("Get Index from List", get_index([1,3,4], 4))

# 11. create a function that Looks through the list and returns the first value that matches all of the key-value pairs listed in properties.
mylist = [{1: 'one', 'index': 0 }, {2: 'two', 'index': 1}, {3: 'three', 'index': 2}] 
def findObject(mylist, obj):
    for key, value in obj.items():
        for x in mylist:
            if key in x and value == x[key]:
                return x

print("Match dictionary from list, returns the first value.", findObject(mylist, {'index': 1}))


# 12. create  a function that will return True if the value is present in the list
def contains(myList, value):
    if value in myList:
        return True
    else:
        return False

print("Value is present in the list", contains([1,2,3], 3))

# 13. create a function that will returns the values from array that are not present in the other arrays.

def check_difference(list1, list2):
    result = [];

    for x in list1:
        if x not in list2:
            result.append(x)
    
    return result

print("Check Difference", check_difference([1, 2, 3, 4, 5], [5, 2, 10]))

# 14. create a function that will remove non-integer from list.

def remove_non_integer(list1):
    result = [];
    for x in list1:
        if isinstance(x, int):
            result.append(x)

    return result

print("Remove non-integer from list", remove_non_integer([2,'a', '2', {1: 'one'}]))

# 15. Write a python code to display given: [a,b,c] [x,y,z]
def display_vertical_list(myList):
    for x, y in zip(*myList):
        print x, y

print("Display list vertically")
display_vertical_list([['a','b','c'],['x','y','z']])

# 16. convert string "2535"  to list [2,5,3,5] using one line of code
def convert_string_to_list(str):
    return list(str)

print("Convert String to List", convert_string_to_list("2535"))