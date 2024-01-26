num_col = int(input())
symbols = []
while True:
    ins = input().strip()
    if ins == "END":
        break
    symbols.append(ins)

current_col, current_row = 0, 0
output = [["."] * num_col]
output[current_row][current_col] = "*"
for symbol in symbols:
    if symbol == "L" and current_col > 0:
        current_col -= 1
    elif symbol == "R" and current_col < num_col - 1:
        current_col += 1
    elif symbol == "B":
        current_row += 1
        output.append(["."] * num_col)

    output[current_row][current_col] = "*"

for row in output:
    print(" ".join(row))

if current_row < len(output) - 1 or current_col < num_col - 1:
    print("There's no way out!")