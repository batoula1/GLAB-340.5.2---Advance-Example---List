
# Problem 1
# Using the list below, use a Class method to add the string "skirt" to the end of the list.
clothing= ['socks', 'pants', 'shirt', 'polo']
clothing.append("skirt")
print(clothing)

# Problem 2
# Using the same list as above, add a list to the 2nd index that includes the following strings:
# 'suit jacket', 'suit pants', 'tie', 'button down'
clothing.insert(2,['suit jacket', 'suit pants', 'tie', 'button down'])
print(clothing)

# Problem 3
# Use the list below and use a Class method to get the total number of times the integer 14 appears in the list.
nums= [2, 150, 14, 36, 78, 81, 14, 1000, 54, 14, 14]
print(nums.count(14))

# Problem 4
# Use the same list as above
# Use a built-in function to find the total of all the numbers in the list.
print(sum(nums))

# Problem 5
# Use the same list as above
# Slice the list so that it is reversed without using the .reverse() method
print(nums[::-1])

# Problem 6
# Use the list below.
# Slice the list so only the last two elements are included in the slice.
one_to_five= [1, 2, 3, 4, 5]
print(one_to_five[-2:])

# Problem 7
# Use the list below
# Write a for loop so that every item in the list is printed
animals= ["koala", "cat", "fox", "panda", "chipmunk", "sloth"]
for animal in animals:
    print(animal)

# Problem 8

# Use the list below
# Create a function that accepts a list as an argument
# Check if the data type at each index is a list
# If it is a list, check the length of the list. If it is greater than 3, add the second element to a new list.
# Return the new list
random_things= ['hello', ['breakfast', 'you', 'pencil', 2], 22, ['burrito', 'taco'],
                [22, 'win', 33, [5], 'laptop']]

def jessSorting(list_to_sort):

    new_list = []

    for item in list_to_sort:
        if type(item) is list:
            if len(item) > 3:
                new_list.append(item[1])

    
    return new_list


list2 = jessSorting(random_things)
print(list2)

# Problem 9
# Use the list below
# Create a new list
# Use a for loop and the append() method to append each item with a Dr. prefix to the new list.
names= ['Dre', 'Seuss', 'Who', 'McCoy']
Doctors = []
for name in names:
  Doctors.append("Dr."+name)
print(Doctors)

# Problem 10
# Use the list below
# Use a while loop, iterate through the list and if there is an integer 100, print a message that says what index the 100 is at
# Example: "There is a 100 at index no: 5"
num2= [10, 99, 85, 76, 43, 2, 77, 100, 13, 12, 42, 99, -1, -100]

counter = 0
while counter < len(num2):
    if num2[counter] == 100:
        print(f"There is a 100 at index no: {counter}") 
        break

    counter += 1

# Problem 11
# Use the list below
# Create a new list
# Use a for loop or a whole loop to iterate through the list and append all the elements in the old list, to the new list UNLESS the element is an empty string

list1= ["McDonald's", "Wendy's", "", "Burger King", "", "Taco Bell"]
new_list = []
for i in list1:
  if i:
    new_list.append(i)
print(new_list)


my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.append(another_list)
print(my_list)  # Output: [1, 2, 3, [4, 5, 6]]

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
  # Output: [1, 2, 3, 4, 5, 6]
another_list.append(7)
print(my_list,another_list)