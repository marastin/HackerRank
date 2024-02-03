def merge_the_tools(string, k):
    # your code goes here
    sub_strings = substring_gen(string, k)
    for sub in sub_strings:
        ans = sub[0]
        for letter in sub:
            if letter not in ans:
                ans += letter
        print(ans)


def substring_gen(string: str, k: int):
    while len(string) > 0:
        sub = ''
        if len(string) >= k:
            sub = string[0:k]
            string = string[k:]
        yield sub
    return ''
    
    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)