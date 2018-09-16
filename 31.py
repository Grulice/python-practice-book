from builtins import print


def group(input_list, chunk_size):
    result = []
    while len(input_list) > 0:
        result.append(input_list[:chunk_size])
        input_list = input_list[chunk_size:]
    return result


my_list = [1, 2, 3, 4]
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

