from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'At {t}, the index of 5.6 is {seq_search(t, 5.6)}')
print(f'At {s}, the index of "n" is {seq_search(s, "n")}')
print(f'At {a}, the index of "DTS" is {seq_search(a, "DTS")}')