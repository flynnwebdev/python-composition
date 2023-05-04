from calculator import square, cube

nums = [10, 14, 21, 50, 5, -6]

squared_values = map(lambda num: num * num, nums)
# cubed_values = map(cube, nums)
# squared_values = [square(num) for num in nums]
# for x in nums:
#   squared_values.append(square(x))

# print(nums)
print(list(squared_values))
# print(list(cubed_values))

# def add_prefix(index, value):
#   # index, value = tuple
#   return f'{index + 1}. {value.strip()}'

# with open('shopping-list.txt') as f:
#   # numbered = map(add_prefix, list(enumerate(f)))
#   numbered = [add_prefix(index, value) for index, value in enumerate(f) if index % 2 == 0]
#   print(numbered)

students = [
  {'name': 'Harry', 'house': 'Gryffindor'},
  {'name': 'Ron', 'house': 'Gryffindor'},
  {'name': 'Hermione', 'house': 'Gryffindor'},
  {'name': 'Draco', 'house': 'Slytherin'},
]

# print([student['name'] for student in students if student['house'] == 'Gryffindor'])

# def is_gryffindor(student):
#   return student['house'] == 'Gryffindor'

# def get_name(student):
#   return student['name']

gryffindor_students = filter(lambda s: s['house'] == 'Gryffindor', students)
print(list(map(lambda s: s['name'], gryffindor_students)))
