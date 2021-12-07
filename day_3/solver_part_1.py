filename = 'input.txt'

binary_list = []
with open(filename) as f:
    for line in f:
        bit_list = [int(x) for x in line.strip()]
        binary_list.append(bit_list)
f.close()

num_binary = len(binary_list)
num_of_one_bits_list = [sum(x) for x in zip(*binary_list)]
gamma_bit_list = [0 for x in range(len(num_of_one_bits_list))]
epsilon_bit_list = [0 for x in range(len(num_of_one_bits_list))]

for x in range(len(num_of_one_bits_list)):
    if (num_of_one_bits_list[x] > num_binary/2):
        gamma_bit_list[x] = 1
        epsilon_bit_list[x] = 0
    else:
        gamma_bit_list[x] = 0
        epsilon_bit_list[x] = 1

gamma_binary = int(''.join(str(x) for x in gamma_bit_list), 2)
epsilon_binary = int(''.join(str(x) for x in epsilon_bit_list), 2)

print(gamma_binary*epsilon_binary)