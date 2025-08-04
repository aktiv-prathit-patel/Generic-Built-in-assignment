# Ask the user to enter a series of numbers (comma-separated) as input.
inp = input("Enter a series of numbers (comma-separated) as input: ")
inp = inp.split(",")
inp = [i for i in inp ]
inp = [int(i) for i in inp if i!=" " and i!="," and i != ""]
print(inp)
input_list = inp.copy()
print("\nList of integers")
for inti in input_list:
  print(inti)
original_list = input_list.copy()

# From the list, remove all numbers less than 10.
less_ten_list = [i for i in input_list if i <10]
print('\nLess than 10 list = ',less_ten_list)

# Check if all remaining numbers are even.
print('\nEven number: ',[i for i in less_ten_list if i%2 == 0])

# Check if any of the remaining numbers are divisible by 5
print('\nDivisible 5 list: ',[i for i in less_ten_list if i%5 == 0])

# Display the highest number, the lowest number, and the total of the remaining list.
if not less_ten_list: 
    print('\nRemaining list is empty \nSo max number, min number, sum, Ascending-descending not possible')
else:
    print('\nMax number = ',max(less_ten_list),'\nmin number = ',min(less_ten_list), '\nsum of total number = ',sum(less_ten_list))

# Show the list sorted in both ascending and descending order.
    print('\nAscending order list = ',sorted(less_ten_list),'\ndescending order list = ',sorted(less_ten_list,reverse=True))

# Convert the original list into a tuple and a set, and print both.
list_2_tuple = tuple(original_list)
list_2_set = set(original_list)
print('\nList into tuple:',list_2_tuple ,'\nlist into set:',list_2_set)

# Print the type of all collections used and verify if each one belongs to its expected data type.
print('\nCheck all types :\n',original_list,' : ',type(original_list),'\n',list_2_tuple,' : ',type(list_2_tuple),'\n',list_2_set,' : ',type(list_2_set))

# Pair each number in the original list with its square and display the result.
print('\nList with its square: ',[i**2 for i in original_list])
