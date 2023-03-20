def insert_min_to_start(arr):
    for row in arr:
        min_val = min(row)
        min_index = row.index(min_val)
        row[0], row[min_index] = row[min_index], row[0]

    return arr
my_array = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

new_array = insert_min_to_start(my_array)
print(new_array)
