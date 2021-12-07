filename = 'input.txt'

total_increase = 0
previous_sum = None
with open(filename) as f:
        num_list = [int(x) for x in f]
        index = 2
        while index < len(num_list):
            sum = num_list[index - 2] + num_list[index - 1] + num_list[index]
            if previous_sum != None and sum > previous_sum:
                total_increase += 1
            previous_sum = sum
            index += 1
f.close()
print(total_increase)