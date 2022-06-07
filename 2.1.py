my_list = {1, 2.2, -3, (4 + 5j), 'word or text', True, None, [6, 7], (8, 9, 10.1), {11: 'eleven', 12: 'twelve'},
           {13, 14}, frozenset(), range(15), b'sixteen', bytearray(b'seventeen'), zip(*{
        (18, 19), (20, 21), ('a', 'b')}), TypeError}

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")



