numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def chop(numbers):
    for n in numbers:
        numbers = numbers[1:len(numbers)-1]
    numbers.sort
    print numbers
        
chop(numbers)
