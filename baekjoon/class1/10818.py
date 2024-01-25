cnt = int(input())
num_list = list(map(int, input().split()))
max_value = num_list[0]
min_value = num_list[0]

for i in num_list:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i
print(min_value, max_value)