def is_polindrome(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num / 10

    return True if n == rev else False

input_array = range(100,1000)
output_array = [x for sublist in map(lambda a: [item*a for item in input_array], input_array) for x in sublist]

print max(filter(lambda x: is_polindrome(x), output_array))
