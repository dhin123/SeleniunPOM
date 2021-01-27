def isZigzag(numbers):
    n = len(numbers)
    output = [0] * (n -2)

    for i in range(len(output)):
        if (numbers[i] < numbers[i+1] >numbers[i+2]) or (numbers[i] > numbers[i+1]<numbers[i+2]):
            output[i] = 1
        else:
            output[i] = 0
    print(output)

numbers = [1000000000, 1000000000, 1000000000]
print(isZigzag(numbers))