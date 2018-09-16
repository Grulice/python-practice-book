def lensort(input_list):
    result = []
    len_list = []
    for elem in input_list:
        len_list.append([elem, len(elem)])

    len_list.sort(key=lambda x: x[1])

    return list(map(lambda x: x[0], len_list))

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
