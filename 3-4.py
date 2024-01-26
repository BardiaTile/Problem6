numbers = list(map(int, input().split()))
target = int(input())
index_sums = []
nums_to_indices = {}
for i, number in enumerate(numbers):
    complement = target - number
    if complement in nums_to_indices:
        index_sums.append(i + nums_to_indices[complement])
    nums_to_indices[number] = i
if index_sums:
    index_sums.sort()
    for sum_of_indices in index_sums:
        print(sum_of_indices)
else:
    print("Not Found!")