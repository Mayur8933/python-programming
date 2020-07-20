def digit_sum(n):
    num = 0
    for i in str(abs(n)):
        num = abs(int(i)) + num
    return abs(num)

digit_sum(-456)