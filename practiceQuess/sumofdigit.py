test_list = [12, 67, 98, 34]

res = []

for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum = sum + int(digit)
    res.append(sum)

print(res)