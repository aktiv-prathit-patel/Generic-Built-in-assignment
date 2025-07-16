# Ask the user to enter a series of numbers (comma-separated) as input.
inp = input("enter a series of numbers (comma-separated) as input: ")
inp = inp.split(',')
input_list = [int(i.strip()) for i in inp]
print(input_list)
original_list = input_list

# From the list, remove all numbers less than 10.
less_ten_list = [i for i in input_list if i <10]
print('less than 10 list = ',less_ten_list)

# Check if all remaining numbers are even.
print('even number: ',[i for i in less_ten_list if i%2 == 0])

# Check if any of the remaining numbers are divisible by 5
print('divisible 5 list: ',[i for i in less_ten_list if i%5 == 0])

# Display the highest number, the lowest number, and the total of the remaining list.
print('max number = ',max(less_ten_list),'\nmin number = ',min(less_ten_list), '\nsum of total number = ',sum(less_ten_list))

# Show the list sorted in both ascending and descending order.
print('ascending order list = ',sorted(less_ten_list),'\ndescending order list = ',sorted(less_ten_list,reverse=True))

# Convert the original list into a tuple and a set, and print both.
list_2_tuple = tuple(less_ten_list)
list_2_set = set(less_ten_list)
print('list into tuple:',list_2_tuple ,'\nlist into set:',list_2_set)

# Print the type of all collections used and verify if each one belongs to its expected data type.
print('check all types :\n',less_ten_list,' : ',type(less_ten_list),'\n',list_2_tuple,' : ',type(list_2_tuple),'\n',list_2_set,' : ',type(list_2_set))

# Pair each number in the original list with its square and display the result.
print('list with its square: ',[i**2 for i in original_list])

