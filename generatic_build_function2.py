# Create a dictionary with keys: "name" (string), "age" (integer), and "scores" (list of integers)
Data = {'name':'Billy','age':39,'score':[89,47,61,50]}
operation_perform_data = Data

# Display all available operations or attributes that can be performed on this dictionary.
print('all the values in the dictionary', operation_perform_data.values())
x = operation_perform_data.copy()
print('copy of the dictionary',x)
key = operation_perform_data.keys()
print('list containing the dictionary keys', key)
items = operation_perform_data.items()
print("list containing a tuple for each key value pair", operation_perform_data.items())
print("use get method for age data get: ", operation_perform_data.get('age'))
operation_perform_data.setdefault('surname','Conifer')
print("use setdefault value: ",operation_perform_data)
operation_perform_data.update({'name':"john"})
print("use setdefault value: ",operation_perform_data)
operation_perform_data.pop('age')
print("Use pop to remove age ", operation_perform_data)
operation_perform_data.popitem()
print('use popitem to remove last key-pair', operation_perform_data)
print("use clear to remove all directory", operation_perform_data.clear())

# Ask the user to enter a mathematical expression as a string and evaluate its result.
enter_mth_str = input('Enter Mathematical string : ')
result = eval(enter_mth_str)
print('Mathematical operation result: ',result)

# Convert the evaluated result into both float and integer types and print them.
print('result in integer', int(result),'\nresult in float :',float(result))

# Convert a list into a string, and then convert it back to its original form.
list_test = ['a','b','c','d']
string_test = " ".join(list_test)
print(list_test, "list into string", string_test)
print(string_test, "string into list", string_test.split(" "))

# From the "scores" list, display a subset of elements using a range of indices.
for index, value in enumerate(list_test):
    print(f"Index: {index}, Value: {value}")

# Loop over a range of numbers, round each to the nearest whole number, and convert to string.
float_num = [1.2,3.12,5.78,8.90]
print("float num ",float_num)
round_num = [round(i) for i in float_num]
print('round each to the nearest whole number', [round(i) for i in float_num])
string_con =[str(i) for i in float_num]
print('convert string: ',''.join(string_con))

# Access the first three elements of the "scores" list using a manual iteration approach.
scores_first_3 = Data['score'][:4]
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

print("Empty list:", bool(check_list))
print("Non-zero number:", bool(num))
print("Empty string:", bool(check_string))