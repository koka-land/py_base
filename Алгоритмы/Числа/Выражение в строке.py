s = input()
op = nums = s

print(eval(s))

operand = ['+', '-']

for i in range(10):
    op = op.replace(str(i), '')

for i in operand:
    nums = nums.replace(i, ' ')
nums = list(map(int, nums.split(' ')))

for i in op:
    if i == '+':
        nums[0] = nums[0] + nums[1]
    if i == '-':
        nums[0] = nums[0] - nums[1]
    nums.pop(1)

print(nums[0])
