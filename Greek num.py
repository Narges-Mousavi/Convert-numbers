n = int(input('PLEASE ENTER A NUMBER : '))
numbers0_10 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
numbers10_10 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
numbers100 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
numbers1000 = ['', 'M', 'MM', 'MMM', 'MMMM', 'V|', 'V|M', 'V|MM', 'V|MMM', 'V|MMMM', 'X|']
numbers10000_100000 =['', 'X|', 'X|X|', 'X|X|X|', 'X|X|X|X|', 'L|', 'L|X|', 'L|X|X|', 'L|X|X|X|', 'L|X|X|X|X|', 'C|']
numbers100000_1000000 = ['', 'C|', 'C|C|', 'C|C|C|', 'C|C|C|C|', 'D|', 'D|C|', 'D|C|C|', 'D|C|C|C|', 'D|C|C|C|C|']
numbers1000000 = ['', 'M|', 'M|M|', 'M|M|M|', 'M|M|M|M|', 'M|M|M|M|M|']


def numbers(n):
    while n > 0:
        return numbers1000000[(n // 1000000)] + numbers100000_1000000[(n // 100000) % 10] + numbers10000_100000[(n // 10000) % 10] + numbers1000[(n // 1000) % 10] + numbers100[(n // 100) % 10] + numbers10_10[(n // 10) % 10] + numbers0_10[n % 10]
    if n <= 0:
        return 'not defined'

print(numbers(n))
