my_list = [1, [2, [3], [1, 2]], 4]
print('Список:', my_list)

# спосіб 1 -- for
my_list_copy = my_list.copy()
my_list_copy = str(my_list_copy)
my_list_copy = my_list_copy.replace('[', '').replace(']', '').replace(\
	',', '').replace(' ', '') # перетворюємо складний список на звичайний рядок,
# елементи якого можна перерахувати

result = 0
for i in my_list_copy:
	result += int(i)

print('for:', result)

# спосіб 2 -- while
def supersum(numbers):
	i = 0
	result = 0
	length = len(numbers)

	while i < length:
		if type(numbers[i]) == list:
			numbers[i] = supersum(numbers[i]) # замінюємо поточний елемент-список
			# на суму його елементів
		result += numbers[i]
		i += 1

	return result

print('while:', supersum(my_list))

# спосіб 3 -- рекурсія зі зміною
def sum_with_change(numbers):
	if len(numbers) == 0:
		return 0
	if type(numbers[0]) == list:
		numbers[0] = sum_with_change(numbers[0]) # замінюємо поточний елемент-список
		# на суму його елементів
	return numbers[0] + sum_with_change(numbers[1:]) # додаємо поточний елемент 
	# і суму наступних

print('recursion with change:', sum_with_change(my_list))

# спосіб 4 -- рекурсія з акумулюванням
def sum_accumulate(numbers, level = 0):
	if level == len(numbers): # кінець рекурсії
		return 0
	if type(numbers[level]) == list:
		current = sum_accumulate(numbers[level]) # знаходимо суму елементів 
		#поточного списка
	else:
		current = numbers[level]
	return current + sum_accumulate(numbers, level + 1)

print('recursion with accumulation:', sum_accumulate(my_list))	