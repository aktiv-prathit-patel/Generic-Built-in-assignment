# Create a dictionary with keys: "name" (string), "age" (integer), and "scores" (list of integers)
Data = {'name':'Billy','age':39,'score':[89,47,61,50]}

# Display all available operations or attributes that can be performed on this dictionary.
operation_perform_data = Data.copy()

print('\nCopy of the dictionary',operation_perform_data)
print('\nAll the values in the dictionary', operation_perform_data.values())

key = operation_perform_data.keys()
print('\nList containing the dictionary keys', key)

items = operation_perform_data.items()
print("\nList containing a tuple for each key value pair", operation_perform_data.items())
print("\nUse get method for age data get: ", operation_perform_data.get('age'))

operation_perform_data.setdefault('surname','Conifer')
print("\nUse setdefault value: ",operation_perform_data)

operation_perform_data.update({'name':"john"})
print("\nUse setdefault value: ",operation_perform_data)

operation_perform_data.pop('age')
print("\nUse pop to remove age ", operation_perform_data)

operation_perform_data.popitem()
print('\nUse popitem to remove last key-pair', operation_perform_data)
print("\nUse clear to remove all directory", operation_perform_data.clear())

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
print(string_test, "string into list", string_test.split(" "),"\n")

# From the "scores" list, display a subset of elements using a range of indices.
for index, value in enumerate(Data['score']):
    print("Index: ",index, "Value: ",value)

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

print("\nIteration approach score first 3 element")
while True:
    try:
        element = next(scores_first_3)
        print("",element)
    except:
        print("End of loop\n")
        break

# Test and display the truthiness of the following: an empty list, a non-zero number, and an empty string.
#Check List empty or not
check_list = list(input("Enter list: "))
check_list = [i for i in check_list if i != " " and i != ""]
if bool(check_list):
    print("Not Empty list\n")
else:
    print("List Empty")
#Check number is zero or not
try:
    check_num= float(input("\nEnter number: "))
    if bool(check_num):
        print("Non Zero")
    else:
        print("Zero number")
except:
    print("Not a number")

#Check String or not
check_string = input("\nEnter any string: ")
if bool(check_string):
    print("String not empty")
else:
    print("Empty string")
