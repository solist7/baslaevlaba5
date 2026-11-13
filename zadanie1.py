n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers = numbers + [num]
positive = []
negative = []
for num in numbers:
    if num > 0:
        positive = positive + [num]
    elif num < 0:
        negatives = negatives + [num]
if len(positive) > 0 and len(negatives) > 0:
    min_positive = min(positives)
    min_abs_negative = max(negative)
    result = min_positive * min_abs_negative
    print(result)
else:
    print('Введите другие элементы')
