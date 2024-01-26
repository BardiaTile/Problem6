def sort_letters(input_string):
    elements = input_string.split()
    input_pairs = []
    for element in elements:
        number = ''.join(filter(str.isdigit, element))
        character = ''.join(
            filter(lambda x: not x.isdigit(), element))
        input_pairs.append((character, int(number)))
    input_pairs.sort(key=lambda x: x[1])
    sorted_string = ''.join([pair[0] for pair in input_pairs])
    return sorted_string
user_input = input()
output_string = sort_letters(user_input)
print(output_string)