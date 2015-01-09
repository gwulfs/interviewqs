arr = [1, 7, 3, 4]
def get_products_of_all_ints_except_at_index(arr):
	prev = 0
	vals = []
	for i, num in enumerate(arr):
		val = 1
		for j in range(i+1, len(arr)):
			val *= arr[j]
		if i is 0:
			vals.append(val)
			prev = num
		else:
			vals.append(val*prev)
			prev *= num
	return vals
vals = get_products_of_all_ints_except_at_index(arr)
print vals