def is_palindrome(num):
    flipped_num = 0
    original_num = num
    while num > 0:
        flipped_num = flipped_num*10 + num%10
        num = num//10
    if original_num == flipped_num:
        return True
    return False
    
largest_palindrome = 0
for num_1 in range(100,1000):
    for num_2 in range(100,1000):
        product = num_1*num_2
        if product>largest_palindrome and is_palindrome(product):
            largest_palindrome = product
print(largest_palindrome)
        