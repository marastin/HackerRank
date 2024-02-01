def print_formatted(number):
    # your code goes here
    max_number = number
    max_len = len(str(bin(max_number))[2:])
    for i in range(1, max_number + 1):
        s = str(i).rjust(max_len, " ") + str(oct(i))[2:].rjust(max_len + 1, " ") + str(hex(i))[2:].rjust(max_len+1, " ").upper() + str(bin(i))[2:].rjust(max_len+1, " ")
        print(s)

if __name__ == '__main__':
    n = 20#int(input())
    print_formatted(n)