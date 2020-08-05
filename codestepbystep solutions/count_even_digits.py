def count_even_digits(num,length):
    empty_list = []
    for i in str(num):
        if int(i) % 2 == 0:
            empty_list.append(i)
    print(empty_list)
    print(len(empty_list))


count_even_digits("8346387", 7)

