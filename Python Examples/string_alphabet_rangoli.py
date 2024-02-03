import string


def print_rangoli(size):
    al = list(string.ascii_lowercase)

    lines = ''
    for i in range(1, size):
        line = al[size - 1 : size - i : -1] + al[size - i: size]
        lines += ('-'.join(line)).center(4*(size-1)+1, '-') + '\n'
    for i in range(size, 0 , -1):
        line = al[size - 1 : size - i : -1] + al[size - i: size]
        lines += ('-'.join(line)).center(4*(size-1)+1, '-') + '\n'
    print(lines)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)