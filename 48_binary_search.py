def search_binary(search_list, search_number):
    
    l = 0
    r = len(search_list)
    
    while l <= r:
        m = l + (r-1) // 2
        if search_list[m] == search_number:
            return m
        elif search_list[m] < search_number:
            l = m + 1
        else:
            r = m - 1
            
    return "It is not in the list."


list1 = [12, 34, 56, 78, 98, 22, 45, 13]
list1.sort()

print(f"The index of the number 22 in your list {list1} is {search_binary(list1, 22)}.")