def return_sum_sub(arg1, arg2):
    return(arg1 + arg2, arg1 - arg2 if arg1 > arg2 else arg2 - arg1)

print(return_sum_sub(5, 3))

