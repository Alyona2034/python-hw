nums = [1, 3, 5, 6, 11, 15, 23, 26, 28, 41, 52, 57, 58, 60, 63, 65, 66, 67, 82, 95]
quant = []
prob = []
n = len(nums)
j = 0
a = 0
count = 0
for i in range(1, 11):
    while nums[a] < 10*i:
        count += 1
        if nums[a] == nums[n - 1]:
            break
        a += 1
    quant.append(count)
    prob.append(count/n)
    count = 0
print(f"{quant}, {prob}")