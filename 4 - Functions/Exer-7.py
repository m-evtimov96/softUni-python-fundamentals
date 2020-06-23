def is_perfect(number):
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
    if number == sum(divisors):
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number_to_check = int(input())
print(is_perfect(number_to_check))
