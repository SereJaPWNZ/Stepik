n = int(input())
sum_number = 0
for current_divider in range(1, n+1):
    if n % current_divider == 0:
        sum_number = current_divider + n // current_divider
print(sum_number)