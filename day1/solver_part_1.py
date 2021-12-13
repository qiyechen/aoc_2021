filename = 'input.txt'

total_increase = 0
previous_num = None
with open(filename) as f:
        num_list = [int(x) for x in f]
        for num in num_list:
            if previous_num != None and num > previous_num:
                total_increase += 1
            previous_num = num
f.close()
print(total_increase)