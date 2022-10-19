# print 1 to 100
# if divisible by 3 print Fizz
# if divisible by 5 print Buzz
# if divisible by 3 and 5 print FizzBuzz

# def fizz_buzz(x):
#     if (x % 3 == 0) and (x % 5 == 0):
#         return 'FizzBuzz'
#     elif x % 3 == 0:
#         return 'Fizz'
#     elif x % 5 == 0:
#         return 'Buzz'
#     else:
#         return x

# # passing the fizzbuzz logic as a element in a list and iterate throughout the list of values
# fizz_buzz_logic = [
#     lambda x: 'Fizz' if (x % 3 == 0) else '',
#     lambda x: 'Buzz' if (x % 5 == 0) else '',
# ]


# def fizz_buzz(x):
#     final_str = ''
#     for i in fizz_buzz_logic:
#         final_str += str(i(x))

#     if not final_str:
#         return x

#     return final_str


def fizz():
    return 'Fizz'


def buzz():
    return 'Buzz'


fizz_buzz_dict = {
    3: fizz,
    5: buzz
    }


def fizz_buzz(x):
    final_str = ''
    for key, value in fizz_buzz_dict.items():
        if x % key == 0:
            final_str += value()
    if not final_str:
        return x
    return final_str


def main():
    output = [fizz_buzz(i) for i in range(1, 101)]
    for i in output:
        print(i)


if __name__ == "__main__":
    main()
