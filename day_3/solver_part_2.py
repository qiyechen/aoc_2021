filename = 'input.txt'

binary_list = []
with open(filename) as f:
    for line in f:
        bit_list = [int(x) for x in line.strip()]
        binary_list.append(bit_list)
f.close()

num_bit = len(binary_list[0])

o_filter_list = binary_list.copy()
o_bit = None
for x in range(num_bit):
    if len(o_filter_list) == 1:
        break

    o_num_of_one_bits_list = [sum(x) for x in zip(*o_filter_list)]

    if (o_num_of_one_bits_list[x] >= len(o_filter_list)/float(2)):
        o_bit = 1
    else:
        o_bit = 0

    o_filter_list_new = []
    for binary in o_filter_list:
        if binary[x] == o_bit:
            o_filter_list_new.append(binary)
    o_filter_list = o_filter_list_new

co2_filter_list = binary_list.copy()
co2_bit = None
for x in range(num_bit):
    if len(co2_filter_list) == 1:
        break

    co2_num_of_one_bits_list = [sum(x) for x in zip(*co2_filter_list)]

    if (co2_num_of_one_bits_list[x] >= len(co2_filter_list)/float(2)):
        co2_bit = 0
    else:
        co2_bit = 1

    co2_filter_list_new = []
    for binary in co2_filter_list:
        if binary[x] == co2_bit:
            co2_filter_list_new.append(binary)
    co2_filter_list = co2_filter_list_new

o_binary = int(''.join(str(x) for x in o_filter_list[0]), 2)
co2_binary = int(''.join(str(x) for x in co2_filter_list[0]), 2)

print(o_binary*co2_binary)