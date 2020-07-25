empty_list = []
for i in range(5):
    rows = []
    for j in range(10):
        rows.append(i*j)
    empty_list.append(rows)
print(empty_list)