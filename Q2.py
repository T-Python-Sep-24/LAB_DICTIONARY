original_list = [5, 0, 34, 9, 0, 13, 8]
def zeros_end(lst):
    non_zero = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    new_list = non_zero + [0] * zero_count
    return new_list
new_list = zeros_end(original_list)
print("Arranged List:", new_list)