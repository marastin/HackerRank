def minion_game(string):
    stuart = calc_stuart_points(string.upper())
    kevin = calc_kevin_points(string.upper())
    
    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif stuart < kevin:
        print(f"Kevin {kevin}")
    else:
        print(f"Draw")

def calc_stuart_points(string: str) -> int:
    result = 0
    vowels = "AEIOU"
    result = 0
    L = len(string)
    for idx in range(L):
        if string[idx] not in vowels:
            result += L - idx
    return result

    
def calc_kevin_points(string: str) -> int:
    result = 0
    vowels = "AEIOU"
    result = 0
    L = len(string)
    for idx in range(L):
        if string[idx] in vowels:
            result += L - idx
    return result

if __name__ == '__main__':
    s = input()
    minion_game(s)