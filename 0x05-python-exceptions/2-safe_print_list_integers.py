def safe_print_list_integers(my_list=[], x=0):
    k = 100
    for i in range(0, k):
        try:
            print("{:d}".format(my_list[0:3]), end="")
            x += 1
        except ValueError:
            pass
        return x
