from itertools import permutations



def increasing_lists_generator(n, current_list=[]):
    if n == 0:
        yield current_list
        return
    
    for i in range(10):
        if not current_list or i >= current_list[-1]:
            yield from increasing_lists_generator(n - 1, current_list + [i])

def main():
    pwr = int(input())
    ans = []
    d_max = 6 # number of digits
    for d in range(2, d_max+1):
        gen = increasing_lists_generator(d)
        
        power_function = lambda x: x**pwr
        
        for n in gen:
            powered_numbers = sum(map(power_function, n))
            list_of_all_permutation = {''.join(map(str, permutation)) for permutation in permutations(n)}
            if str(powered_numbers) in list_of_all_permutation:
                ans.append(powered_numbers)
    print(sum(ans))

if __name__ == "__main__":
    main()
