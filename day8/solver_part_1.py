FILE_NAME = 'input.txt'
UNIQUE_SEG_NUMS = [2, 4, 3, 7]  # 1, 4, 7, 8

def solve():
    signals, outputs = get_signal_and_output_values()
    flat_outputs = flat_two_dimensional_array(outputs)
    unique_num_count = count_value_with_lengths(flat_outputs, UNIQUE_SEG_NUMS)

    print(unique_num_count)

def get_signal_and_output_values():
    signals = []
    outputs = []
    with open(FILE_NAME) as f:
        for line in f:
            signal, output = [x.strip().split() for x in [y for y in line.strip().split('|')]]
            signals.append(signal)
            outputs.append(output)
    f.close()
    return signals, outputs

def flat_two_dimensional_array(array):
    return [value for sublist in array for value in sublist]

def count_value_with_lengths(values, lengths):
    counter = 0

    for value in values:
        if len(value) in lengths:
            counter += 1

    return counter

if __name__ == '__main__':
    solve()
