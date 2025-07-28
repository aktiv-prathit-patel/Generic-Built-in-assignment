# Create a dictionary with keys: "name" (string), "age" (integer), and "scores" (list of integers)
Data = {'name':'Billy','age':39,'score':[89,47,61,50]}

# Display all available operations or attributes that can be performed on this dictionary.
print("\n===Dictionary Operations ===")
operation_perform_data = Data.copy()
print('Copy of the dictionary',operation_perform_data)
print('All the values in the dictionary', operation_perform_data.values())
key = operation_perform_data.keys()
print('List containing the dictionary keys', key)
items = operation_perform_data.items()
print("List containing a tuple for each key value pair", operation_perform_data.items())
print("Use get method for age data get: ", operation_perform_data.get('age'))
operation_perform_data.setdefault('surname','Conifer')
print("Use setdefault value: ",operation_perform_data)
operation_perform_data.update({'name':"john"})
print("Use setdefault value: ",operation_perform_data)
operation_perform_data.pop('age')
print("Use pop to remove age ", operation_perform_data)
operation_perform_data.popitem()
print('Use popitem to remove last key-pair', operation_perform_data)
print("Use clear to remove all directory", operation_perform_data.clear())

# Ask the user to enter a mathematical expression as a string and evaluate its result.
enter_mth_str = input('\nEnter Mathematical string : ')
result = eval(enter_mth_str)
print('Mathematical operation result: ',result)

# Convert the evaluated result into both float and integer types and print them.
print('\nResult in integer', int(result),'\nresult in float :',float(result))

# Convert a list into a string, and then convert it back to its original form.
list_test = ['a','b','c','d']
string_test = " ".join(list_test)
print("\n",list_test, "list into string", string_test)
print(string_test, "string into list", string_test.split(" "))

# From the "scores" list, display a subset of elements using a range of indices.
print('\n')
for index, value in enumerate(Data['score']):
    print(f"Index: {index}, Value: {value}")

# Loop over a range of numbers, round each to the nearest whole number, and convert to string.
float_num = [1.2,3.12,5.78,8.90]
print("\nFloat num ",float_num)
round_num = [round(i) for i in float_num]
print('Round each to the nearest whole number', [round(i) for i in float_num])
string_con =[str(i) for i in float_num]
print('Convert string: ',''.join(string_con))

# Access the first three elements of the "scores" list using a manual iteration approach.
scores_first_3 = Data['score'][:3]
scores_first_3 = iter(scores_first_3)
try:
    while True:
        element = next(scores_first_3)
        print(element)
except StopIteration:
    print("End of list reached.")

# Test and display the truthiness of the following: an empty list, a non-zero number, and an empty string.
check_list = []
num = 1
check_string = ""

print("\nEmpty list:", bool(check_list))
print("\nNon-zero number:", bool(num))
print("\nEmpty string:", bool(check_string))
