input_text = input()
updated_text = ""
at_count = 0 
for char in input_text:
    if char == '@':
        at_count += 1
        updated_text += char
    elif char == '#' and at_count > 0:
        at_count -= 1
    else:
        updated_text += char
updated_text = updated_text.strip()
updated_text = ' '.join(updated_text.split())
updated_text = updated_text.replace('\\n', '\n')
print("Formatted Text: " + updated_text)