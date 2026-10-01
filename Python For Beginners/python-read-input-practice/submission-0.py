def add_two_numbers() -> int:
    numbers = input()
    numbers = numbers.split(",")
    res = 0
    for num in numbers:
        num = int(num)
        res += num
    return res
    
    

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
