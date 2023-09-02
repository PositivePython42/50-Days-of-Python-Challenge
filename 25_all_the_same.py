def all_the_same(check_this):
    if isinstance(check_this, str) == True:
        flag = 'the same'
        for element in range(0, len(check_this)-1):
            if check_this[element] != check_this[element + 1]:
                flag = 'not the same'
                return flag
        return flag
  
    elif isinstance(check_this, list) == True:
        if check_this.count(check_this[0]) == len(check_this):
            return 'the same'
        else:
            return 'not the same'
        
    elif isinstance(check_this, tuple) == True:
        flag = 'the same'
        for element in range(0, len(check_this)-1):
            if check_this[element] != check_this[element + 1]:
                flag = 'not the same'
                return flag
        return flag

def read_backwards(string):
    split_string = string.split(" ")
    split_string.reverse()
    backward_string = ' '.join(split_string)
    return backward_string

item_to_check = [ '111', '123', [1, 1, 1], [1, 2, 3], (1, 1, 1), (1, 3, 1)]

for item in item_to_check:
    print(f"The elements in {item} in are {all_the_same(item)}.")

input_string = input("\nEnter your string here : ")
print(f"The reverse of {input_string} is {read_backwards(input_string)}.")