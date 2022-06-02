#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    if count == 1:
        print("{}", "{}".format(count, "argument"))
    elif count != 1:
        print("{:s}".format("arguments"))
    else:
        print("{}" or "{}".format(":", "."))
