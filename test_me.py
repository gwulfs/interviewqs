from merge_sorted_arrays import merge_arrays
def test_merge():
	assert merge_arrays([3,4,6,10,11,15], [1,5,8,12,14,19]) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]