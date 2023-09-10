import time

def inter_section(lista, listb):
    return sorted(tuple(set(lista).intersection(listb)))

def search(search_for, search_object):
    start = time.time()
    test = search_for in search_object
    end = time.time()
    return end - start


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(f"In the two lists supplied ({list1} {list2}, the common numbers are {inter_section(list1, list2)}.")

max = 10000000
a = range(max)
x = set(a)
y = list(a)

search_value = input(f"What number do you want to search for, between 0 and {max-1} : ")

print(f"Searching the set took  {search(search_value, x)} milliseconds.")
print(f"Searching the list took {search(search_value, y)} milliseconds.")

