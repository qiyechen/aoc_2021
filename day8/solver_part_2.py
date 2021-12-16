FILE_NAME = 'input.txt'

def solve():
    signals_list, outputs_list = get_signal_and_output_values()

    output_sum = 0
    for i in range(len(signals_list)):
        signal_num_map = find_signal_meaning(signals_list[i])
        output_number = decode_number(outputs_list[i], signal_num_map)
        output_sum += output_number

    print(output_sum)

def get_signal_and_output_values():
    signals_list = []
    outputs_list = []
    with open(FILE_NAME) as f:
        for line in f:
            signal, output = [x.strip().split() for x in [y for y in line.strip().split('|')]]
            signals_list.append(signal)
            outputs_list.append(output)
    f.close()
    return signals_list, outputs_list

def find_signal_meaning(signals):
    num_signal_map = [None] * 10
    five_segment_signals = []
    six_segment_signals = []

    for signal in signals:
        signal_len = len(signal)
        sorted_signal = "".join(sorted(signal))
        if signal_len == 2:
            num_signal_map[1] = sorted_signal
        elif signal_len == 3:
            num_signal_map[7] = sorted_signal
        elif signal_len == 4:
            num_signal_map[4] = sorted_signal
        elif signal_len == 7:
            num_signal_map[8] = sorted_signal
        elif signal_len == 5:
            five_segment_signals.append(sorted_signal)
        elif signal_len == 6:
            six_segment_signals.append(sorted_signal)
        else:
            raise Exception("Invalid signal.")

    for signal in five_segment_signals:
        if is_subset_of_characters(signal, num_signal_map[1]):
            num_signal_map[3] = signal
            five_segment_signals.remove(signal)
            break

    for signal in six_segment_signals:
        if is_subset_of_characters(signal, num_signal_map[3]):
            num_signal_map[9] = signal
            six_segment_signals.remove(signal)
            break

    for signal in six_segment_signals:
        if is_subset_of_characters(signal, num_signal_map[7]):
            num_signal_map[0] = signal
            six_segment_signals.remove(signal)
            break

    num_signal_map[6] = six_segment_signals[0]
    six_segment_signals.remove(six_segment_signals[0])

    for signal in five_segment_signals:
        if is_subset_of_characters(num_signal_map[6], signal):
            num_signal_map[5] = signal
            five_segment_signals.remove(signal)
            break

    num_signal_map[2] = five_segment_signals[0]
    five_segment_signals.remove(five_segment_signals[0])

    signal_num_map = create_map_value_to_index_from_array(num_signal_map)

    return signal_num_map

def create_map_value_to_index_from_array(arr):
    map = {}
    for i, value in enumerate(arr):
        map[value] = i

    return map

def decode_number(codes, signal_num_map):
    final_value = None
    for code in codes:
        sorted_code = "".join(sorted(code))
        if final_value == None:
            final_value = signal_num_map[sorted_code]
        else:
            final_value = concat_nums(final_value, signal_num_map[sorted_code])

    return final_value

def concat_nums(num_1, num_2):
    return int(str(num_1) + str(num_2))

def is_subset_of_characters(text_1, text_2):
    chars_1 = [char for char in text_1]
    chars_2 = [char for char in text_2]

    for char in chars_2:
        if char not in chars_1:
            return False

    return True

if __name__ == '__main__':
    solve()
