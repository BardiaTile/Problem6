def sum_all_divisors(number):
    return sum([i for i in range(1, number+1) if number % i == 0])


def convert_to_base(number, base):
    if number == 0:
        return '0'
    nums = []
    while number:
        number, i = divmod(number, base)
        nums.append(str(i))
    return ''.join(reversed(nums))


def is_valid_base(num):
    return 2 <= num <= 9


input_data = []
invalid_base_used = False

while True:
    current_input = input()
    num1, num2 = map(int, current_input.split())
    if num1 == num2 == -1:
        break
    if not is_valid_base(num2):
        invalid_base_used = True
        continue
    input_data.append((num1, num2))


total_sum = 0
for num1, num2 in input_data:
    sum_divisors = sum_all_divisors(num1)
    try:
        sum_divisors_in_base = convert_to_base(sum_divisors, num2)
        total_sum += int(sum_divisors_in_base)
    except ValueError:
        continue

if invalid_base_used:
    print('invalid base!')
else:
    print(total_sum)