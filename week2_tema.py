l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(l)

list_asc = l.copy()
list_asc.sort()
print(list_asc)

list_desc = l.copy()
list_desc.sort(reverse=True)
# list_desc.sort()
# list_desc.reverse()
print(list_desc)

odd_list = list_asc[0::2]
print(odd_list)

even_list = list_asc[1::2]
print(even_list)

mult3_list = [i for i in list_asc if i % 3 == 0]
print(mult3_list)