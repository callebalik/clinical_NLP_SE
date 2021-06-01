# # Empty nested dictionary
# Dict = { 'Dict1': { },
#          'Dict2': { }}
# print("Nested dictionary 1-")
# print(Dict)

# # Nested dictionary having same keys
# Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
#          'Dict2': {'name': 'Bob', 'age': '25'}}
# print("\nNested dictionary 2-")
# print(Dict)

# # Nested dictionary of mixed dictionary keys
# Dict = { 'Dict1': {1: 'G', 2: 'F', 3: 'G'},
#          'Dict2': {'Name': 'Geeks', 1: [1, 2]} }
# print("\nNested dictionary 3-")
# print(Dict)


# Dict = { }
# print("Initial nested dictionary:-")
# print(Dict)

# Dict['Dict1'] = {}

# # Adding elements one at a time
# Dict['Dict1']['name'] = 'Bob'
# Dict['Dict1']['age'] = 21
# print("\nAfter adding dictionary Dict1")
# print(Dict)

# # Adding whole dictionary
# Dict['Dict2'] = {'name': 'Cara', 'age': 25}
# print("\nAfter adding dictionary Dict1")
# print(Dict)

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp4'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
# Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#         'emp2': {'name': 'Kim', 'job': 'Dev'},
#         'emp3': {'name': 'Sam', 'job': 'Dev'},
#         'emp4': {'name': 'Max', 'job': 'Janitor'}}