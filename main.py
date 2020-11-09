list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
print(list_to_sort)
listy=sorted(list_to_sort, key=lambda posort: (posort[1], posort[2]))
print(listy)
