def sort_unique_after_at():
    unique_text = set()
    try:
        num_lines = int(input())
        if not 1 <= num_lines <= 1000:

            return
    except ValueError:
        print("You did not enter a valid number.")
        return

    for _ in range(num_lines):
        line = input()
        if '@' in line:
            text_after_at = line.split('@', 1)[1]
            unique_text.add(text_after_at.strip())

    sorted_text = sorted(unique_text)
    for text in sorted_text:
        print(text)
sort_unique_after_at()