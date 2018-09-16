def ext_sort(input_list):
    """Sorts a list of file names based on extensions"""
    return sorted(input_list, key=lambda s: s.split(".")[1])


print(ext_sort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
