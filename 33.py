def unique(input_list, key=lambda v: v):
    """Returns a list of unique elements in the input list"""
    output = []
    for elem in input_list:
        elem = key(elem)
        if elem not in output:
            output.append(elem)
    return output




print(unique(["python", "java", "Python", "Java"],key=lambda s: s.lower()))